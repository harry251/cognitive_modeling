import numpy as np
import pandas as pd
from typing import Tuple

def simulate_many(num_sim: int = 100_000) -> Tuple[pd.Series, pd.Series]:
    """
    Simulate the suspect and tool selection process for num_sim times.

    Parameters:
        num_sim (int): Number of simulations to run.
    
    Returns:
        Tuple[pd.Series, pd.Series]: Two Pandas Series containing the suspect and tool selections, respectively.
    """
    # Vectorized sampling of suspects
    suspects = np.random.choice(["Kevin", "Joe"], size=num_sim, p=[0.4, 0.6])
    
    # Prepare an array for tool selections
    observations = np.empty(num_sim, dtype=object)
    
    # Vectorized sampling for each suspect type
    observations[suspects == "Kevin"] = np.random.choice(
        ["stool", "tall_chair", "stepladder"],
        size=(suspects == "Kevin").sum(),
        p=[0.5, 0.4, 0.1]
    )
    observations[suspects == "Joe"] = np.random.choice(
        ["stool", "tall_chair", "stepladder"],
        size=(suspects == "Joe").sum(),
        p=[0.2, 0.5, 0.3]
    )
    
    return pd.Series(suspects, name="suspect"), pd.Series(observations, name="tool")

if __name__ == "__main__":
    num_sim = 30_000  
    suspects, observations = simulate_many(num_sim)
    
    # Build the joint probability table
    df = pd.crosstab(suspects, observations, normalize=True)
    
    # Remove default index/column names and reorder rows/columns
    df.index.name = None
    df.columns.name = None
    df = df.loc[["Kevin", "Joe"], ["stool", "tall_chair", "stepladder"]]
    
    print("Approximate Joint Probabilities (Suspect vs. Tool):\n")
    print(df.round(2))
