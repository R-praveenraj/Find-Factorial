def factorial(number):
    result=1
    for i in range(1,number+1):
        result*=i
    return result

number=int(input())
print(factorial(number))