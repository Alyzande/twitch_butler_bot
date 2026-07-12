import os

from dotenv import load_dotenv


load_dotenv()


TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID", "").strip()
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET", "").strip()
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL", "").strip().lower()
BOT_NAME = os.getenv("BOT_NAME", "").strip().lower()


def validate_config() -> None:
    """Raise a clear error when required settings are missing."""

    required_values = {
        "TWITCH_CLIENT_ID": TWITCH_CLIENT_ID,
        "TWITCH_CLIENT_SECRET": TWITCH_CLIENT_SECRET,
        "TWITCH_CHANNEL": TWITCH_CHANNEL,
        "BOT_NAME": BOT_NAME,
    }

    missing = [
        name
        for name, value in required_values.items()
        if not value
    ]

    if missing:
        missing_list = ", ".join(missing)
        raise RuntimeError(
            f"Missing required configuration: {missing_list}"
        )