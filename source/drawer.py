from source.cell import Cell
from source.global_refs import CellType
from source.graphics import GraphWin, Point, Rectangle


class Drawer:
    _window: GraphWin
    _cell_size: int
    _colour_map = {
        CellType.wall: "red",
        CellType.blank: "black",
        CellType.snake: "lime",
        CellType.food: "yellow",
    }

    def __init__(self):
        self._window = GraphWin("snakePy", 1500, 600)
        self._cell_size = 14
        pass

    def draw(self, cells: list[Cell]) -> None:
        for cell in cells:
            ri = cell._row
            ci = cell._col

            hor_offset = ri * self._cell_size
            ver_offset = ci * self._cell_size

            left = hor_offset
            right = left + self._cell_size
            top = ver_offset
            bottom = top + self._cell_size

            point1 = Point(top, left)
            point2 = Point(bottom, right)

            square = Rectangle(point1, point2)
            cellType = cell.get_type()
            colour = self._colour_map[cellType]
            square.setFill(colour)
            square.draw(self._window)

    def getMouse(self):
        return self._window.getMouse()
