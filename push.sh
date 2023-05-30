#!/bin/sh

VERSION=$1
if [ $VERSION = "" ]; then
  echo "ERROR: please type version. e.g. ./push.sh 1.00"
  exit 1
fi

sed -i -e  "s/version: v[0-9]*\.[0-9][0-9]/version: v${VERSION}/g" ./docs/_config.yml 
sed -i -e  "s/baseurl: ""/public_page/[0-9]*\.[0-9][0-9]/baseurl: ""/public_page/${VERSION}/g" ./docs/_config.yml 

cd docs
bundle exec jekyll build
cd ..

# git checkout origin/master
sed -i -e  "s/RELEASE_VERSION=[0-9]*\.[0-9][0-9]/RELEASE_VERSION=${VERSION}/g" ./.github/workflows/deploy-version.yml 
git add .
git commit -m "${VERSION}"
git push origin master
