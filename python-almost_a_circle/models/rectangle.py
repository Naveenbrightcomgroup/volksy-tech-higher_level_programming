#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base.
    Args:
        Base: father class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor that sets the instance attributes.
        Args:
            width (int): width value.
            height (int): height value.
            x (int, 0): x value. Defaults to 0.
            y (int, 0): y value. Defaults to 0.
            id (int, None): id value. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter of the rectangle width.
        Returns:
            int: width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the rectangle width.
        Args:
            value (int): new width value.
        Raises:
            TypeError: <name of the attribute> must be an integer.
            ValueError: <name of the attribute> must be > 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    @property
    def height(self):
        """Getter of the rectangle height.
        Returns:
            int: height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the rectangle height.
        Args:
            value (int): new height value.
        Raises:
            TypeError: <name of the attribute> must be an integer.
            ValueError: <name of the attribute> must be > 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        """Getter of the rectangle x value.
        Returns:
            int: x value.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of the rectangle x value.
        Args:
            value (int): new x value.
        Raises:
            TypeError: <name of the attribute> must be an integer.
            ValueError: <name of the attribute> must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        elif value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    @property
    def y(self):
        """Getter of the rectangle y value.
        Returns:
            int: y value.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the rectangle y value.
        Args:
            value (int): new y value.
        Raises:
            TypeError: <name of the attribute> must be an integer.
            ValueError: <name of the attribute> must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        elif value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        """Claculate and return the rectangle area.
        Returns:
            int: rectangle area.
        """
        return self.__width * self.__height

    def display(self):
        """print in stdout the Rectangle instance with the
            character "#" by taking care of x and y.
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """Returns "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
        Returns:
            str: "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes.
        """
        l1 = ["id", "width", "height", "x", "y"]
        if args:
            for idx, val in enumerate(args):
                setattr(self, l1[idx], val)
        else:
            for key, val in kwargs.items():
                if key in l1:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle.
        Returns:
            dict: dictionary representation of a Rectangle.
        """
        new = {}
        for key, val in self.__dict__.items():
            new[key.split("_")[-1]] = val
        return new
