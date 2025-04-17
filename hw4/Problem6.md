## Problem 6: Project Pre-Study

**What problem are you considering?** 
This project investigates how well the Drift Diffusion Model (DDM) can recover its underlying cognitive parameters under varying levels of noise. Specifically, the focus is on understanding the robustness and reliability of Bayesian parameter recovery when both decision-making parameters and the stochastic noise component are allowed to vary. By simulating data with known ground truth and different noise conditions, we can evaluate whether the DDM is able to accurately infer parameters such as drift rate, boundary separation, and non-decision time. This can provide insight into the limits of model identifiability and sensitivity in noisy environments.

**What is the data y?**
The data consist of synthetic binary choices and reaction times (RTs) generated from the DDM. Each trial records which decision boundary was reached (choice) and how long it took to reach that boundary (RT). All data are generated in silico under known parameter settings, which allows for direct comparison between true parameters and inferred posteriors.

**What are the parameters θ?**
The parameters of interest include drift rate, boundary separation, non-decision time, and noise standard deviation. All four parameters are treated as free variables and are either systematically varied during simulation or estimated during Bayesian inference. The noise parameter σ is of particular interest in this study, as we aim to understand how increased stochasticity affects both observed behavior and the model’s ability to recover the generative parameters.

**What is the modeling task?**
The task is Bayesian parameter estimation and recovery analysis using simulated data. For a variety of noise levels and prior configurations, we will perform Bayesian inference to estimate the posterior distributions of the DDM parameters. The accuracy and stability of these estimates are then evaluated relative to the known ground truth used in the simulation. We will also conduct sensitivity analyses to understand how the choice of prior and the amount of noise influence inference quality.

**What existing models have been applied to tackle the problem?**
The DDM is a widely used cognitive process model for binary decision-making tasks. It has been employed extensively in psychology and neuroscience to model reaction time and accuracy patterns. Traditional approaches use either maximum likelihood estimation or Bayesian methods to estimate DDM parameters. However, many implementations assume a fixed noise level to resolve identifiability. In this project, we will explicitly treat σ as a variable in both simulation and inference to study its effects more directly.

**What model would be adequate in your case?**
We adopt the standard Drift Diffusion Model but extend it by allowing all core parameters — including noise — to vary. Bayesian inference is implemented in PyMC using the No-U-Turn Sampler (NUTS) for posterior estimation. This flexible model structure enables us to directly test how different noise levels affect parameter recovery, which is the central research question.

**How would you ensure computational faithfulness?**
We ensure convergence and computational validity by inspecting trace plots and evaluating effective sample sizes. The model implementation is vectorized for efficiency, and posterior predictive checks are used to validate the generative adequacy of the fitted model. We will also compare inference outcomes across varying noise levels to confirm the internal consistency of our conclusions.

**How would you criticize the model(s) in your intended project?**
While treating σ as a free parameter provides valuable insight into noise sensitivity, it reintroduces identifiability concerns. In classic DDM formulations, parameters like drift rate and noise interact multiplicatively, meaning that trade-offs between them can lead to ambiguity in parameter estimates. We will address this by carefully selecting prior distributions and validating inferences through simulation recovery. Nonetheless, estimating noise alongside other parameters may yield unstable posteriors, particularly when the data are limited. These limitations are inherent to the DDM and motivate future exploration of more constrained or hierarchical formulations.