import tensorflow as tf
from src.ml.eye_fake import EyeFake
from src.ml.view import View
from tests.ml.eye_ import Eye_


class Eye_fake_see_(Eye_):
    def test_see_gets_tensor(self):
        view = View()
        sut = EyeFake(view)
        game = self.make_game()
        head = game.get_head()
        food = game._grid.get_random_blanks(1)[0]
        actual = sut.see(head, food)
        self.assertIsInstance(actual, tf.Tensor)

    def test_see_gets_the_right_shape(self):
        view = View(True, False, True, False, True)
        sut = EyeFake(view)
        game = self.make_game()
        head = game.get_head()
        food = game._grid.get_random_blanks(1)[0]
        actual = sut.see(head, food).shape
        self.assertEqual(actual, [view.size])
