__doc__ = " Calculate deceleration "
def calculate_deceleration(friction_force,mass):
    """
    Calculation of the deceleration of the vehicle due to friction.

    Parameters:
    - friction_coefficient : The coefficient of friction.
    - mass : The mass of the vehicle in kilograms.

    """
    deceleration = friction_force / mass
    return deceleration
