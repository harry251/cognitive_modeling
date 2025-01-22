# Problem 1: True-False Questions (4 points)
**Mark all statements which are FALSE.**

**False Statements:** 1, 4, 5, 7, 8

1. **Stochastic models will always produce the same output \( $x$ \) given the same input parameters \( $\theta$ \).**  
   **Answer:** False. Stochastic models incorporate randomness, so they may produce different outputs even with the same input parameters.

2. **In psychology, replicability refers to obtaining consistent results using the same data and analysis methods, while reproducibility refers to obtaining consistent results by conducting a new study with different data under similar conditions.**  
   **Answer:** True. 

3. **In Python, the expression `5 + "5"` will result in a `TypeError`.**  
   **Answer:** True.

4. **The `git rebase` command is used to squash commits in the history, but it cannot be used to reapply commits on top of a different base branch.**  
   **Answer:** False. `git rebase` can reapply commits on top of a different base branch.

5. **A detached HEAD state in Git means you are no longer on any branch and cannot commit changes until you switch back to a branch.**  
   **Answer:** False. You can still commit changes in a detached HEAD state, but those commits may not be associated with any branch unless explicitly moved.

6. **Function arguments in Python are passed by reference, meaning that modifying a mutable object within a function will also modify it outside the function scope.**  
   **Answer:** True. 

7. **Using the `is` operator in Python checks for value equality, similar to the `==` operator.**  
   **Answer:** False. The `is` operator checks for object identity, not value equality.

8. **The `.gitignore` file in a Git repository is used to specify files that should not be tracked by Git and cannot be overridden by a user.**  
   **Answer:** False. The `.gitignore` rules can be overridden using explicit commands or settings like `git add -f`.

---

# Problem 2: Inverse vs. Forward Problems (6 points)
**Provide three examples of inverse and forward problems, and discuss their relative computational difficulty.**

1. **Example 1: Physics**
   - **Forward Problem:** Predicting the motion of a projectile given initial velocity and angle.  
   - **Inverse Problem:** Determining the initial velocity and angle from observed projectile motion.  
   - **Difficulty:** Inverse problems are generally harder due to noise and potential non-uniqueness in the data.

2. **Example 2: Imaging**
   - **Forward Problem:** Generating a 2D image projection from a 3D object model.  
   - **Inverse Problem:** Reconstructing a 3D object model from 2D image projections.  
   - **Difficulty:** Inverse problems are computationally more intensive due to the need for solving complex equations and dealing with incomplete data.

3. **Example 3: Machine Learning**
   - **Forward Problem:** Predicting output labels from input features using a trained model.  
   - **Inverse Problem:** Inferring the input features that might produce a specific output.  
   - **Difficulty:** Inverse problems often involve solving optimization tasks that are non-linear or ill-posed, making them significantly more challenging.
