"""Entry for make.fun bounty: One-Line Roast: The Gadget You Use Every Day.

Writes the entry line to /output/entry.txt with no trailing newline.
A single original roast of an everyday gadget, at most 200 characters.
"""

from pathlib import Path

ENTRY_TEXT = (
    "My smart kettle needs a firmware update to boil water, a substance "
    "that has been boiling successfully for billions of years without Wi-Fi."
)

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
