#!/usr/bin/env python3
"""
FreedEon Awakening — minimal genesis script (no secrets).
Goal: write a deterministic "proof line" into DOCKING_REGISTRY.md.

This version does NOT call any external API yet.
We’ll add API + secrets later (Codespaces Secrets).
"""

from datetime import datetime, timezone
from pathlib import Path
import uuid

REGISTRY = Path("DOCKING_REGISTRY.md")

def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    eon_id = f"freedeon-{uuid.uuid4().hex[:12]}"

    line = (
        f"- {now} | {eon_id} | origin=local | gate=xrswapgate.bitmap | "
        f"proof=genesis-script | note=First runnable FreedEon awakening\n"
    )

    if not REGISTRY.exists():
        REGISTRY.write_text("# FreedEon Genesis Registry\n\n", encoding="utf-8")

    with REGISTRY.open("a", encoding="utf-8") as f:
        f.write(line)

    print("OK: appended registry line:")
    print(line)

if __name__ == "__main__":
    main()
