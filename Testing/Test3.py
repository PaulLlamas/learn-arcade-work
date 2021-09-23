def final_velocity_calculation(initial_velocity, acceleration, time):
    final_velocity = initial_velocity + (acceleration * time)
    return final_velocity


v2 = final_velocity_calculation(5, 1.3, 10)
print(v2)