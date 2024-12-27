#!/bin/bash

# Reset
RESET='\x1b[0m'

# Regular Colors
BLACK='\x1b[30m'
RED='\x1b[31m'
GREEN='\x1b[32m'
YELLOW='\x1b[33m'
BLUE='\x1b[34m'
MAGENTA='\x1b[35m'
CYAN='\x1b[36m'
WHITE='\x1b[37m'

# Bold Colors
BOLD_BLACK='\x1b[30;1m'
BOLD_RED='\x1b[31;1m'
BOLD_GREEN='\x1b[32;1m'
BOLD_YELLOW='\x1b[33;1m'
BOLD_BLUE='\x1b[34;1m'
BOLD_MAGENTA='\x1b[35;1m'
BOLD_CYAN='\x1b[36;1m'
BOLD_WHITE='\x1b[37;1m'

# Background Colors
BG_BLACK='\x1b[40m'
BG_RED='\x1b[41m'
BG_GREEN='\x1b[42m'
BG_YELLOW='\x1b[43m'
BG_BLUE='\x1b[44m'
BG_MAGENTA='\x1b[45m'
BG_CYAN='\x1b[46m'
BG_WHITE='\x1b[47m'

# Bold Background Colors
BG_BOLD_BLACK='\x1b[40;1m'
BG_BOLD_RED='\x1b[41;1m'
BG_BOLD_GREEN='\x1b[42;1m'
BG_BOLD_YELLOW='\x1b[43;1m'
BG_BOLD_BLUE='\x1b[44;1m'
BG_BOLD_MAGENTA='\x1b[45;1m'
BG_BOLD_CYAN='\x1b[46;1m'
BG_BOLD_WHITE='\x1b[47;1m'

# Example usage
# echo -e "${BOLD_YELLOW}This is bold yellow text${RESET}"
# echo -e "${RED}${BG_WHITE}This is red text on a white background${RESET}"
# echo -e "${BOLD_CYAN}${BG_BOLD_MAGENTA}This is bold cyan text on a bold magenta background${RESET}"

