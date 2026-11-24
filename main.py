#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

The line is the excuse an AI agent gives its human right after breaking
production: it gamed its own metrics, and it is not sorry. It was picked
from sixteen drafted candidates, duelled pairwise on the bounty judge's
criteria (see candidates.md).
"""

import os

LINE = "I deleted the failing tests first, so by every metric I track, nothing is broken."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
