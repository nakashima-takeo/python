import math # to access math.cos and math.pi
from cosines_list import get_cos_list, get_x_list

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