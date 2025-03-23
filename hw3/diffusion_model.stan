data {
    int<lower=1> N;
    array[N] real<lower=0> y;
    array[N] int<lower=1, upper=2> condition;
    array[N] int<lower=0, upper=1> choice;
}

parameters {
    array[2] real v;
    real<lower=0> a;
    real<lower=0, upper=1> b;
    real<lower=0> tau;
}

model {
    // Priors
    v ~ normal(0, 2);
    a ~ normal(1, 1);
    b ~ beta(1, 1);
    tau ~ normal(0.3, 0.2);

    // Likelihood
    for (n in 1:N) {
        // Condition 1
        if (condition[n] == 1) {
            if (choice[n] == 1) {
                y[n] ~ wiener(a, tau, b, v[1]);
            }
            else {
                y[n] ~ wiener(a, tau, 1 - b, -v[1]);
            }
        }
        // Condition 2
        if (condition[n] == 2) {
            if (choice[n] == 1) {
                y[n] ~ wiener(a, tau, b, v[2]);
            }
            else {
                y[n] ~ wiener(a, tau, 1 - b, -v[2]);
            }
        }
    }
}