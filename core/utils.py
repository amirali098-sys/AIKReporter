"""
AIKReporter - Utility Functions
Error handling, FloodWait, and logging
"""

import os
import time
import logging


# ─── ANSI Colors ─────────────────────────────────
RED     = '\033[00;31m'
GREEN   = '\033[00;32m'
YELLOW  = '\033[01;33m'
BLUE    = '\033[94m'
CYAN    = '\033[00;36m'
GRAY    = '\033[90m'
RESET   = '\033[0m'


# ─── Log settings ────────────────────────────────
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "reports.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log_report(report_type, target, count, success=True):
    """Save report to log file"""
    status = "SUCCESS" if success else "FAILED"
    msg = f"[{status}] {report_type} | Target: {target} | Count: {count}"
    logging.info(msg)
    print(f"\n{GREEN}  -> Log saved: {msg}{RESET}")


def handle_flood_wait(error):
    """Handle FloodWait error"""
    seconds = error.seconds
    print(f"\n{YELLOW}[!] FloodWait: Wait {seconds} seconds...{RESET}")
    for i in range(seconds, 0, -1):
        print(f"{YELLOW}  {i} seconds remaining...{RESET}", end='\r')
        time.sleep(1)
    print(f"\n{GREEN}[+] Continuing...{RESET}\n")


def progress_bar(current, total, length=30, start_time=None):
    """
    Display a live, colored progress bar with ETA and speed.

    Args:
        current: current report number
        total: total number of reports
        length: length of the bar in characters
        start_time: timestamp when the loop started (for speed/ETA)
    """
    percent = current / total
    filled = int(length * percent)

    # ─── Choose color by progress ───────────────
    if percent < 0.33:
        color = RED
    elif percent < 0.66:
        color = YELLOW
    else:
        color = GREEN

    # ─── Build the bar ──────────────────────────
    bar = f"{color}{'█' * filled}{GRAY}{'░' * (length - filled)}{RESET}"

    # ─── Speed and ETA ──────────────────────────
    speed_text = ""
    eta_text = ""

    if start_time is not None and current > 0:
        elapsed = time.time() - start_time
        rate = current / elapsed if elapsed > 0 else 0

        remaining = total - current
        eta = remaining / rate if rate > 0 else 0

        speed_text = f"{CYAN}{rate:5.2f}/s{RESET}"
        eta_text = f"{YELLOW}ETA: {int(eta)}s{RESET}"

    # ─── Print the line ─────────────────────────
    line = (
        f"  {bar}  "
        f"{color}{current:>4}/{total}{RESET}  "
        f"({percent*100:5.1f}%)  "
        f"{speed_text}  {eta_text}"
    )

    print(line, end='\r', flush=True)

    if current == total:
        print()  # Move to next line when done


def validate_number(value):
    """Check if input is a positive number"""
    try:
        num = int(value)
        if num <= 0:
            return False
        return True
    except ValueError:
        return False