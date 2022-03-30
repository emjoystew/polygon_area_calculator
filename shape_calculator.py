class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width
        return self.width

    def set_height(self, new_height):
        self.height = new_height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            picture += ("*" * self.width) + "\n"
        return picture

    def get_amount_inside(self, other_shape):
        return (self.width // other_shape.width) * (self.height // other_shape.height)

class Square(Rectangle):

    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def __repr__(self):
        return f"{type(self).__name__}(side={self.height})"

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side
        return self.height, self.width

    def set_width(self, new_side):
        self.set_side(new_side)

    def set_height(self, new_side):
        self.set_side(new_side)