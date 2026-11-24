"""make.fun entry: Two Days of Quiet Dread.

Writes the entered one-line code review comment to the output directory
as entry.txt. The comment lives in entry.txt beside this file and is
copied byte-for-byte, so the graded output is exactly the entered line:
a single line of at most 140 characters that approves a pull request
while carrying quiet existential dread.
"""

import os


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.txt")
    with open(source, "rb") as fh:
        data = fh.read()
    # Mirror the bounty gate before writing: UTF-8 text of 1 to 140
    # characters, not only white space, on a single line.
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
