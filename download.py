import requests
import urllib
import bs4
import sys

url_base = "http://sillok.history.go.kr/id/"
ids = ["kaa_10107017_001",
        "kba_10101001_001",
        "kca_10101001_001",
        "kda_10008011_001",
        "kea_10002018_001",
        "kfa_10005014_001",
        "kga_10106111_001",
        "kha_10009007_001",
        "kia_10011028_001",
        "kja_10012025_001",
        "kka_10109002_001",
        "kla_10101001_001",
        "kma_10007007_001",
        "kna_10007004_001",
        "knb_10007003_001",
        "koa_10002001_001",
        "kob_10002001_001",
        "kpa_10103013_001",
        "kqa_10005008_001",
        "kra_10005004_001",
        "krb_10005004_001",
        "ksa_10008018_001",
        "ksb_10008026_001",
        "kta_10006008_001",
        "ktb_10006008_001",
        "kua_10008030_001",
        "kva_10003010_001",
        "kwa_10007004_001",
        "kxa_10011018_001",
        "kya_10006009_001"]

idx = 0
doc_id = ids[idx]

while True:
    url = url_base + urllib.parse.quote(doc_id)
    print('getting page {}'.format(url))
    try:
        page = requests.get(url)
    except KeyboardInterrupt:
        break
    except:
        print('page loading failed by error {}. retrying...'.format(sys.exc_info()[0]))
        continue
    if page.status_code != 200:
        print('page status code {}. retrying...'.format(page.status_code))
        continue

    html_doc = page.content
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    kor = soup.select_one('.ins_view.ins_view_left')
    lzh = soup.select_one('.ins_view.ins_view_right')

    def cleanup(tree):
        for sup in tree.find_all('sup'):
            sup.decompose()

        for tag in tree.select('.ins_footnote, .ins_source, .ins_view_line'):
            tag.decompose()

        text = tree.text
        text = ' '.join(text.split())
        return text
  
    kor = cleanup(kor)
    lzh = cleanup(lzh)

    with open('KOR_{}.txt'.format(doc_id), "w") as f:
        f.write(kor)
    with open("LZH_{}.txt".format(doc_id), "w") as f:
        f.write(lzh)
   
    try:
        doc_id = soup.select("ul.view_btnset.mt_-20 li a")[1]['href'][19:-3] 
    except:
        idx += 1
        doc_id = ids[idx]
        print('next book: {}'.format(doc_id))

