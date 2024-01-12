import math

def generate_points_on_line(length, angle, num_points):
    points = []
    for i in range(num_points):
        x = i * length * math.cos(angle)
        y = i * length * math.sin(angle)
        points.append((round(x, 4), round(y, 4)))
    return points

# Example usage:
length = 1.0  # Replace with the desired distance between points
angle = math.radians(45)  # Replace with the desired angle in radians
num_points = 10  # Replace with the desired number of points

points = generate_points_on_line(length, angle, num_points)

for point in points:
    print(point)
