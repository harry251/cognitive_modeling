import matplotlib.pyplot as plt

from simulation import simulate_seir
from viz import plot_results


if __name__ == "__main__":


    parameters = (3, 0.5, 0.5)

    # S0, E0, I0, R0
    inits = (9999., 1., 0., 0.)

    ### Your code here
    sim = simulate_seir(parameters, inits, 100)

    ### Expected result
    f = plot_results(sim[2])
    plt.show()
