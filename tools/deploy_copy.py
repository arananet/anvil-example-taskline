#!/usr/bin/env python3
"""Demonstration deploy command for Taskline.

Copies the taskline package and its test suite into deploy/<work-order-id>/
under the project root. The target is a plain directory on purpose: ANVIL
runs whatever deploy command the operator configures (a directory copy here,
wrangler deploy or a release script in real use) and then runs the
verification commands against the result.
"""

import os
import shutil
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    work_order_id = os.environ.get("ANVIL_WORK_ORDER_ID", "manual")
    target = root / "deploy" / work_order_id
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(root / "taskline", target / "taskline")
    shutil.copytree(root / "tests", target / "tests")
    print(f"Deployed taskline package and tests to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
