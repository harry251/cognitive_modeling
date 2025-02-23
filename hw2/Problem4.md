## Problem 4:

We define:
$$P(T) = \frac{1}{3} \quad \text{(first tells truth)}$$

$$P(L) = \frac{2}{3} \quad \text{(first lies)}$$

$$P(Y|T) = \frac{1}{3} \quad \text{(second says yes when first tells truth)}$$

$$P(Y|L) = \frac{2}{3} \quad \text{(second says yes when first lies)}$$

We want to find $P(T|Y)$:

Using Bayes' Theorem:

$$P(T|Y) = \frac{P(Y|T) P(T)}{P(Y)}$$

Computing $P(Y)$:

$$P(Y) = P(Y|T) P(T) + P(Y|L) P(L)$$

$$= \frac{1}{3} \times \frac{1}{3} + \frac{2}{3} \times \frac{2}{3}$$

$$= \frac{1}{9} + \frac{4}{9}$$

$$= \frac{5}{9}$$

Now, solving for $P(T|Y)$:

$$P(T|Y) = \frac{\frac{1}{3} \times \frac{1}{3}}{\frac{5}{9}}$$

$$= \frac{1}{9} \div \frac{5}{9}$$

$$= 0.2$$

Thus, $P(T|Y) = $ 20\%.

There is only a **20%** chance the original statement indeed true. 