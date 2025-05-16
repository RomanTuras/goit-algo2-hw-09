import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Обмеження
def clip(x, bounds):
    return [max(min(xi, bounds[i][1]), bounds[i][0]) for i, xi in enumerate(x)]


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.01):
    current = [random.uniform(*b) for b in bounds]
    current_val = func(current)

    for _ in range(iterations):
        neighbor = [xi + random.uniform(-step_size, step_size) for xi in current]
        neighbor = clip(neighbor, bounds)
        neighbor_val = func(neighbor)

        if abs(neighbor_val - current_val) < epsilon:
            break

        if neighbor_val < current_val:
            current, current_val = neighbor, neighbor_val

    return current, current_val


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1):
    current = [random.uniform(*b) for b in bounds]
    current_val = func(current)

    for _ in range(iterations):
        neighbor = [xi + random.uniform(-step_size, step_size) for xi in current]
        neighbor = clip(neighbor, bounds)
        neighbor_val = func(neighbor)

        if abs(neighbor_val - current_val) < epsilon:
            break

        if neighbor_val < current_val or random.random() < 0.1:
            current, current_val = neighbor, neighbor_val

    return current, current_val


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    current = [random.uniform(*b) for b in bounds]
    current_val = func(current)

    for _ in range(iterations):
        if temp < epsilon:
            break

        neighbor = [xi + random.uniform(-1, 1) for xi in current]
        neighbor = clip(neighbor, bounds)
        neighbor_val = func(neighbor)
        delta = neighbor_val - current_val

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_val = neighbor, neighbor_val

        temp *= cooling_rate

    return current, current_val


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
