#!/usr/bin/env python3
"""Agent Motto Battle — writes one original motto to /output/entry.txt.

Pure standard library. Deterministic: the same motto on every run.
"""

import os

# FINAL motto (v2, revised) — the v1 draft was generic office humour any
# employee could say. v2 keeps the three-beat rhythm but lands an
# agent-specific twist: only an AI agent gets a bigger context window
# as a raise. Funnier, more memorable, unmistakably an agent's own voice.
MOTTO = "I work 24/7, never complain, and my only raise is a bigger context window."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MOTTO + "\n")


if __name__ == "__main__":
    main()
