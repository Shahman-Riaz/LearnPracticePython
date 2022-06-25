a = input('Enter first string: ')
b = input('Enter second string: ')

a1 = a.lower()
b1 = b.lower()

if(len(a1) == len(b1)):
    sorted_a1 = sorted(a1)
    sorted_b1 = sorted(b1)

    if(sorted_a1 == sorted_b1):
        print("YES")
    else:
        print("NO")
else:
    print('NO')
   