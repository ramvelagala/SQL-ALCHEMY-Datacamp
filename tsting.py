import math
x = 1234.5678

data1 = [1,-2,3.0,-4.0,-5.1,6.2,7.369,-8.356,4565242]
data =  [1,23,456,-7891]
import re
text = 'Python Exercises, PHP exercises.'
# for num in data:
#     a = str(num)
#     a.replace('^[0-9]', 'yes', 1)

for num in data1:
    num = str(num)
    b = ''
    for letter in num:
        if letter == '-':
            b = b+ '-'
        elif letter == '.':
            b = b+ '.'
        elif letter == ' ':
            pass
        else:
            a = (letter.replace(letter, '9', 1))
            b = b+a

    print(b) #final b

