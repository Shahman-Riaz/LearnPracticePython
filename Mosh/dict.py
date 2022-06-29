x = int(input('Phone: '))
phone = {
    '1':'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output = ''
for ch in x:
    output += phone.get(ch, '!')
print(output)