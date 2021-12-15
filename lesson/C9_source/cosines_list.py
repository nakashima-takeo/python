import math # to access math.cos and math.pi


def get_x_list(start, end, step):
    """Returns a list from start to end with a step of 0.1
    """
    # Get the number of steps we need
    number_steps = int((end - start) / step) + 1

    # Fill the values in an empty list
    x_list = [] 
    for i in range(number_steps):
        x_list.append(start + i * step)
    return x_list

def get_cos_list(x_list):
    """Returns the list of cosines of a list of values"""
    return [math.cos(i) for i in x_list] # Use list comprehension

def main():
    # Call the functions with the test values
    x_list = get_x_list(0, 2.0 * math.pi, 0.1)
    cos_list = get_cos_list(x_list)

    # Display the values using zip to parse both lists together
    for i, c in zip(x_list, cos_list):
        #print("{} {}".format(i, c)) # gives "long" numbers
        print("{:.03} {:.03}".format(i, c)) # :.03 means keep 3 decimals after the dot
        # format has syntax to define the formating of the display
        # Full doc at https://docs.python.org/3/library/string.html
        # You can also use f-string in recent python 3

if __name__ == "__main__":
    main()