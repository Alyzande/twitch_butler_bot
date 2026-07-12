import asyncio

from butler.bot import run_bot
from config import validate_config


def main() -> None:
    validate_config()
    asyncio.run(run_bot())


if __name__ == "__main__":
    main()