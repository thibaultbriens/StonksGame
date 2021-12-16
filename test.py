list = [1, 3, 5, 7, 9, 11, 13 , 1, 3, 5, 7, 9, 11, 13 , 1, 3, 5, 7, 9, 11, 13 , 1, 3, 5, 7, 9, 11, 13]

'''textfile = open("test.txt", "w")
for element in list:
    textfile.write(str(element) + "\n")
textfile.close()'''

places = []
f = open('test.txt', 'r')

for prix in f:
    # remove linebreak which is the last character of the string
    currentPlace = prix[:-1]
    # add item to the list
    places.append(currentPlace)
    print(currentPlace)

print(places)

