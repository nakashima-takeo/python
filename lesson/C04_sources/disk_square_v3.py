import math
radius_m = 1.11
edge_m = 2.0

disk_area = 3.14 * radius_m**2

square_area = edge_m**2.0

if disk_area > square_area:
    print("Disk area larger than square area")
    print("Disk area = ", disk_area)

if disk_area < square_area:
    print("Square area larger than disk area")
    print("Square area = ", square_area)

