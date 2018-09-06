import sys
import re
from requests.exceptions import RequestException
import requests
import json



論文名 = sys.argv[1]

with open(論文名, 'r') as lunbun:
    content = lunbun.readlines()

content = [x.strip() for x in content]



# 將文章照漢字台羅對應

bracketregex = re.compile("\[")
han_lineregex = re.compile(".*?[，、。]")
lo_lineregex = re.compile(".*?[,.]")

for tsua in content:
    if not tsua.strip():
        continue
    # 才是漢羅對應文章
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
            for a,b in zip(han_arr, lo_arr):
                print('{}\n[{}]\n\n'.format(a,b.strip(' ')))
        else:
            print('對齊失敗：{}\n{}\n'.format(han_ku, lo_ku))

    else:
        # 補羅馬字
        try:
            r = requests.get('https://服務.意傳.台灣/標漢字音標', params={
                '查詢腔口': '閩南語',
                '查詢語句': tsua,
            })
        except RequestException as e:  # This is the correct syntax
            print(e)
            sys.exit(1)
        
        if r.status_code == requests.codes.ok:
            pkg_str = r.content.decode('unicode_escape')
            to_guan_arr = json.loads(pkg_str)
            try:
                peh_ue_ji = to_guan_arr['多元書寫'][0]['白話字'] 
                print('{}\n[{}]\n\n'.format(tsua, peh_ue_ji.strip(' ')))
            except IndexError:
                print('tsua:{},,,{}'.format(tsua,to_guan_arr))
                break
        else:
            print('回傳狀態毋是200：{}', tsua)
        