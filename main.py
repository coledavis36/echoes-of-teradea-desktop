"""Echoes of Teradea Desktop — A local helper for Harvest Moon: Echoes of Teradea farm folders, animal barns, and festival shots."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='echoes_of_teradea_desktop',
        description='A local helper for Harvest Moon: Echoes of Teradea farm folders, animal barns, and festival shots.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Echoes of Teradea Desktop')
    print('Keep the farm on disk before a festival patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
