## *Convert a sentence into its equivalent mobile numeric keypad sequence *
x = input("")
y = x.lower()
num = ''
for i in y:
    if i in ' ':
        num += '0'
    if i in 'abc':
        num += '2' if i == 'a'  else '22' if i == 'b' else '222'
    if i in 'def':
        num += '3' if i == 'd'  else '33' if i == 'e' else '333'
    if i in 'ghi':
        num += '4' if i == 'g'  else '44' if i == 'h' else '444'
    if i in 'jkl':
        num += '5' if i == 'j'  else '55' if i == 'k' else '555'
    if i in 'mno':
        num += '6' if i == 'm'  else '66' if i == 'n' else '666'
    if i in 'pqrs':
        num += '7' if i == 'p'  else '77' if i == 'q' else '777' if i == 'r' else '7777'
    if i in 'tuv':
        num += '8' if i == 't'  else '88' if i == 'u' else '888'
    if i in 'wxyz':
        num += '9' if i == 'w'  else '99' if i == 'x' else '999' if i == 'y' else '9999'
    
print((num))
    

#solved
