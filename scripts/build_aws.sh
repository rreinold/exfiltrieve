#/bin/bash

docker build -t amazonlinux:exfiltrieve -f tests/Dockerfile.amazonlinux .

docker run -it --rm --user 1000 -v $(pwd)/exfiltrieve:/app amazonlinux:exfiltrieve

