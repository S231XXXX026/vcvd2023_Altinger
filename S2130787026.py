__doc__ = "Main script for vehicle braking simulation."

# Standard library imports
#import argparse
import sys

# Import methods from their respective modules
from trying.parse_arguments import parse_arguments
from trying.calculate_normal_force import calculate_normal_force
from trying.calculate_friction_force import calculate_friction_force
from trying.calculate_deceleration import calculate_deceleration
from trying.simulate_braking import simulate_braking
from trying.calculate_stopping_distance import calculate_stopping_distance
from trying.generate_plots import generate_plots
from trying.compare_to_rule_of_thumb import compare_to_rule_of_thumb


def main():
    """
    
    Runs the code going through each method to get an output for the vehicle breaking.

    """
    # Parse command-line arguments
    mass, velocity, friction = parse_arguments()
    # Calculate the normal force (assuming flat surface, i.e., normal force = weight)
    normal_force = calculate_normal_force(mass)

    # Calculate the friction force
    friction_force = calculate_friction_force(friction, normal_force)

    # Calculate deceleration
    deceleration = calculate_deceleration(friction_force, mass)

    # Simulate braking
    braking_data = simulate_braking(velocity, deceleration)

    # Calculate stopping distance
    stopping_distance = calculate_stopping_distance(velocity, deceleration)

    # Compare the simulated stopping distance to the rule of thumb
    comparison = compare_to_rule_of_thumb(velocity, stopping_distance)

    # Generate plots
    time_data = [point[0] for point in braking_data]
    velocity_data = [point[1] for point in braking_data]
    distance_data = [point[2] for point in braking_data]
    generate_plots(time_data, velocity_data, distance_data)


    # Print the comparison for visualization in the console
    for key, value in comparison.items():
        print(f"{key}: {value}")

# Check if this is the main module being executed
if __name__ == "__main__":
    main()
    sys.exit()
