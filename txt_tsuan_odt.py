import sys

txt_bun = sys.argv[1]

wrapper = """<html>
    <head>
    <title>Un2-gian5 lun5-bun5</title>
    <style>
    p {{font-family:"WenQuanYi Micro Hei"}}
    .han{{font-size:15pt; font-weight:"bold"}}
    .lo {{font-size:10pt;}}
    </style>
    </head>
    <body>{}</body>
    </html>"""

kiat_ko = ""

# Tak8 txt
with open(txt_bun, 'r') as txt_tong2:
    countHanLo = 0
    suHan = ""
    suLo = ""
    kuHan = ""
    kuLo = ""
    for tsua in txt_tong2:
        if tsua.strip() == '':
            countHanLo = 0
            kiat_ko += "<p class='han'>{}</p>".format(kuHan)
            kiat_ko += "<p class='lo'>{} 【{}{}】</p>".format(kuLo,suHan, suLo)
#             kiat_ko += "<p class='lo'>{}{}</p>".format(suHan, suLo)
            kiat_ko += "<br/>"
        elif countHanLo % 4 == 0:
            suHan = tsua
            countHanLo += 1
        elif countHanLo % 4 == 1:
            suLo = tsua
            countHanLo += 1
        elif countHanLo % 4 == 2:
            kuHan = tsua
            countHanLo += 1
        elif countHanLo % 4 == 3:
            kuLo = tsua
            countHanLo += 1
        else:
            raise RuntimeError('發生錯誤：', tsua)

# In3 html
with open('output.html', 'w') as html_tong2:
    print(wrapper.format(kiat_ko), file=html_tong2)
