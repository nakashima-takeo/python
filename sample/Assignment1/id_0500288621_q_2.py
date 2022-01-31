string_to_parse = "This is a test string"
# It should be possible to easily modify the script to stop for a different letter than r.
find_character = "r"
while string_to_parse:
    if string_to_parse[0] == find_character:
        print("Found " + string_to_parse[0] + "!")
        break
    print(string_to_parse[0])
    # Remove the first character from the string.
    string_to_parse = string_to_parse[1:]
    # If the selected letter is not found in the string, the script should display a message.
    if string_to_parse == "":
        print("Did not find " + find_character + " in ‘This is a test string’")
