
n = 50
count = 0

for num in range(1, n + 1):
    
    if num % 3 == 0 and num % 5 == 0:
       count += 1

   
    

print("numbers divisible by 3 & 5 :", count)  