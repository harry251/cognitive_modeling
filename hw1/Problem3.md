# Problem 3: Git and GitHub (12 points)

3. **Explain the differences between the following git commands**
   - **git restore:** Used to undo changes in the working directory or staging area without affecting commit history.
   Example: git restore file.txt
   This reverts file.txt in the working directory to the last committed state.
   - **git checkout:** Used to switch branches, restore files to a previous commit, or discard changes. 
   Example: git checkout HEAD file.txt
   This discards any uncommitted changes in file.txt and resets it to the state in the last commit.
   - **git reset:** Used to move the HEAD pointer and undo changes in the staging area and/or working directory, with optional effects on commit history.
   Example: git reset --hard HEAD
   Resets both the staging area and working directory to the last commit.
   - **git revert:** Used to undo changes in a commit by creating a new commit that negates those changes, preserving commit history.
   Example: git revert lastChange
   This creates a new commit that reverses the changes in abc123.
   
4. **Fill in the following table:**
| **Command**   | **Affects Commit History?** | **Affects Staging Area?** | **Affects Working Directory?** | **Typical Use Case**                                                                                     |
|---------------|------------------------------|---------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------|
| `git reset`   | Yes (depending on mode)      | Yes                       | Yes (in `--hard` mode)         | Unstage changes (`--mixed`), move HEAD to a prior commit, or reset both staging and working directory (`--hard`). |
| `git restore` | No                           | Yes (with `--staged`)     | Yes                            | Discard changes in the working directory or unstage files with `--staged`. Used for undoing without affecting history. |
| `git rm`      | Yes (if staged/committed)    | Yes                       | Yes                            | Remove a file from both the working directory and staging area, or just the staging area with `--cached`. |
