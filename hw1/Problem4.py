import random

def monte_carlo_approximation(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    pi_approximation = 4 * (points_inside_circle / num_points)
    return pi_approximation

if __name__ == "__main__":
    num_points = int(input("Enter the number of random points to generate: "))
    pi_estimate = monte_carlo_pi_approximation(num_points)
    print(f"Approximated value of π using {num_points} points: {pi_estimate}")
