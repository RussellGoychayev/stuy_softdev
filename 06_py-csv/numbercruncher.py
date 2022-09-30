'''
heading

qcc:
disco:
ops sum:
'''
import random

a = open("occupations.csv")
b = a.read()

dict = {}
txt = b.split("\n")
txt.pop()#remove last element: " "
txt.pop()#remove last element: "'Total': '99.8'"
txt.pop(0)#remove first element: "'Job Class': 'Percentage'"

for x in txt:
    list = x.rsplit(",", 1)
    dict[list[0]]= float(list[1])

list = []
for x in dict:
    for y in range(0, int(dict[x]*10)):
        list.append(x)

#print(random.choice(list))
'''
to test the weighted averages

dict2 same key as dict
[key] = 0
1000 times
[key] = value + 1
'''
