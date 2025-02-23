## Problem 3:

### 1. Show the following identity for the variance of a random variable $X$:
$$
\operatorname{Var}[X] = E[X^2] - E[X]^2.
$$
---

By definition, $\operatorname{Var}[X] = E\bigl[(X - E[X])^2\bigr].$

Expand the square inside the expectation:
$$
E[(X - E[X])^2] = E[X^2 - 2X\,E[X] + E[X]^2].
$$

Using the linearity of expectation, 
$$
E[X^2 - 2X\,E[X] + E[X]^2] = E[X^2] - 2E[X]\,E[X] + E[X]^2
$$

$$
=E[X^2] - 2E[X]^2 + E[X]^2 = E[X^2] - E[X]^2.
$$


Hence, we have shown that

$$
\boxed{
\operatorname{Var}[X] = E[X^2] - E[X]^2.
}
$$

### 2. Show the following property for the variance of a random variable $X$ and a scalar $\alpha$:

$$
\mathrm{Var}[\alpha X + \beta\,] = \alpha^2 \,\mathrm{Var}[X].
$$
---

Using defintion of variance,
$$
\mathrm{Var}[\alpha X + \beta] 
= E[(\alpha X + \beta)^2] - [E[\alpha X + \beta]]^2
$$

Expand the square inside the expectation,

$$
\mathrm{Var}[\alpha X + \beta] = E[(\alpha^2 X^2 + 2\alpha\beta X + \beta^2)] - [\alpha E[X] + \beta]^2
$$

$$
= \alpha^2 E[X^2] + 2\alpha\beta E[X] + \beta^2 - [\alpha^2 E[X]^2 + 2\alpha\beta E[X] + \beta^2]
$$

Simplify, 

$$
\mathrm{Var}[\alpha X + \beta] = \alpha^2 E[X^2] + 2\alpha\beta E[X] + \beta^2 - \alpha^2 E[X]^2 - 2\alpha\beta E[X] - \beta^2
$$

$$
= \alpha^2 E[X^2] - \alpha^2 E(X)^2 
$$

$$
= \alpha^2 [E[X^2] - E[X]^2]
$$

$$
= \alpha^2 Var[X]
$$

Thus, we have shown:

$$
\boxed{\mathrm{Var}[\,aX + b\,] = a^2 \,\mathrm{Var}[X].}
$$

### 3. Assume you are given a random variable $X$ with a standard normal distribution (mean zero, variance one). We can write this as
$$
X \sim \mathcal{N}(\mu = 0,\sigma = 1).
$$
One way to sample from this distribution is using NumPy’s function `numpy.random.randn().` What transformation do you need to apply to the sampled values (i.e., the outputs of the function) such that they are now distributed according to
$$
\tilde{X} \sim \mathcal{N}(\mu = 3, \sigma = 5)?
$$
---
