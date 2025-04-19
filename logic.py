from itertools import permutations

# Product availability at centers
centers = {
    'C1': {'A', 'B', 'C'},
    'C2': {'D', 'E', 'F'},
    'C3': {'G', 'H', 'I'}
}

# Distance in km between centers and L1
distances = {
    ('C1', 'L1'): 10,
    ('C2', 'L1'): 20,
    ('C3', 'L1'): 30,
    ('C1', 'C2'): 10,
    ('C1', 'C3'): 15,
    ('C2', 'C3'): 5,
    ('C2', 'C1'): 10,
    ('C3', 'C1'): 15,
    ('C3', 'C2'): 5,
    ('L1', 'C1'): 10,
    ('L1', 'C2'): 20,
    ('L1', 'C3'): 30
}

cost_per_km = 1.0  # cost for 0.5kg per km

def find_center(product):
    for center, products in centers.items():
        if product in products:
            return center
    raise ValueError(f"Product {product} not found in any center")

def calculate_cost(route):
    total_cost = 0
    current_location = route[0]
    for next_location in route[1:]:
        distance = distances.get((current_location, next_location), None)
        if distance is None:
            return float('inf')  # Return infinity if distance is missing
        total_cost += distance * cost_per_km
        current_location = next_location
    return total_cost

def compute_min_cost(order):
    centers_needed = set(find_center(prod) for prod in order if order[prod] > 0)
    min_cost = float('inf')

    for start_center in centers_needed:
        possible_routes = permutations(centers_needed - {start_center})
        for route in possible_routes:
            full_route = [start_center]
            for center in route:
                full_route += ['L1', center]
            full_route += ['L1']
            cost = calculate_cost(full_route)
            if cost < min_cost:
                min_cost = cost

    return min_cost
