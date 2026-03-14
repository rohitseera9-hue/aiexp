from collections import deque

def water_jug_problem(m, n, d):
    visited = set()
    queue = deque()

    # initial state (0,0)
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        # Check if we got the required amount
        if x == d or y == d:
            print("Steps to get", d, "liters:")
            for step in path:
                print(step)
            return

        # Possible operations
        next_states = [
            (m, y),  # Fill jug1
            (x, n),  # Fill jug2
            (0, y),  # Empty jug1
            (x, 0),  # Empty jug2
            (max(0, x - (n - y)), min(n, y + x)),  # Pour jug1 -> jug2
            (min(m, x + y), max(0, y - (m - x)))   # Pour jug2 -> jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution possible")

# Example
m = 4
n = 3
d = 2

water_jug_problem(m, n, d)