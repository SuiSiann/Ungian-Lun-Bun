from unittest.case import TestCase
from lun5_bun5_thiah4_khui1 import han_hokbu_lineregex, han_lineregex,\
    lo_lineregex



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
        
    def test_ah(self):
        han = "根據語料庫，beh kā共同出現而且互相關係密切ê語詞chhē出來，是利用統計ê方法。有兩個公式會sái做，第一個是互訊息(mutual information, 以下簡稱MI)，設使A、B是語詞，這兩個語詞ê MI ê公式是："
        han_arr = han_lineregex.findall(han)
        self.assertEqual(len(han_arr), 8, han_arr)
    
    def test_al(self):
        lo = "Kun-kù gú-liāu-khò͘ , beh kā kiōng-tông chhut-hiān jî-chhiáⁿ hō͘-siong koan-hē bi̍t-chhiat ê gú-sû chhē--chhut-lâi, sī lī-iōng thóng-kè ê hong-hoat. Ū nn̄g-ê kong-sek ē-sái chòe, tē-it-ê sī hō͘-sìn-sit (mutual information, í-hā kán-chheng MI ), siat-sú A, B sī gú-sû, chit nn̄g-ê gú-sû ê MI ê kong-sek sī :"
        lo_arr = lo_lineregex.findall(lo)
        self.assertEqual(len(lo_arr), 8, lo_arr)
        
    def test_bh(self):
        han = "簡單講，beh算CR (AB)，tō kā語料內底ê詞組分做 AB、A~B、~AB、~A~B四部分，透過頂面ê公式來計算。算出來ê數字lóng是正數，AB兩個語詞若tiāⁿ-tiāⁿ做陣出現，CR (AB)可能超過10,000，甚至超過100,000。"
        han_arr = han_lineregex.findall(han)
        self.assertEqual(len(han_arr), 8, han_arr)
    
    def test_bl(self):
        lo = " Kán-tan kóng, beh sǹg CR (AB), tō kā gú-liāu lāi-tóe ê sû-cho͘ hun-chòe AB, A~B, ~AB, ~A~B sì pō͘-hūn, thàu-kè téng-bīn ê kong-sek lai kè-sǹg. Sǹg--chhut-lâi ê sò͘-jī lóng-sī chiàⁿ-sò͘, AB nnḡ-ê gú-sû nā tiāⁿ-tiāⁿ chòe-tīn chhut-hiān, CR(AB) khó-lêng chhiau-kè 10,000.0 , sīm-chì chhiau-kè 100,000.0 ."
        lo_arr = lo_lineregex.findall(lo)
        self.assertEqual(len(lo_arr), 8, lo_arr)
    

