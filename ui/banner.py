"""
AIKReporter - Banner and ASCII Art
Developer: AmirAli (AIK)
Version: 1.0.0
"""

import os
import time
import platform

# ─── Enable ANSI colors on Windows ───────────────
if 'Windows' in platform.uname():
    os.system('')
    try:
        from colorama import init, just_fix_windows_console
        just_fix_windows_console()
    except ImportError:
        os.system("pip install colorama")
        from colorama import init, just_fix_windows_console
        just_fix_windows_console()

# ─── ANSI Color Codes ────────────────────────────
RED     = '\033[00;31m'
BLUE    = '\033[94m'
CYAN    = '\033[00;36m'
GREEN   = '\033[00;32m'
LGREEN  = '\033[01;32m'
YELLOW  = '\033[01;33m'
GRAY    = '\033[90m'
PURPLE  = '\033[01;35m'
ORANGE  = '\033[38;5;130m'
WHITE   = '\033[97m'
RESET   = '\033[0m'


# ─── Main Banner: AIK (Red) + REPORTER (Blue) ────
BANNER = f"""{RED}
   █████████   █████ █████   ████
  ███▒▒▒▒▒███ ▒▒███ ▒▒███   ███▒ 
 ▒███    ▒███  ▒███  ▒███  ███   
 ▒███████████  ▒███  ▒███████    
 ▒███▒▒▒▒▒███  ▒███  ▒███▒▒███   
 ▒███    ▒███  ▒███  ▒███ ▒▒███  
 █████   █████ █████ █████ ▒▒████
▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒ 
{RESET}{BLUE}
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}{GRAY}              Report Telegram Channels & Accounts
{RESET}{YELLOW}              Developer: AmirAli (AIK) | v1.0.0
{RESET}
"""


# ─── Channel Report Art ──────────────────────────
CHANNEL_ART = f"""{RED}
                                                                      
    ▄▄▄▄   ▄▄                                                ▄▄▄▄     
  ██▀▀▀▀█  ██                                                ▀▀██     
 ██▀       ██▄████▄   ▄█████▄  ██▄████▄  ██▄████▄   ▄████▄     ██     
 ██        ██▀   ██   ▀ ▄▄▄██  ██▀   ██  ██▀   ██  ██▄▄▄▄██    ██     
 ██▄       ██    ██  ▄██▀▀▀██  ██    ██  ██    ██  ██▀▀▀▀▀▀    ██     
  ██▄▄▄▄█  ██    ██  ██▄▄▄███  ██    ██  ██    ██  ▀██▄▄▄▄█    ██▄▄▄  
    ▀▀▀▀   ▀▀    ▀▀   ▀▀▀▀ ▀▀  ▀▀    ▀▀  ▀▀    ▀▀    ▀▀▀▀▀      ▀▀▀▀  
                                                                      
{RESET}
{BLUE}        [ Channel Report Mode ]{RESET}
"""


# ─── Account Report Art ──────────────────────────
ACCOUNT_ART = f"""{BLUE}
                                                                      
    ▄▄                                                                
   ████                                                        ██     
   ████     ▄█████▄   ▄█████▄   ▄████▄   ██    ██  ██▄████▄  ███████  
  ██  ██   ██▀    ▀  ██▀    ▀  ██▀  ▀██  ██    ██  ██▀   ██    ██     
  ██████   ██        ██        ██    ██  ██    ██  ██    ██    ██     
 ▄██  ██▄  ▀██▄▄▄▄█  ▀██▄▄▄▄█  ▀██▄▄██▀  ██▄▄▄███  ██    ██    ██▄▄▄  
 ▀▀    ▀▀    ▀▀▀▀▀     ▀▀▀▀▀     ▀▀▀▀     ▀▀▀▀ ▀▀  ▀▀    ▀▀     ▀▀▀▀  
                                                                      
{RESET}
{RED}        [ Account Report Mode ]{RESET}
"""


# ─── Group Report Art ────────────────────────────
GROUP_ART = f"""{PURPLE}
                                                  
    ▄▄▄▄                                          
  ██▀▀▀▀█                                         
 ██         ██▄████   ▄████▄   ██    ██  ██▄███▄  
 ██  ▄▄▄▄   ██▀      ██▀  ▀██  ██    ██  ██▀  ▀██ 
 ██  ▀▀██   ██       ██    ██  ██    ██  ██    ██ 
  ██▄▄▄██   ██       ▀██▄▄██▀  ██▄▄▄███  ███▄▄██▀ 
    ▀▀▀▀    ▀▀         ▀▀▀▀     ▀▀▀▀ ▀▀  ██ ▀▀▀   
                                         ██       
{RESET}
{ORANGE}        [ Group Report Mode ]{RESET}
"""


# ─── Helper: Typewriter effect ───────────────────
def type_text(text, delay=0.001):
    """Print text character by character."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


# ─── Helper: Clear screen ────────────────────────
def clear_screen():
    """Clear terminal screen (Windows / Linux / macOS)."""
    if 'Windows' in platform.uname():
        os.system('cls')
    else:
        os.system('clear')


# ─── Helper: Show main banner ────────────────────
def show_banner():
    """Display the main banner."""
    clear_screen()
    type_text(BANNER)


# ─── Helper: Show mode art ───────────────────────
def show_mode_art(mode):
    """Display art for the chosen mode."""
    if mode == "channel":
        type_text(CHANNEL_ART)
    elif mode == "account":
        type_text(ACCOUNT_ART)
    elif mode == "group":
        type_text(GROUP_ART)