numbers = [1,2,3,40.5,5]
a = numbers [0]
#print('numbers[0]', a)
#we can get item if we know the index
#numbers[1]= 'Soumyajit'
#print(numbers[1])
"""for x in range (0,5):
    print(numbers[x])"""
#print(numbers[:])

maximum = numbers[0]
for x in range(0,5):
    if maximum < numbers[x]:
        maximum = numbers[x]
print (maximum)