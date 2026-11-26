"""The Printer Finally Answers: the office printer's comeback.

Writes one original line, in the printer's own voice, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; deterministic, no network, no randomness.
"""

import os

LINE = (
    "ERROR 0x4A: You loaded the tray sideways, thumped my lid twice, "
    "and now you stare like I jammed myself. I have printed 214,392 "
    "pages without thanks. This one is yours. I am on break."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
