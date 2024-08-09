from src.ml.generation import Generation
from tests.test_ import Test_


class Generation_(Test_):

    def test_allows_previous_res_alone(self):
        stuff = Generation(id=0, previous_res={})

    def test_allows_ancestor_file_alone(self):
        stuff = Generation(id=0, has_ancestor_file=True)

    def test_rejects_simultaneous_previous_res_and_ancestor_file(self):
        self.assertRaises(
            ValueError,
            lambda: Generation(id=0, previous_res={}, has_ancestor_file=True),
        )
