#!/usr/bin/env python3
"""Demonstration executor for the ANVIL execution contract.

This is a stand in runtime, not a model. It reads a station packet, and for
reviewer stations it answers with a passing review JSON; for every other
station it answers with a short plain text note. It exists so the Taskline
repository can demonstrate the execute mode plumbing end to end: packets in,
outputs recorded, reviews feeding the approver, deploy and verification
afterwards. A real deployment would replace this command in anvil.yaml with
an actual agent runtime (for example a local agent CLI or an HTTP endpoint).
"""

import json
import sys
from pathlib import Path


def station_of(packet_path):
    for line in Path(packet_path).read_text(encoding="utf-8").splitlines():
        if line.startswith("# Task packet:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def main():
    packet_path = sys.argv[1]
    station = station_of(packet_path)
    if station.startswith("reviewer"):
        print(json.dumps({
            "station": station,
            "verdict": "pass",
            "findings": [f"Demonstration review by {station}: the change matches the spec and its tests."],
        }))
    else:
        print(f"Demonstration executor completed station {station} for this work order.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
