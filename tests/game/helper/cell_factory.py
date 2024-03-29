from src.game.global_refs import CellType
from src.game.cell import Cell


class CellFactory:
    _map = {
        "b": CellType.blank,
        "f": CellType.food,
        "s": CellType.snake,
        "w": CellType.wall,
    }

    @staticmethod
    def _make_getter(cell: Cell):
        return lambda *args, **kwargs: cell

    @staticmethod
    def _make_list(pattern: str) -> list[Cell]:
        res: list[Cell] = []
        for i, char in enumerate(pattern):
            type = CellFactory._map[char]
            cell = Cell(None, None, type)
            res.append(cell)
        return res

    @staticmethod
    def _link(cells: list[Cell]) -> Cell:
        for i, cell in enumerate(cells[:-1]):
            next = cells[i + 1]
            cell.get_neighbour = CellFactory._make_getter(next)
        return cells[0]

    @staticmethod
    def make(pattern: str) -> (Cell, list[Cell]):
        cells = CellFactory._make_list(pattern)
        CellFactory._link(cells)
        return cells[0], cells

    @staticmethod
    def make_infinite_chain(type: CellType = CellType.blank) -> Cell:
        cell = Cell(type=type)
        cell.get_neighbour = lambda *args: CellFactory.make_infinite_chain(type)
        return cell
