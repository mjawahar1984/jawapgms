low = 1
up = 100
count = 0
print("Prime numbers between",low,"and",up,"are:")

for num in range(low,up + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
           count = count+1
print (count)
