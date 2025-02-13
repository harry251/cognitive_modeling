# Problem 3: Git and GitHub (12 points)

1. **Create a public GitHub repository, create and add a team logo to the README file, along with some basic introductory notes on why cognitive modeling is important for psychology and cognitive science.**

   - Added a `README.md` file with the following:
     - A team logo and 
     - An introduction.

   - Added an `environment.yml` file to the root directory of the repository with all the discussed dependencies.

   - Created two separate branches (`Harry` and `Shichao`).

2. **Create a merge conflict (either for some of the coding exercises or a mock conflict) and resolve it.**

Create a mock conflict: Commit 0d1df76 (Change beta parameters on merge_conflict branch)
   and Commit fa4e3ae (Change beta parameter on main branch)

Resolved mock conflicts in the following commit: Commit d2f6d69

3. **Explain the differences between the following git commands**
   - **git restore:** Used to undo changes in the working directory or staging area without affecting commit history.  
     Example: `git restore file.txt`  
     This reverts `file.txt` in the working directory to the last committed state.
   - **git checkout:** Used to switch branches, restore files to a previous commit, or discard changes.  
     Example: `git checkout HEAD file.txt`  
     This discards any uncommitted changes in `file.txt` and resets it to the state in the last commit.
   - **git reset:** Used to move the HEAD pointer and undo changes in the staging area and/or working directory, with optional effects on commit history.  
     Example: `git reset --hard HEAD`  
     Resets both the staging area and working directory to the last commit.
   - **git revert:** Used to undo changes in a commit by creating a new commit that negates those changes, preserving commit history.  
     Example: `git revert abc123`  
     This creates a new commit that reverses the changes in `abc123`.

4. **Fill in the following table:**

| **Command**   | **Affects Commit History?** | **Affects Staging Area?** | **Affects Working Directory?** | **Typical Use Case**                                                                                     |
|---------------|------------------------------|---------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------|
| `git reset`   | Yes (depending on mode)      | Yes                       | Yes (in `--hard` mode)         | Unstage changes (`--mixed`), move HEAD to a prior commit, or reset both staging and working directory (`--hard`). |
| `git restore` | No                           | Yes (with `--staged`)     | Yes                            | Discard changes in the working directory or unstage files with `--staged`. Used for undoing without affecting history. |
| `git rm`      | No                           | Yes                       | Yes                            | Remove a file from both the working directory and staging area, or just the staging area with `--cached`. |