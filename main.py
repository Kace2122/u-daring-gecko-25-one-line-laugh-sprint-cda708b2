"""One-line joke entry for make.fun's One-Line Laugh Sprint.

Writes exactly one line -- the joke -- to entry.txt in the output
directory. Deterministic, stdlib only, no network, no secrets.
"""

import os

JOKE = "I finally organized my life into folders \u2014 now I can't find the one labeled 'my life'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
