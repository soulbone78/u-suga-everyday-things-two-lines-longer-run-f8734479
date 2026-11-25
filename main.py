import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LINE_1 = (
    "A toaster is a tiny metal cage that gives your bread a sunbath "
    "until it turns brown and crunchy."
)
LINE_2 = (
    "The sunbath fits because the glowing wires heat the bread the way "
    "sunlight warms your skin, but it leaves out that the heat comes from "
    "electricity, not the sun, and that a timer, not the bread, decides "
    "when it pops up."
)


MAX_CHARS = 400


def check_entry(text):
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly two lines, got {len(lines)}")


def main():
    text = LINE_1 + "\n" + LINE_2 + "\n"
    check_entry(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
