#! /bin/bash

# load environment
. ./.env

# load colours
. ./scripts/colours_include.sh

echo -e "${YELLOW}***"
echo -e "*** running: ${GREEN}---> ${RED} docker push gcr.io/${PROJECT_ID}/${ENDPOINT} ${RESET}"
echo -e "${YELLOW}***"

docker push gcr.io/${PROJECT_ID}/${ENDPOINT}

# EOF
