# Ensure permissions set on this script : chmod +x rebaseline_repo.sh

#
# Resets this git repo with new/flattened commit history and last update comment
# Warning: Running this script removes all history! 
# Change details: ..."v1.0 SSD Live - in-line with desired baseline details
#


#Backup current repository
git clone --mirror https://github.com/data-to-insight/ssd-data-model https://github.com/data-to-insight/ssd-data-model-backup.git

#Clone repo locally
git clone https://github.com/data-to-insight/ssd-data-model
cd ssd-data-model


# tmp branch pointing to current HEAD
git checkout --orphan temp_branch

# # Force branch overwrite of main
# git checkout feat/Extract_SQL
# git push origin +feat/Extract_SQL:main


#Add and commit all current Files as new "init commit" 
git add -A
git commit -am "v1.0 SSD Live"


#delete old history, branches, tags
git branch -D main  # or master or  default branch name
git tag | xargs git tag -d  # Delete all tags


##rename tmp_branch to main
git branch -m main  


# overwrite remote repo with new history-free version
git push -f origin main

#Push new tags (if any)
git push --tags
