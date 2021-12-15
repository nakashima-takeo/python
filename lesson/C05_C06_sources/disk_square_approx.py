import math

def compute_disk_area(radius):
    """Returns the area of a disk given the radius"""
    return math.pi * radius ** 2.0

def compute_square_area(edge):
    """Returns the area of a square given the edge"""
    return edge**2.0

def get_initial_interval(edge):
    """Returns:
    the radius of the inscribed circle 
    the radius of the circumscribed circle
    given the edge of a square"""
    return edge / 2.0, edge / math.sqrt(2.0)

def main(edge, tolerance = 0.1, max_iter = 100):
    """Search for the radius of the disk with same area as the square of a given edge.
    The search stops when the areas are close enough 
    or the maximum number of iterations is reached.

    Arguments:
        edge : the edge of the square
        tolerance : how close the areas should be.
        max_iter : the maximal number of iterations to perform
    """
   

    # Get an initial interval and radius
    radius_lower, radius_upper = get_initial_interval(edge)
    radius = 0.5 * (radius_upper + radius_lower)

    # Get the areas and error
    square_area = compute_square_area(edge)
    disk_area = compute_disk_area(radius)
    area_error = disk_area - square_area

    # Start the computation loop    
    number_iter = 0
    while abs(area_error) > tolerance and number_iter < max_iter:
        # Use the error to update the interval
        if area_error > 0.0 :
            # Disk larger
            # set upper value
            radius_upper = radius
        else:
            # square larger
            # set lower value
            radius_lower = radius            

        # Update the radius, the area and the error
        radius = 0.5 * (radius_upper + radius_lower)
        disk_area = compute_disk_area(radius)
        area_error = disk_area - square_area

        # Update the iteration counter        
        number_iter += 1

    # show the results:
    print("Square area:", square_area)
    print("Disk area:", disk_area)
    print("Radius:", radius)
    print("Number iterations:", number_iter)


if __name__ == "__main__":

     # Ask for the edge of the square
    edge = float(input("Enter square edge: "))

    main(edge, max_iter=10)
