## Problem 3:

### 1. Show the following identity for the variance of a random variable $X$:

$$Var[X] = E[X^2] - E[X]^2.$$

---

By definition, $Var[X] = E\bigl[(X - E[X])^2\bigr].$

Expand the square inside the expectation:

$$E[(X - E[X])^2] = E[X^2 - 2X\,E[X] + E[X]^2].$$

Using the linearity of expectation, 

$$E[X^2 - 2X\,E[X] + E[X]^2] = E[X^2] - 2E[X]\,E[X] + E[X]^2$$

$$=E[X^2] - 2E[X]^2 + E[X]^2 = E[X^2] - E[X]^2.$$


Hence, we have shown that

$$\boxed{Var[X] = E[X^2] - E[X]^2.}$$

### 2. Show the following property for the variance of a random variable $X$ and a scalar $\alpha$:

$$Var[\alpha X + \beta] = a^2 \,Var[X]$$

---

Using defintion of variance,

$$\mathrm{Var}[\alpha X + \beta] 
= E[(\alpha X + \beta)^2] - [E[\alpha X + \beta]]^2$$

Expand the square inside the expectation,

$$\mathrm{Var}[\alpha X + \beta] = E[(\alpha^2 X^2 + 2\alpha\beta X + \beta^2)] - [\alpha E[X] + \beta]^2$$

$$= \alpha^2 E[X^2] + 2\alpha\beta E[X] + \beta^2 - [\alpha^2 E[X]^2 + 2\alpha\beta E[X] + \beta^2]$$

Simplify, 

$$\mathrm{Var}[\alpha X + \beta] = \alpha^2 E[X^2] + 2\alpha\beta E[X] + \beta^2 - \alpha^2 E[X]^2 - 2\alpha\beta E[X] - \beta^2$$

$$= \alpha^2 E[X^2] - \alpha^2 E(X)^2$$

$$= \alpha^2 [E[X^2] - E[X]^2]$$

$$= \alpha^2 Var[X]$$

Thus, we have shown:

$$\boxed{Var[\alpha X + \beta] = a^2 \,Var[X].}$$

### 3. Assume you are given a random variable $X$ with a standard normal distribution (mean zero, variance one). We can write this as

$$X \sim \mathcal{N}(\mu = 0,\sigma = 1).$$

One way to sample from this distribution is using NumPy’s function `numpy.random.randn()`. What transformation do you need to apply to the sampled values (i.e., the outputs of the function) such that they are now distributed according to

$$\tilde{X} \sim \mathcal{N}(\mu = 3, \sigma = 5)?$$

---

We want $\tilde{X}$ to have mean $3$. Hence, we set $a = 3$.   
Expected: $E[\tilde{X}] = E[3 + 5X] = 3 + 5E[X] = 3 + 5(0) = 3$

We want $\tilde{X}$ to have standard deviation $5$. Hence, we set $b = 5$.  
Variance: $Var[\tilde{X}] = Var[3 + 5X] = 5^2 Var[X] = 25$    
Standard deviation: $\sigma = \sqrt{25} = 5$

Therefore, the transformed variable is given by

$$\tilde{X} = 3 + 5X.$$

Since $X$ is standard normal, $\tilde{X}$ will be normally distributed with mean $3$ and standard deviation $5$.

If you have a sample `x` from `numpy.random.randn()`, you can transform it via:

```python
import numpy as np

# Transform it to have mean = 3 and std = 5
x_tilde = 3 + 5 * np.random.randn()
```