sentence_1 = 'This is the first sentense'
sentence_2 = 'And, this is the second sentence'
sentence_3 = 'Finally, this is the third sentence'

# Get the lengths
len_1 =  len(sentence_1)
len_2 =  len(sentence_2)
len_3 =  len(sentence_3)

# Compare the lengths
if len_1 > len_2:
    if len_1 > len_3:
        if len_3 > len_2:
            print("132")
        else:
            print("123")
    else:
        print("312")
else:
    if len_1 > len_3:
        print("213")
    else:
        if len_3 > len_2:
            print("321")
        else:
            print("231")