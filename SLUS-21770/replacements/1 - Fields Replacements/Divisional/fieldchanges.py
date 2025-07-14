#!/usr/bin/env python3
import os
import argparse
import sys
from datetime import datetime

# ─── Updated mapping from Team → new filename (without “.png”) ───────────────
TEAM_TO_NEWNAME = {
    "Bears":       "e52d38f583479d2e-d8159e08e0a76768-00006214",
    "Bengals":     "d72e59520c173775-d5dc96c489ee179a-00006214",
    "Bills":       "e96949b8de3a733d-6423d9bb1f40fd9-00006214",
    "Broncos":     "7aeb8972cf7b03f0-9cf61e06c760c20f-00006214",
    "Browns":      "2b908238cbac470c-8c4c601fcde58572-00006214",
    "Buccaneers":  "6e5fa1fd5b047899-2d51af3294330da5-00006214",
    "Cardinals":   "2248c8dc85822965-75e61868a60ee76a-00006214",
    "Chargers":    "1dcbabe1e4fdc4bc-94d6413ea110e27f-00006214",
    "Chiefs":      "6778c5b413d6745a-3f1bb461d8d8e9d6-00006214",
    "Colts":       "d669f946e62607f6-c219c4a7f27a0fd8-00006214",
    "Cowboys":     "39807b7c3d4e5414-878281de69b586a7-00006214",
    "Dolphins":    "bf74afeedacc442f-da80130fecb1f958-00006214",
    "Eagles":      "d34d5a59236f24a9-fd363c38c6a9c1f4-00006214",
    "Falcons":     "54cefd8a80c124ae-78d6789e2175aec-00006214",
    "49ers":       "fbffd90bd2b24614-349791819376a10e-00006214",
    "Giants":      "54c817a6d59e95cd-6c06bdf3d0817fd3-00006214",
    "Jaguars":     "cd1c4fad642cf10-ca30b2b8f67c6a4f-00006214",
    "Jets":        "caf804370b25553f-6c06bdf3d0817fd3-00006214",
    "Lions":       "8f75eb409ed28621-b40eeb539f4892fb-00006214",
    "Packers":     "a0c5062095d51b5-ab5d993d5836071c-00006214",
    "Panthers":    "488a606ea9ff9551-6c06bdf3d0817fd3-00006214",
    "Patriots":    "c2b011559a400b7e-d9acd93d84724b70-00006214",
    "Raiders":     "b1310f8db49612ad-6131d4be65d5beb7-00006214",
    "Rams":        "e10b9873b389edbe-d2396a5fed3b72f9-00006214",
    "Ravens":      "2bb10c065006d159-945d0efa2564ba23-00006214",
    "Commanders":  "8c4c741749c2f90-7dcd4b3aa3546628-00006214",
    "Saints":      "881dec8d1bf30759-81bd09fb83d4bf88-00006214",
    "Seahawks":    "3caf69b56315833d-14dd39da09d1edec-00006214",
    "Steelers":    "3a435f23b3e2ec50-b63e9a1efec9ec73-00006214",
    "Texans":      "cc7eaf7bc51df491-e4f8ce05e83f48fe-00006214",
    "Titans":      "9a741d228e26fa5b-14784ff1078a08e0-00006214",
    "Vikings":     "f327e9d05a0f2d83-fcf3c14d98a4d3b7-00006214",
}

def log_action(logfile, action, src, dst=None):
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    if dst:
        logfile.write(f"{timestamp} | {action:<7} | {src} → {dst}\n")
    else:
        logfile.write(f"{timestamp} | {action:<7} | {src}\n")

def rename_pngs(root_dir, dry_run=False):
    log_path = os.path.join(root_dir, 'rename_log.txt')
    with open(log_path, 'a', encoding='utf-8') as logf:
        logf.write(f"\n=== Run at {datetime.now().isoformat(sep=' ', timespec='seconds')} ===\n")
        for dirpath, _, filenames in os.walk(root_dir):
            for fn in filenames:
                if not fn.lower().endswith('.png'):
                    continue
                for team, newbase in TEAM_TO_NEWNAME.items():
                    if team.lower() in fn.lower():
                        src = os.path.join(dirpath, fn)
                        dst = os.path.join(dirpath, newbase + '.png')
                        if dry_run:
                            print(f"[DRY RUN] Would rename:\n  {src}\n→ {dst}\n")
                            log_action(logf, "DRYRUN", src, dst)
                        else:
                            if os.path.exists(dst):
                                print(f"Skipping (target exists): {dst}")
                                log_action(logf, "SKIPPED", dst)
                            else:
                                os.rename(src, dst)
                                print(f"Renamed:\n  {src}\n→ {dst}\n")
                                log_action(logf, "RENAMED", src, dst)
                        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Scan for PNGs whose filename contains an NFL team name and rename them to the mapped GUID."
    )
    parser.add_argument('folder', nargs='?', default='.',
                        help="Root folder to scan (default: current directory)")
    parser.add_argument('--dry-run', action='store_true',
                        help="Show what would be done without renaming")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: “{args.folder}” is not a directory.", file=sys.stderr)
        sys.exit(1)

    rename_pngs(args.folder, dry_run=args.dry_run)
    print("Done. Log written to rename_log.txt")
