__doc__ = " Calculate the stopping distance"
def calculate_stopping_distance(initial_velocity, deceleration):
    """
    Calculation of the stopping distance.

    Parameters:
    - initial_velocity (float): The initial velocity of the vehicle in meters per second.
    - deceleration (float): The constant deceleration in meters per second squared.

    """
    # The stopping distance can be found using the kinematic equation:
    # stopping_distance = (initial_velocity^2) / (2 * deceleration)
    stopping_distance = (initial_velocity ** 2) / (2 * deceleration)
    return stopping_distance
