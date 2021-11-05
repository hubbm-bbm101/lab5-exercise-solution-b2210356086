print("This program calculates the sum of odd numbers, and the average of even numbers starting from 1 up to and including N")
N = int(input("Please Enter a Positive Integer N: "))
oddSum = 0
evenSum = 0
for i in range (1,N+1):
    if i % 2 == 0 :
        evenSum += i
    elif i % 2 != 0 :
        oddSum += i
evenAverage = evenSum / (N//2)
print("Sum of odd numbers is: "+ str(oddSum))
print("Average of even numbers is: "+ str(evenAverage))


