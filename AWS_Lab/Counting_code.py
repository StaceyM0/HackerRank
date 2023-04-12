import boto3

fruits = ['apples','oranges','bananas']

for fruit in fruits:
    print(f'The best fruit now is {fruit}')
    
# this starts counting at 0
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(f'The next number is {number}')
    
# this starts counting at 1
for number in range(1,10):
    print(f'The next number is {number}')
    
# for only odd or even number counting
for number in range(1,10,2):
    print(f'The next number is {number}')
    