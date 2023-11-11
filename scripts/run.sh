#/bin/bash
cd $(git rev-parse --show-toplevel)
docker run -i --rm --user 1001 --hostname ex amazonlinux:exfiltrieve python3 - < exfiltrieve/scan.py
