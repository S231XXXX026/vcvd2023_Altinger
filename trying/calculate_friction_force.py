__doc__ = " Calculate the friction force"
def calculate_friction_force(friction, normal_force):
    """
    Calculation of the friction force based on the coefficient of friction and the normal force.

    Parameters:
    - Friction : The coefficient of friction.
    - normal_force : The normal force, which is mass * gravity for flat surfaces.

    """
    friction_force = friction * normal_force
    return friction_force
