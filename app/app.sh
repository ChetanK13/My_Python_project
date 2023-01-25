#!/usr/bin/env bash
set -e -o pipefail

tag=$(cat TAG || echo "Unknown")
echo "Kicking off '$tag'"
uvicorn main:app --workers ${WORKERS-1} --host '0.0.0.0' --port 3000
