import os
import matplotlib.pyplot as plt

__doc__ = " Generate plots "

def generate_plots(time_data, velocity_data, distance_data):
    """
    Generating the graphs.
    
    Parameters:
    - time_data : time values list.
    - velocity_data : velocity values list corresponding to the time values.
    - distance_data : distance values list corresponding to the time values.

    """
    # Plot Velocity vs Time
    plt.figure(figsize=(10, 5))
    plt.plot(time_data, velocity_data, label='Velocity (m/s)', color='red')
    plt.title('Velocity vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    plt.grid(True)
    current_directory = os.getcwd()  # Gets the current working directory
    plt.savefig(os.path.join(current_directory, 'velocity_vs_time.png'))
    plt.show()

    # Plot Distance vs Time
    plt.figure(figsize=(10, 5))
    plt.plot(time_data, distance_data, label='Distance (m)', color='green')
    plt.title('Distance vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (m)')
    plt.legend()
    plt.grid(True)
    current_directory = os.getcwd()  # Gets the current working directory
    plt.savefig(os.path.join(current_directory, 'Distance_vs_time.png'))
    plt.show()
