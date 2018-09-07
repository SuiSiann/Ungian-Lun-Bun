from unittest.case import TestCase
from lun5_bun5_thiah4_khui1 import han_hokbu_lineregex



class 拆開論文單元試驗(TestCase):
    def test判斷為三句(self):
        tsua = "楊允言，大漢技術學院、資訊工程系，助理教授。" 
        han_arr = han_hokbu_lineregex.findall(tsua)
        self.assertEqual(len(han_arr), 3, han_arr)

    def test上尾有兩个句號_判斷為兩句(self):
        tsua = "。。" 
        han_arr = han_hokbu_lineregex.findall(tsua)
        self.assertEqual(len(han_arr), 2, han_arr)

    def test句尾無句號_判斷為兩句(self):
        tsua = "附加詞類訊息ê台語語詞，搭配tī教學上ê應用" 
        han_arr = han_hokbu_lineregex.findall(tsua)
        self.assertEqual(len(han_arr), 2, han_arr)