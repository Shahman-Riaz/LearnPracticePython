operations = ["--X","X++","X++"]
x = 0
for i in operations:
    if i == '++X' or i == 'X++':
        x += 1
    elif i == '--X' or i == 'X--':
        x -=1
print(x)

#SOLVED
