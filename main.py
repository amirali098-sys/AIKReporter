"""
AIKReporter - Main Entry Point
Developer: AmirAli (AIK)
"""

import os
import sys

# Add project path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.banner import show_banner, show_mode_art, clear_screen, RED, BLUE, GREEN, YELLOW, GRAY, RESET
from ui.menu import main_menu, reason_menu
from core.client import TGClient
from core.reporter import Reporter
from core.utils import validate_number
from core.config import save_config, load_config


def get_credentials():
    """Get API credentials from user or load from file"""
    config = load_config()

    if config:
        print(f"{GREEN}[+] Found saved credentials{RESET}")
        print(f"{GRAY}  API ID: {config['api_id']}{RESET}")
        print(f"{GRAY}  Phone:  {config['phone']}{RESET}\n")

        use_saved = input(f"{YELLOW}Use saved credentials? (y/n): {RESET}").lower()
        if use_saved == 'y':
            return config['api_id'], config['api_hash'], config['phone']

    print(f"{BLUE}=== Telegram API Credentials ==={RESET}")
    print(f"{GRAY}(Get them from my.telegram.org){RESET}\n")
    api_id = input(f"{YELLOW}API ID: {RESET}")
    api_hash = input(f"{YELLOW}API Hash: {RESET}")
    phone = input(f"{YELLOW}Phone (with +): {RESET}")

    save_config(api_id, api_hash, phone)
    return api_id, api_hash, phone


def run_report(reporter, mode):
    """Run reporting process"""
    clear_screen()
    show_mode_art(mode)

    target = input(f"{YELLOW}Target username (without @): {RESET}")

    clear_screen()
    show_mode_art(mode)
    print(f"{BLUE}Target: {target}{RESET}\n")

    method = reason_menu()

    count = input(f"{YELLOW}Number of reports: {RESET}")
    if not validate_number(count):
        print(f"{RED}[!] Invalid number!{RESET}")
        input(f"\n{GRAY}Press Enter to continue...{RESET}")
        return

    count = int(count)

    message = ""
    if method == "5":
        message = input(f"{YELLOW}Report message: {RESET}")

    clear_screen()
    show_mode_art(mode)

    if mode == "channel":
        reporter.report_channel(target, method, count, message)
    elif mode == "account":
        reporter.report_account(target, method, count, message)
    elif mode == "group":
        reporter.report_channel(target, method, count, message)


def main():
    """Main function"""
    show_banner()

    api_id, api_hash, phone = get_credentials()

    with TGClient(api_id, api_hash, phone) as client:
        reporter = Reporter(client)

        while True:
            clear_screen()
            show_banner()
            choice = main_menu()

            if choice == "1":
                run_report(reporter, "channel")
            elif choice == "2":
                run_report(reporter, "account")
            elif choice == "3":
                run_report(reporter, "group")
            elif choice == "4":
                clear_screen()
                print(f"{GREEN}Goodbye! 👋{RESET}")
                break
            else:
                print(f"{RED}[!] Invalid choice!{RESET}")

            input(f"\n{GRAY}Press Enter to continue...{RESET}")


if __name__ == "__main__":
    main()