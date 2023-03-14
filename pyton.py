fter seeing a conflict, you can do two things:

Decide not to merge. The only clean-ups you need are to reset the index file to the HEAD commit to reverse 2. and to clean up working tree changes made by 2. and 3.; git merge --abort can be used for this.

Resolve the conflicts. Git will mark the conflicts in the working tree. Edit the files into shape and git add them to the index. Use git commit or git merge --continue to seal the deal. The latter command checks whether there is a (interrupted) merge in progress before calling git commit.




Use a mergetool. git mergetool to launch a graphical mergetool which will work you through the merge.

Look at the diffs. git diff will show a three-way diff, highlighting changes from both the HEAD and MERGE_HEAD versions.

Look at the diffs from each branch. git log --merge -p <path> will show diffs first for the HEAD version and then the MERGE_HEAD version.

Look at the originals. git show :1:filename shows the common ancestor, git show :2:filename shows the HEAD version, and git show :3:filename shows the MERGE_HEAD version.

