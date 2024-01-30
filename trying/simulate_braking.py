__doc__ = " Simulating braking "
def simulate_braking(initial_velocity, deceleration):
    """
    Simulation and gathering data for the time , velocity and distance

    Parameters:
    - time_step (float): The time increment for the simulation, in seconds.
    - initial_velocity (float): The initial velocity of the vehicle in meters per second.
    - deceleration (float): The constant deceleration in meters per second squared.
    """
    time = 0
    time_step = 0.1
    velocity = initial_velocity
    distance = 0
    braking_data = []

    while velocity > 0:
        braking_data.append((time, velocity, distance))
        distance += velocity * time_step + (0.5 * (-deceleration)) * (time_step ** 2)
        velocity += (-deceleration) * time_step  # velocity will decrease due to deceleration
        time += time_step

#ensures velocity != 0
        velocity = max(velocity, 0)

    return braking_data
