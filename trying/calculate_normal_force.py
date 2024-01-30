__doc__ = " Calculate the normal force"
def calculate_normal_force(mass):
    """

    Calculating the normal force (assuming flat surface, i.e., normal force = weight)

    """
    gravity = 9.81  # m/s^2, standard gravity
    normal_force = mass * gravity
    return normal_force
