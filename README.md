# DevOps-intern-assessement
# This repository is for my DevOps intern final test codes.

## Name:- Abhilash Shahu
## Date:- 20 october 2025
## Project description:- This repo demonstrates key DevOps skills including scripting, containerization, CI/CD, job orchestration, and monitoring.

## Instruction to RUN Dockerfile:-

docker build -t hello-devops .

docker run hello-devops

## badge

![CI](https://github.com/ABHILASH894/devops-intern-final/actions/workflows/ci.yml/badge.svg)

## command to RUN nomad:- 

nomad job run nomad/hello.nomad

## Monitoring with Grafana Loki

Loki was run locally using Docker and logs from the Nomad container were forwarded manually using curl. See `monitoring/loki_setup.txt` for full setup.
<img width="1366" height="711" alt="nomad output" src="https://github.com/user-attachments/assets/a57dfa42-62bb-47ad-9a88-0e554f716d62" />
<img width="1366" height="727" alt="monitor" src="https://github.com/user-attachments/assets/746160dc-4465-43eb-b8e0-6e42a88a4543" />
<img width="1366" height="729" alt="mlflow output" src="https://github.com/user-attachments/assets/3dfb72c0-c56b-46b2-86e1-d07292d275cb" />
<img width="1366" height="708" alt="dockerfile output" src="https://github.com/user-attachments/assets/f78ab3f8-bf3f-4bf7-8e76-3cbd2a372d1c" />




```bash
./scripts/sysinfo.sh
