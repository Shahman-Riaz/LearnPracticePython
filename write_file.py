with open("bear.txt", "r") as read_file:
    content1 = read_file.read()[0:90]

with open("first.txt", 'w') as write_file:
    content2 = write_file.write(content1)