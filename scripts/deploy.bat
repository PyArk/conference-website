@ECHO off

SET CURR_BRANCH="git rev-parse --abbrev-ref HEAD"
IF "%CURR_BRANCH" == "master" (
    echo "The current branch must be master to deploy."
    echo "Run 'git checkout master' and merge your changes there first."
    exit
)

git checkout deploy
git merge master
git status
echo "Check the merge, then run git push"
echo "Don't forget to switch back to master"
