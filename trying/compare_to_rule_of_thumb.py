__doc__ = " compare to rule of thumb "
def compare_to_rule_of_thumb(velocity, stopping_distance):
    """
    Parameters:

    Comapring the rule of thumb to the simulated stopping distance.

    - velocity : The initial velocity of the vehicle in meters per second.
    - stopping_distance : The simulated stopping distance in meters.

    """
    # Rule of thumb calculations
    s_normal = (velocity / 10) ** 2
    s_danger = ((velocity / 10) ** 2) * 0.5
    s_reaction = (velocity / 10) * 3

    # Total stopping distance according to rule of thumb
    s_stop = s_normal + s_reaction
    s_stop_danger = s_danger + s_reaction

    # Comparison result
    comparison = {
        's_normal': s_normal,
        's_danger': s_danger,
        's_reaction': s_reaction,
        's_stop': s_stop,
        's_stop_danger': s_stop_danger,
        'simulated_stopping_distance': stopping_distance,
        'within_normal_limits': stopping_distance <= s_stop,
        'within_danger_limits': stopping_distance <= s_stop_danger
    }

    return comparison
