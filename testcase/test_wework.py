from ..api.wework import WeWork
from ..api.util import Util
class TestWework:
    def test_get_token(self):
        print(Util().get_token())

    def test_create(self):
        print(WeWork().test_create("1122", "大da漂亮", "138023247199"))
        # aa=WeWork()
        # aa.test_create("111", "大漂亮", "13902324708")

    def test_update(self):
        print(WeWork().test_update("111", "可可爱"))

    def test_delete(self):
        WeWork().test_delete("1111")

