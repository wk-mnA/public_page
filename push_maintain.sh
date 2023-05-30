#!/bin/sh

VERSION=$1

# git checkout origin/master
sed -i -e  "s/RELEASE_VERSION=[0-9]*\.[0-9][0-9]/RELEASE_VERSION=${VERSION}/g" ./.github/workflows/deploy-version.yml 
git add .
git commit -m "${VERSION}"
git push origin master

git branch
git checkout gh-pages
git fetch
git pull origin origin/gh-pages
ln -sf $VERSION latest
# git config user.name "$(git --no-pager log --format=format:'%an' -n 1)"
# git config user.email "$(git --no-pager log --format=format:'%ae' -n 1)"
git add .
git commit -m "redirect latest to new version $VERSION"
git push origin origin/gh-pages

git checkout master
