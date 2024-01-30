import argparse

__doc__ = " Parse arguments "

def parse_arguments():
    """
    Setting up the argpaser arguments for velocity , mass and friction.
    
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Calculating braking distance")

    # Add arguments for mass, velocity, and friction coefficient
    parser.add_argument('--mass', type=float, required=True, help='Mass of the vehicle (in kg)')
    parser.add_argument('--velocity', type=float, required=True, help='Vo of the vehicle (m/s)')
    parser.add_argument('--friction', type=float, required=True, help='Friction coefficient')

    # Parse the arguments and return them
    args = parser.parse_args()
    return args.mass, args.velocity, args.friction
