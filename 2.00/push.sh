#!/bin/sh

VERSION=$1

# git checkout origin/master
sed -i -e  "s/RELEASE_VERSION=[0-9]*\.[0-9][0-9]/RELEASE_VERSION=${VERSION}/g" ./.github/workflows/deploy-version.yml 
git add .
git commit -m "${VERSION}"
git push origin master
