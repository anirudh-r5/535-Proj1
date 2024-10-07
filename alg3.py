# Code Author: Anirudh Ramakrishnan (anirudh.r@csu.fullerton.edu)
def find_starting_city(distances, fuel, mpg):
    n = len(fuel)  # Number of cities
    current_fuel = 0  # To track fuel as we move through cities
    starting_city = 0  # Index of the potential starting city

    for i in range(n):
        fuel_gain = fuel[i] * mpg  # Gas from city i converted to miles we can travel
        fuel_required = distances[i]  # Miles required to travel to the next city
        current_fuel += fuel_gain - fuel_required  # Update the current fuel balance

        # If we run out of fuel, reset the starting point
        if current_fuel < 0:
            starting_city = i + 1  # Set the next city as the new potential starting point
            current_fuel = 0  # Reset the current fuel

    return starting_city  # Return the valid starting city

# Test data
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

print(find_starting_city(city_distances, fuel, mpg))
