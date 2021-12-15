def function_1(v1, v2):
    return v1 + v2

def function_2(v1, v2):
    return v1 + v2, v1 * v2 # This syntax will be clarified later

def function_3(v1, v2):
    return

def function_4(v1, v2):
    if v1 > v2:
        print("v1>v2")
    else:
        print("v1<=v2")

r1 = function_1(1.0, 3.0)      
r2 = function_2(1.0, 3.0)      
r3 = function_3(1.0, 3.0)      # Some IDEs may complains
r4 = function_3(1.0, 3.0)      # Some IDEs may complains

# Add some statements to check the return values
