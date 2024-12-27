#! /bin/bash

# load environment
. ./.env

# load colours
. ./scripts/colours_include.sh

echo -e "${YELLOW}***"
echo -e "*** running: ${GREEN}---> ${RED} docker build -t gcr.io/${PROJECT_ID}/${ENDPOINT} . ${RESET}"
echo -e "${YELLOW}***"

docker build -t gcr.io/${PROJECT_ID}/${ENDPOINT} .

# EOF
