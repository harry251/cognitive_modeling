import matplotlib.pyplot as plt

def plot_results(infected, 
    figsize=(10, 6),
    color='#AA0000',
    linestyle='dashed',
    marker='o', 
    labelfontsize=16,
    titlefontsize=20,
    title='Simulated Oubreak'):
    """Plots the time series of infected cases."""
    
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.plot(infected, color=color, linestyle=linestyle, marker=marker)
    ax.set_xlabel('Day', fontsize=labelfontsize)
    ax.set_ylabel('Number of Infected Cases', fontsize=labelfontsize)
    ax.set_title(title, fontsize=titlefontsize)
    ax.grid(alpha=0.2)
    return fig
