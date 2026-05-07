#!/bin/bash

mkdir -p actions-runner && cd actions-runner
curl -o actions-runner-osx-arm64-2.334.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.334.0/actions-runner-osx-arm64-2.334.0.tar.gz
echo "760899b29fd4e942076bcd1160a662bf83c15d9ce8a8cc466763aec7e582b21b  actions-runner-osx-arm64-2.334.0.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-osx-arm64-2.334.0.tar.gz

./config.sh --url https://github.com/paridhishr3/github-gists-EE --token $TOKEN --unattended --replace
./run.sh