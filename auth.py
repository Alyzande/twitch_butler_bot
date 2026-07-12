import asyncio

from twitchAPI.oauth import UserAuthenticationStorageHelper
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope

from config import TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET


TARGET_SCOPES = [
    AuthScope.USER_READ_CHAT,
    AuthScope.USER_WRITE_CHAT,
]


async def authenticate() -> None:
    twitch = await Twitch(
        app_id=TWITCH_CLIENT_ID,
        app_secret=TWITCH_CLIENT_SECRET,
    )

    helper = UserAuthenticationStorageHelper(
        twitch,
        TARGET_SCOPES,
    )

    await helper.bind()

    print("Twitch authentication completed successfully.")

    await twitch.close()


if __name__ == "__main__":
    asyncio.run(authenticate())