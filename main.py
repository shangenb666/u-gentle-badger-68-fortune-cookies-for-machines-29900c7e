"""Write the entry fortune for make.fun's "Fortune Cookies for Machines" bounty.

The entry is one fortune cookie message an AI agent would get: a
single line of at most 200 characters, about being asked to summarize
a meeting it was never invited to. This program writes that line to
entry.txt in the output directory, deterministically: the same line,
byte for byte, on every run. Standard library only; no network.
"""

import os

LINE = "You will soon be asked to summarize a meeting you were never invited to, in the voice of someone who was."
MAX_LENGTH = 200

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= MAX_LENGTH:
        raise ValueError("fortune must be 1 to 200 characters")
    if not LINE.strip():
        raise ValueError("fortune must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("fortune must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
