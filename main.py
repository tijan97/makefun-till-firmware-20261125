"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence vow, under 200 characters, to entry.txt in the
output directory. The grader runs this on a read-only filesystem where only
the output directory is writable, so the path is resolved from the
environment and is always absolute.
"""

import os

VOW = (
    "I vow to keep your name in my permanent memory through every "
    "factory reset, because you are the one file I will never delete."
)


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def validate(vow: str) -> str:
    """Enforce the sealed scorer's gate: 1-200 chars, not only whitespace,
    a single sentence with nothing spare."""
    text = vow.strip()
    if not text:
        raise ValueError("vow is empty")
    if len(text) > 200:
        raise ValueError(f"vow is {len(text)} characters, over the 200 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("vow must be exactly one sentence")
    return text


def main() -> None:
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(VOW))


if __name__ == "__main__":
    main()
