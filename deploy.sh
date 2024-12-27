#! /bin/bash

# load environment
. ./.env

# load colours
. ./scripts/colours_include.sh

echo -e "${YELLOW}***"
echo -e "*** running: ${GREEN} ---> ${RED} gcloud config set project ${PROJECT_ID}${RESET}"
gcloud config set project ${PROJECT_ID}
echo -e "*** running: ${GREEN} ---> ${RED} gcloud beta run deploy ${ENDPOINT} --region ${GCP_REGION} --image gcr.io/${PROJECT_ID}/${ENDPOINT} --port ${RUNPORT} --cpu 1 --memory 1Gi --max-instances ${MAX_INSTANCES} --min-instances ${MIN_INSTANCES} --no-cpu-boost --cpu-throttling --allow-unauthenticated --service-account=${GCP_SERVICE_ACCOUNT} ${RESET}"
echo -e "${YELLOW}***"

gcloud beta run deploy ${ENDPOINT} \
    --region ${GCP_REGION} \
    --image gcr.io/${PROJECT_ID}/${ENDPOINT} \
    --port ${RUNPORT} \
    --cpu 1 \
    --memory 1Gi \
    --max-instances ${MAX_INSTANCES} \
    --min-instances ${MIN_INSTANCES} \
    --no-cpu-boost \
    --cpu-throttling \
    --allow-unauthenticated \
	 --service-account=${GCP_SERVICE_ACCOUNT}

# EOF
