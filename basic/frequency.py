num = input("Enter Number:")
list = [num[i] for i in range(len(num))]
frequency = {}

for i in list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Number : Frequency")    
for key, value in frequency.items():
    print(f"{key} : {value}")


