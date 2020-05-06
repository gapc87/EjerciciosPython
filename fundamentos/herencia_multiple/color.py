class Color:
    def __init__(self, color):
        self.__color = color

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def __str__(self) -> str:
        return "Color: " + self.__color

