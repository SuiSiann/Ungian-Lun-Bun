import sys
import re



論文名 = sys.argv[1]

with open(論文名, 'r') as lunbun:
    content = lunbun.readlines()

content = [x.strip() for x in content]


# 將文章照漢字台羅對應

bracketregex = re.compile("\[")
han_lineregex = re.compile(".*?[，、。]")
lo_lineregex = re.compile(".*?[,.]")

for tsua in content:
    # 才是漢羅對應文章
    if '[' in tsua and ']' in tsua:
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
        print('揣無中括號：{}\n\n'.format(tsua))