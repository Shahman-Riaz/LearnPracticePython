x = input("")
num = ''
for i in x:
    if i in 'abc':
        num += '2'
    elif i in 'def':
        num += '3'
    elif i in 'ghi':
        num += '4'
    elif i in 'jkl':
        num += '5'
    elif i in 'mno':
        num += '6'
    elif i in 'pqrs':
        num += '7'
    elif i in 'tuv':
        num += '8'
    elif i in 'wxyz':
        num += '9'
print(int(num))
    
