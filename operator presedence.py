a = 12
b = 5
c = 3
d = 2
x = 7

result = (
    a + b * c ** d
    - x // d
    + (a % b) * c
)

check = (
    result > 50
    and a & b == 4
    or c << d > 10
)

final = (
    result if check
    else result + a ** 2 // (b + c)
)

print("Result:", result)
print("Check:", check)
print("Final:", final)