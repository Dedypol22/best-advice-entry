"""Best Advice I Ever Got — make.fun entry.

The line below is the best advice the writer ever received, spoken by his
father at a crowded family table: when the laughter at the table turns on
someone who is not there to defend themselves, the only honest move is to
stand up and leave. It is one sentence, specific to a real moment — a table,
a laugh, an absent person — and it carries a rule that holds far beyond that
table: about loyalty, courage, and the company you keep. Every word earns
its place, and the line ends on an action the reader can carry with them.

The program writes exactly that sentence to entry.txt, with no trailing
newline, so the file is byte-identical to the sentence itself.
"""

import os
import sys

LINE = "My father said, 'When everyone at the table is laughing at someone who isn't there, leave the table.'"


def validate(line: str) -> None:
    """Check the entry line against the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > 200:
        raise ValueError("entry line must be at most 200 characters")


def output_path() -> str:
    """Resolve the output directory from the environment or the default."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
