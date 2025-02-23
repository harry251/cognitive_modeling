# The Case of the Missing Cookie

## Setting
Mom baked a special, large cookie as a treat and warned her two sons—Kevin, the older brother, and Joe, the younger brother—not to eat it without permission. Kevin and Joe had already enjoyed their own cookies, and this last cookie was meant as a special treat for Dad. To keep the cookie safe, Mom placed the cookie jar on top of a tall cabinet in the kitchen, well out of their reach without using a tool.

## Suspects

- **Kevin (Older Brother)**
   - Has a reputation for bending rules, though he tries not to get caught.
   - Taller than Joe, so he might risk using a stool to reach the cabinet.
   - Moderately fond of sweets, but careful enough to leave little evidence behind.

- **Joe (Younger Brother)**
   - Loves cookies and is more impulsive.
   - Being shorter, he would most likely need a more stable tool like a tall chair or a stepladder.
   - Less meticulous, often leaving behind clues such as crumbs.

## Defining the Probabilities

### Prior Distribution
We begin by assigning a prior probability for each suspect based on their known tendencies:
- **Kevin:** $P(\text{Kevin}) = 0.4$
- **Joe:** $P(\text{Joe}) = 0.6$

### Likelihood (Tool Selection)
Given a suspect, we define the likelihood of using each tool to reach the high cabinet:

- **For Kevin:**  
   - **Stool:** $P(\text{stool} \mid \text{Kevin}) = 0.5$  
   *Justification:* Being taller, Kevin can often get by with the simpler stool.  
   - **Tall Chair:** $P(\text{tall\_chair} \mid \text{Kevin}) = 0.4$  
   *Justification:* If a stool seems too risky (e.g., due to potential traces), he might opt for the chair.  
   - **Stepladder:** $P(\text{stepladder} \mid \text{Kevin}) = 0.1$  
   *Justification:* Kevin is less inclined to go through the hassle of using and setting up a stepladder.

- **For Joe:**  
   - **Stool:** $P(\text{stool} \mid \text{Joe}) = 0.2$  
   *Justification:* The stool is less likely for Joe since his height makes it a poor option.  
   - **Tall Chair:** $P(\text{tall\_chair} \mid \text{Joe}) = 0.5$  
   *Justification:* Joe would prefer the tall chair as it is more stable and accessible.  
   - **Stepladder:** $P(\text{stepladder} \mid \text{Joe}) = 0.3$  
   *Justification:* In some cases, if the tall chair isn’t available or seems too conspicuous, Joe might use the stepladder.

### Analytic Joint Probabilities
By multiplying the prior with the tool likelihood for each suspect, we obtain the analytic joint probabilities:

- **Kevin:**  
   - $$P(\text{Kevin, stool}) = 0.4 \times 0.5 = 0.20$$  
   - $$P(\text{Kevin, tall\_chair}) = 0.4 \times 0.4 = 0.16$$  
   - $$P(\text{Kevin, stepladder}) = 0.4 \times 0.1 = 0.04$$

- **Joe:**  
   - $$P(\text{Joe, stool}) = 0.6 \times 0.2 = 0.12$$  
   - $$P(\text{Joe, tall\_chair}) = 0.6 \times 0.5 = 0.30$$  
   - $$P(\text{Joe, stepladder}) = 0.6 \times 0.3 = 0.18$$
