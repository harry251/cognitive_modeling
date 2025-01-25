import matplotlib.pyplot as plt
from typing import Sequence, Tuple

def plot_results(
    infected: Sequence[float], 
    figsize: Tuple[int, int] = (10, 6),
    color: str = '#AA0000',
    linestyle: str = 'dashed',
    marker: str = 'o', 
    labelfontsize: int = 16,
    titlefontsize: int = 20,
    title: str = 'Simulated Oubreak'):
    """Plots the time series of infected cases."""
    
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.plot(infected, color=color, linestyle=linestyle, marker=marker)
    ax.set_xlabel('Day', fontsize=labelfontsize)
    ax.set_ylabel('Number of Infected Cases', fontsize=labelfontsize)
    ax.set_title(title, fontsize=titlefontsize)
    ax.grid(alpha=0.2)
    return fig
