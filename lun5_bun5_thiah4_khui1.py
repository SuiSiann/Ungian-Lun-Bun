import sys
import re
from requests.exceptions import RequestException
import requests
import json
from json.decoder import JSONDecodeError

# 論文輸入：lun5_bun5/ （無入git）
# 漢羅輸出：uan5_sing5/ （有上git）


# 輸入論文
論文名 = sys.argv[1]

with open(論文名, 'r') as lunbun:
    content = lunbun.readlines()

content = [x.strip() for x in content]


# 輸出論文每一句的漢羅對照
bracketregex = re.compile("\[") #論文逐段的對應羅馬字會用[]包起來 
han_lineregex = re.compile(".*?[，；、。：]") #粗判一段有幾句漢字
lo_lineregex = re.compile(".*?[,.;:]")  #粗判一段有幾句羅馬字
han_hokbu_lineregex = re.compile("([^，。]+[，。]?)|([^，。]*[，。])") #意傳工具袂共、拆開，所以另外寫這逝


def _pehueji_tsua_tailo(tsua):
    kiat_ko = None
    try:
        # 原始資料可能有雙括號，先換成別的
        tsua = tsua.replace('"', '#')
        r = requests.get('https://服務.意傳.台灣/羅馬字轉換', params={
            '查詢腔口': '閩南語',
            '查詢語句': tsua,
        })
    except RequestException as e:
        print(e)
        sys.exit(1)

    if r.status_code == requests.codes.ok:
        try:
            pkg_str = r.content.decode('unicode_escape')
            to_guan_arr = json.loads(pkg_str)
            # 把雙引號換回來
            kiat_ko = to_guan_arr['臺羅'].replace('#', '"')
        except JSONDecodeError as 錯誤:
             print(pkg_str)
             sys.exit(1)
    else:
        print('轉台羅狀態毋是200：{}', tsua)

    return kiat_ko


def _sui2():
    for tsua in content:
        # 空白tsua
        if not tsua.strip():
            continue
        # 有漢羅對應的論文段落
        elif '[' in tsua and ']' in tsua:
            # get chapter
            try:
                han_ku, pehueji_ku = bracketregex.split(tsua)
            except ValueError:
                print('可能格式錯誤：{}\n\n'.format(tsua))
                continue
    
            # get lines preprocess
            han_ku = han_ku.strip('\n')
            pehueji_ku = pehueji_ku.rstrip(']')
            # POJ轉做台羅
            lo_ku = _pehueji_tsua_tailo(pehueji_ku)
            # get lines
            han_arr = han_lineregex.findall(han_ku)
            lo_arr = lo_lineregex.findall(lo_ku)
    
            if len(lo_arr) == len(han_arr):
                # 輸出每一句的漢羅
                for han, lo in zip(han_arr, lo_arr):
                    print('{}\n{}'.format(han, lo.strip(' ')))
                # 一段結束的換行
                print()
            else:
                print('對齊失敗：{}\n{}\n'.format(han_ku, lo_ku))
        # 只有漢字的論文段落
        else:
            # 補段落的羅馬字
            try:
                r = requests.get('https://服務.意傳.台灣/標漢字音標', params={
                    '查詢腔口': '閩南語',
                    '查詢語句': tsua,
                })
            except RequestException as e:
                print(e)
                sys.exit(1)
    
            if r.status_code == requests.codes.ok:
                pkg_str = r.content.decode('unicode_escape')
                to_guan_arr = json.loads(pkg_str)
                try:
                    # 提多元書寫的臺羅
                    lo_arr = to_guan_arr['多元書寫']
                    # 拆漢字段落
                    han_arr = han_hokbu_lineregex.findall(tsua)
                    if len(lo_arr) == len(han_arr):
                        # 輸出每一句的漢羅
                        for han, lo in zip(han_arr, lo_arr):
                            print('{}\n鬥拍字：{}'.format(''.join(han), lo['臺羅'].strip(' ')))
                        # 一段結束的換行
                        print()
                    else:
                        print('補羅馬字但是對齊失敗：{}\n{}\n'.format(tsua, str(lo_arr)))
                    
                except ValueError:
                    print('可能格式錯誤：{}\n\n'.format(tsua))
                except IndexError:
                    # 無法度提著多元書寫
                    print('tsua:{},,,{}'.format(tsua, to_guan_arr))
                    break
            else:
                print('回傳狀態毋是200：{}', tsua)


if __name__ == '__main__':
    _sui2()