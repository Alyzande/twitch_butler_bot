import asyncio

from twitchAPI.eventsub.websocket import EventSubWebsocket
from twitchAPI.helper import first
from twitchAPI.object.eventsub import ChannelChatMessageEvent
from twitchAPI.oauth import UserAuthenticationStorageHelper
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope
from butler.guestbook import Guestbook
from butler.greetings import greeting_for

from config import (
    BOT_NAME,
    TWITCH_CHANNEL,
    TWITCH_CLIENT_ID,
    TWITCH_CLIENT_SECRET,
)


TARGET_SCOPES = [
    AuthScope.USER_READ_CHAT,
    AuthScope.USER_WRITE_CHAT,
]

guestbook = Guestbook()

async def on_chat_message(event: ChannelChatMessageEvent) -> None:
    """Print chat messages and record first-time chatters."""

    username = event.event.chatter_user_login
    display_name = event.event.chatter_user_name
    message = event.event.message.text

    print(f"{display_name}: {message}")

    is_new_guest = guestbook.add_guest(
        username=username,
        display_name=display_name,
    )

    if is_new_guest:
        print(
            f"New guest recorded: {display_name} "
            f"(guest #{guestbook.guest_count()})"
        )

        greeting = greeting_for(display_name)

        print(f"Butler reply: {greeting}")


async def run_bot() -> None:
    """Connect to Twitch and listen for chat messages."""

    twitch = await Twitch(
        app_id=TWITCH_CLIENT_ID,
        app_secret=TWITCH_CLIENT_SECRET,
    )

    auth_helper = UserAuthenticationStorageHelper(
        twitch,
        TARGET_SCOPES,
    )

    await auth_helper.bind()

    bot_user = await first(
        twitch.get_users(logins=[BOT_NAME])
    )

    channel_user = await first(
        twitch.get_users(logins=[TWITCH_CHANNEL])
    )

    if bot_user is None:
        raise RuntimeError(
            f"Could not find bot account: {BOT_NAME}"
        )

    if channel_user is None:
        raise RuntimeError(
            f"Could not find Twitch channel: {TWITCH_CHANNEL}"
        )

    eventsub = EventSubWebsocket(twitch)
    eventsub.start()

    await eventsub.listen_channel_chat_message(
        broadcaster_user_id=channel_user.id,
        user_id=bot_user.id,
        callback=on_chat_message,
    )

    print("The butler is now attending the drawing room.")
    print(f"Listening as: {bot_user.display_name}")
    print(f"Watching channel: {channel_user.display_name}")
    print("Send a message in Twitch chat to test it.")
    print("Press Enter here to stop the butler.")

    try:
        await asyncio.to_thread(input)
    finally:
        await eventsub.stop()
        await twitch.close()

        print("The butler has retired for the evening.")