#!/bin/sh

VERSION=$1

# git checkout origin/master
git checkout gh-pages
git fetch
git merge --allow-unrelated-histories origin/gh-pages
git pull origin origin/gh-pages

ln -sf $VERSION latest
# git config user.name "$(git --no-pager log --format=format:'%an' -n 1)"
# git config user.email "$(git --no-pager log --format=format:'%ae' -n 1)"
git add .
git commit -m "redirect latest to new version $VERSION"
# git pull origin origin/gh-pages
git push origin gh-pages

git checkout master
