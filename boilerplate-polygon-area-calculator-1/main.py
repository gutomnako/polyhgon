from shape_calculator import Rectangle, Square

rect = Rectangle(10, 5)
rect.set_height(8)
rect.set_width(16)
print(rect)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())

sq = Square(9)
sq.set_side(5)
print(sq)
print(sq.get_area())
print(sq.get_perimeter())
print(sq.get_diagonal())
print(sq.get_picture())

print(rect.get_amount_inside(sq))
