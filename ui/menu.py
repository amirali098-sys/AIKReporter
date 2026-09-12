"""
AIKReporter - Menus
Interactive menus
"""

from prettytable import PrettyTable
from ui.banner import RED, BLUE, CYAN, GREEN, YELLOW, GRAY, RESET


def main_menu():
    """Main menu"""
    table = PrettyTable()
    table.field_names = [f"{BLUE}Number{RESET}", f"{BLUE}Option{RESET}"]
    table.add_row([f"{RED}1{RESET}", f"{GREEN}Report Channel{RESET}"])
    table.add_row([f"{RED}2{RESET}", f"{GREEN}Report Account{RESET}"])
    table.add_row([f"{RED}3{RESET}", f"{GREEN}Report Group{RESET}"])
    table.add_row([f"{RED}4{RESET}", f"{GREEN}Exit{RESET}"])
    print(table)
    return input(f"{YELLOW}Choose: {RESET}")


def reason_menu():
    """Reason menu"""
    table = PrettyTable()
    table.field_names = [f"{BLUE}Number{RESET}", f"{BLUE}Reason{RESET}"]
    reasons = [
        "Spam", "Pornography", "Violence", "Child Abuse",
        "Other", "Copyright", "Fake", "Geo Irrelevant",
        "Illegal Drugs", "Personal Details"
    ]
    for i, reason in enumerate(reasons, 1):
        table.add_row([f"{RED}{i}{RESET}", f"{GREEN}{reason}{RESET}"])
    print(table)
    return input(f"{YELLOW}Choose reason: {RESET}")