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
    han = []
    lo = []
    countHanLo = 0

    for tsua in txt_tong2:
        if tsua.strip() == '':
            countHanLo = 0
            kiat_ko += "<p class='han'>{}</p>".format(''.join(han))
            kiat_ko += "<p class='lo'>{}</p>".format(''.join(lo))
            han = []
            lo = []
            kiat_ko += "<br/>"
        elif countHanLo % 2 == 0:
            han.append(tsua)
            countHanLo += 1
        elif countHanLo % 2 == 1:
            lo.append(tsua)
            countHanLo += 1
        else:
            raise RuntimeError('發生錯誤：', tsua)
    kiat_ko += "<p class='han'>{}</p>".format(''.join(han))
    kiat_ko += "<p class='lo'>{}</p>".format(''.join(lo))

# In3 html
with open('output.html', 'w') as html_tong2:
    print(wrapper.format(kiat_ko), file=html_tong2)
