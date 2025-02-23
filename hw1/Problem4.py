import numpy as np

def monte_carlo_approximation(num_points: int) -> float:
    x, y = np.random.uniform(-1, 1, size=(2, num_points))
    points_inside_circle = np.sum(x**2 + y**2 <= 1)
    return 4 * (points_inside_circle / num_points)

if __name__ == "__main__":
    num_points = int(input("Enter the number of random points to generate: "))
    pi_estimate = monte_carlo_approximation(num_points)
    print(f"Approximated value of π using {num_points} points: {pi_estimate}")
