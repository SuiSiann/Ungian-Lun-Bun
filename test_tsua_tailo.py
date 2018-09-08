from unittest.case import TestCase
from lun5_bun5_thiah4_khui1 import _pehueji_tsua_tailo


class 轉台羅單元試驗(TestCase):
    def test_一般(self):
        lo = 'phah kah tshia-tuann'
        result = _pehueji_tsua_tailo(lo)
        self.assertEqual(result, lo)

    def test_雙括號(self):
        lo = '"phah" kah "tshia-tuann"'
        result = _pehueji_tsua_tailo(lo)
        self.assertEqual(result, lo)
