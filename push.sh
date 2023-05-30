#!/bin/sh

VERSION=$1
if [$VERSION = ""]; then
  echo "ERROR: please type version. e.g. ./push.sh 1.00"
  exit 1
fi

cd docs
bundle exec jekyll build
cd ..

# git checkout origin/master
sed -i -e  "s/RELEASE_VERSION=[0-9]*\.[0-9][0-9]/RELEASE_VERSION=${VERSION}/g" ./.github/workflows/deploy-version.yml 
git add .
git commit -m "${VERSION}"
git push origin master
