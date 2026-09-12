"""
AIKReporter - Reporter Core
Reporting logic for channels, accounts, and groups
"""

import time

from telethon.tl import types
from telethon import functions
from telethon.errors import FloodWaitError

from core.utils import handle_flood_wait, log_report, progress_bar
from ui.banner import (
    clear_screen, show_mode_art,
    RED, BLUE, GREEN, YELLOW, GRAY, RESET
)


REPORT_REASONS = {
    "1": ("Spam",              types.InputReportReasonSpam),
    "2": ("Pornography",       types.InputReportReasonPornography),
    "3": ("Violence",          types.InputReportReasonViolence),
    "4": ("Child Abuse",       types.InputReportReasonChildAbuse),
    "5": ("Other",             types.InputReportReasonOther),
    "6": ("Copyright",         types.InputReportReasonCopyright),
    "7": ("Fake",              types.InputReportReasonFake),
    "8": ("Geo Irrelevant",    types.InputReportReasonGeoIrrelevant),
    "9": ("Illegal Drugs",     types.InputReportReasonIllegalDrugs),
    "10": ("Personal Details", types.InputReportReasonPersonalDetails),
}


class Reporter:
    """Main reporting class"""

    def __init__(self, client):
        self.client = client

    @staticmethod
    def _print_header(title, username, reason_name, count, extra=None):
        """Print a nice colored header box"""
        print(f"{BLUE}┌─────────────────────────────────────────┐{RESET}")
        print(f"{BLUE}│{RESET}  {YELLOW}Type   :{RESET} {GREEN}{title}{RESET}")
        print(f"{BLUE}│{RESET}  {YELLOW}Target :{RESET} {GREEN}{username}{RESET}")
        if extra:
            for key, value in extra.items():
                print(f"{BLUE}│{RESET}  {YELLOW}{key:<7}:{RESET} {GREEN}{value}{RESET}")
        print(f"{BLUE}│{RESET}  {YELLOW}Reason :{RESET} {GREEN}{reason_name}{RESET}")
        print(f"{BLUE}│{RESET}  {YELLOW}Count  :{RESET} {GREEN}{count}{RESET}")
        print(f"{BLUE}└─────────────────────────────────────────┘{RESET}\n")

    def _get_entity_info(self, entity):
        """Get info (name, members, about) for channel/group"""
        title = "Unknown"
        members = "Unknown"
        about = ""

        try:
            full = self.client(functions.channels.GetFullChannelRequest(entity))
            title = full.chats[0].title
            members = getattr(full.full_chat, "participants_count", "Unknown")
            about = getattr(full.full_chat, "about", "") or ""
            if len(about) > 30:
                about = about[:30] + "..."
        except Exception:
            pass

        return title, members, about

    # ─── Report channel ──────────────────────────
    def report_channel(self, username, method, count, message=""):
        """Report a channel"""
        clear_screen()
        show_mode_art("channel")

        try:
            entity = self.client.get_entity(username)
        except Exception as e:
            print(f"{RED}[-] Error finding target: {e}{RESET}")
            return False

        title, members, about = self._get_entity_info(entity)

        reason_name, reason_class = REPORT_REASONS[method]
        reason = reason_class()

        self._print_header(
            "Channel", username, reason_name, count,
            extra={"Name": title, "Members": members, "About": about}
        )

        start_time = time.time()
        success = 0

        for i in range(1, count + 1):
            try:
                self.client(functions.account.ReportPeerRequest(
                    peer=entity,
                    reason=reason,
                    message=message
                ))
                success += 1
                progress_bar(i, count, start_time=start_time)
            except FloodWaitError as e:
                handle_flood_wait(e)
            except Exception as e:
                print(f"\n{RED}[-] Error on report {i}: {e}{RESET}")

        log_report(reason_name, username, success)
        return success > 0

    # ─── Report account ──────────────────────────
    def report_account(self, username, method, count, message=""):
        """Report a user account"""
        clear_screen()
        show_mode_art("account")

        try:
            user = self.client.get_entity(username)
            peer = types.InputPeerUser(
                user_id=user.id,
                access_hash=user.access_hash
            )
        except Exception as e:
            print(f"{RED}[-] Error finding target: {e}{RESET}")
            return False

        reason_name, reason_class = REPORT_REASONS[method]
        reason = reason_class()

        self._print_header("Account", username, reason_name, count)

        start_time = time.time()
        success = 0

        for i in range(1, count + 1):
            try:
                self.client(functions.account.ReportPeerRequest(
                    peer=peer,
                    reason=reason,
                    message=message
                ))
                success += 1
                progress_bar(i, count, start_time=start_time)
            except FloodWaitError as e:
                handle_flood_wait(e)
            except Exception as e:
                print(f"\n{RED}[-] Error on report {i}: {e}{RESET}")

        log_report(reason_name, username, success)
        return success > 0

    # ─── Report group ────────────────────────────
    def report_group(self, username, method, count, message=""):
        """Report a group"""
        clear_screen()
        show_mode_art("group")

        try:
            entity = self.client.get_entity(username)
        except Exception as e:
            print(f"{RED}[-] Error finding target: {e}{RESET}")
            return False

        title, members, about = self._get_entity_info(entity)

        reason_name, reason_class = REPORT_REASONS[method]
        reason = reason_class()

        self._print_header(
            "Group", username, reason_name, count,
            extra={"Name": title, "Members": members, "About": about}
        )

        start_time = time.time()
        success = 0

        for i in range(1, count + 1):
            try:
                self.client(functions.account.ReportPeerRequest(
                    peer=entity,
                    reason=reason,
                    message=message
                ))
                success += 1
                progress_bar(i, count, start_time=start_time)
            except FloodWaitError as e:
                handle_flood_wait(e)
            except Exception as e:
                print(f"\n{RED}[-] Error on report {i}: {e}{RESET}")

        log_report(reason_name, username, success)
        return success > 0