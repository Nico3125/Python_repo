def is_a_triangle(a, b, c): # In order to form a triangle, the sum of two sides has to be greater than the 3rd side
    return a + b > c and b + c > a and c + a > b

def is_a_triangle(a, b, c): #checks if 3 sides can form a triangle
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# In a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides 
def is_a_right_triangle(a, b, c): #checks if the triangle is right-angle triangle
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

