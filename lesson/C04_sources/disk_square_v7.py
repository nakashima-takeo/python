radius_m = 1.0
edge_m = 2.0

disk_area = 3.14 * radius_m**2
square_area = edge_m**2.0

while disk_area < square_area:
    radius_m = radius_m + 0.01
    disk_area = 3.14 * radius_m**2
    print("Disk radius = ", radius_m)

print("Disk area larger than square area")
print("Disk area = ", disk_area)

