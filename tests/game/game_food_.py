from src.game.global_refs import CellType
from src.game.game import Game
from tests.game.game_ import Game_


class Game_etc_(Game_):
    def test_add_food_without_args_affects_one_cell(self):
        self.sut._give_food()
        expected = self.sut._init_food_count + 1
        self.assertCellCount(self.sut._grid, CellType.food, expected)

    def test_add_food_with_specific_number_adds_correct_amount(self):
        self.sut._give_food(self.few)
        expected = self.few + self.sut._init_food_count
        self.assertCellCount(self.sut._grid, CellType.food, expected)

    def test_initiates_correct_number_of_foods(self):
        expected = self.few
        sut = Game(self.some, init_food_count=expected)
        self.assertCellCount(sut._grid, CellType.food, expected)
