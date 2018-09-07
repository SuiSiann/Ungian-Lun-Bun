import sys
import re
from requests.exceptions import RequestException
import requests
import json

# 論文輸入：lun5_bun5/ （無入git）
# 漢羅輸出：uan5_sing5/ （有上git）


# 輸入論文
論文名 = sys.argv[1]

with open(論文名, 'r') as lunbun:
    content = lunbun.readlines()

content = [x.strip() for x in content]


# 輸出論文每一句的漢羅對照
bracketregex = re.compile("\[")
han_lineregex = re.compile(".*?[，、。]")
lo_lineregex = re.compile(".*?[,.]")

for tsua in content:
    # 空白tsua
    if not tsua.strip():
        continue
    # 有漢羅對應的論文段落
    elif '[' in tsua and ']' in tsua:
        # get chapter
        try:
            han_ku, lo_ku = bracketregex.split(tsua)
        except ValueError:
            print('可能格式錯誤：{}\n\n'.format(tsua))
            continue

        # get lines preprocess
        han_ku = han_ku.strip('\n')
        lo_ku = lo_ku.rstrip(']')
        # get lines
        han_arr = han_lineregex.findall(han_ku)
        lo_arr = lo_lineregex.findall(lo_ku)

        if len(lo_arr) == len(han_arr):
            for han, lo in zip(han_arr, lo_arr):
                # 輸出每一句的漢羅
                print('{}\n[{}]'.format(han, lo.strip(' ')))
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
                # 提白話字
                lo_arr = to_guan_arr['多元書寫']
                # 拆漢字段落
                han_ku = han_lineregex.split(tsua)
                han_arr = han_lineregex.findall(han_ku)
                if len(lo_arr) == len(han_arr):
                    for han, lo in zip(han_arr, lo_arr):
                        # 輸出每一句的漢羅
                        print('{}\n[{}]'.format(han, lo['臺羅'].strip(' ')))
                    # 一段結束的換行
                    print()
                else:
                    print('對齊失敗：{}\n{}\n'.format(han_ku, lo_ku))
                # 輸出每一句的漢羅
                print('{}\n[{}]\n'.format(tsua, peh_ue_ji.strip(' ')))
            except ValueError:
                print('可能格式錯誤：{}\n\n'.format(tsua))
            except IndexError:
                # 無法度提著多元書寫
                print('tsua:{},,,{}'.format(tsua, to_guan_arr))
                break
        else:
            print('回傳狀態毋是200：{}', tsua)
