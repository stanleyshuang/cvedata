#!/usr/bin/env bash
base_dir=$(dirname "$0")
cvelist_home="$base_dir/../cvelist"
echo "cd $cvelist_home"
      cd $cvelist_home

### 1. Ensure your fork is up to date, especially prior to creating a new 
###    branch (every time you create a new branch). The command for this are:
git fetch upstream
git checkout master
git merge upstream/master

### 2. Optionally push any updates from the upstream CVEProject/cvelist 
###    master back to you fork on Github.com:
git push
