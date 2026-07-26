class Numbers:

    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width}cm"
    @property
    def height(self):
        return f"{self._height}cm"
