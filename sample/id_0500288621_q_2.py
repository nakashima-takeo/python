string_to_parse = "This is a test string"
find_character = "y"
while string_to_parse:
    if string_to_parse[0] == find_character:
        print("Found " + string_to_parse[0] + "!")
        break
    print(string_to_parse[0])
    string_to_parse = string_to_parse[1:]
    if string_to_parse == "":
        print("Did not find " + find_character + " in ‘This is a test string’")
