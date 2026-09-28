# squaring of the number

def square(a):
    return a**2

result=square(5)

print(result)

# calculating the area

def calculate_area(a,b):
    return a*b

result=calculate_area(10,6)
print(result)

# to find even or not

def iseven(a):
    return a%2==0

result=iseven(5)
print(result)

# to check the largest

def is_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
result=is_max(10,20,30)
print(result)

# calculate percentage

def calculate_percentage(obtained,total):
    return (obtained/total)*100

result=calculate_percentage(75,100)
print(result)