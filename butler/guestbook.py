from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Guest:
    username: str
    display_name: str
    first_seen: str


class Guestbook:
    def __init__(self) -> None:
        self._guests: dict[str, Guest] = {}

    def add_guest(
        self,
        username: str,
        display_name: str,
    ) -> bool:
        """
        Add a guest if they are not already present.

        Returns True for a new guest.
        Returns False if they were already recorded.
        """

        key = username.casefold()

        if key in self._guests:
            return False

        self._guests[key] = Guest(
            username=username,
            display_name=display_name,
            first_seen=datetime.now(timezone.utc).isoformat(),
        )

        return True

    def guest_count(self) -> int:
        return len(self._guests)

    def guest_names(self) -> list[str]:
        return [
            guest.display_name
            for guest in self._guests.values()
        ]