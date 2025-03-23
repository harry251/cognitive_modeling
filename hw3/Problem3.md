## Problem 3:

Given any prior and posterior:

$1. Var[\theta] \text{ - Prior variance.}$

$2. E[Var[\theta | y]] \text{ - Expected posterior variance.}$

$3. Var[E[\theta | y]] \text{ - Variance of posterior mean.}$

From the RHS, 

$$E[Var[\theta | y]] + Var [E[\theta | y]]$$

$$= E[E[\theta^2 | y]- E[\theta | y]^2] + E[(E[\theta | y]^2)] - E[E[\theta | y]]^2 \text{ using }Var[X] = E[X^2] - E[X]^2$$

$$= E[E[\theta^2 | y]] - E[E[\theta | y]^2] + E[(E[\theta | y]^2)] - E[E[\theta | y]]^2 \text{ using linearity of expectation}$$

$$= E[\theta^2] - E[E[\theta | y]^2] + E[E[\theta | y]^2] - E[\theta]^2\text{ using }E[X] = E[E[X | y]]$$

$$= E[\theta^2] + 0 - (E[\theta])^2$$

$$= E[\theta^2] - (E[\theta])^2$$

$$= Var[\theta] $$

Hence shown that the identity $Var[\theta] = E[Var[\theta | y]] + Var [E[\theta | y]]$ holds for any given prior and posterior.