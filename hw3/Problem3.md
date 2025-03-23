## Problem 3:

From the RHS, 

$$E[Var[\theta | y]] + Var [E[\theta | y]]$$

$$= E[E[\theta^2 | y]- E[\theta | y]^2] + E[(E[\theta | y]^2)] - E[E[\theta | y]]^2 \text{ using }Var[X] = E[X^2] - E[X]^2$$

$$= E[E[\theta^2 | y]] - E[E[\theta | y]^2] + E[(E[\theta | y]^2)] - E[E[\theta | y]]^2 \text{ using linearity of expectation}$$

$$= E[\theta^2] - E[E[\theta | y]^2] + E[E[\theta | y]^2] - E[\theta]^2\text{ using }E[X] = E[E[X | y]]$$

$$= E[\theta^2] + 0 - (E[\theta])^2$$

$$= E[\theta^2] - (E[\theta])^2$$

$$= Var[\theta] $$

Hence shown that $Var[\theta] = E[Var[\theta | y]] + Var [E[\theta | y]]$.