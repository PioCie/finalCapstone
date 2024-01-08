with open('DOB.txt', 'r+') as file:
    content = file.readlines()
    for i in range(len(content)):
        print(type(i))

