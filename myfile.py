def calculate_area(radius):
    return 3.14 * radius ** 2

radius = 5
area = calculate_area(radius)
print("The area of the circle is " + area)

if area > 50:
    print("Large circle")
else:
    print("Small circle")