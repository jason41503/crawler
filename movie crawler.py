#yahoo movie crawler
import requests
from bs4 import BeautifulSoup
url = "https://movies.yahoo.com.tw/movie_intheaters.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGjm2hzQuDqQoHpMcTsm4qbjNdhsINYEosdtN24uFdMsbdkjBmVvg1OJd_U9LGF4Jc5pQdtG0mHgaZciK5smK2URLkOSOmrmQL82aqEhsdDDtEf_6gS-PzMChZAfePxTRpK_E8Qw8Zb15_IaFnzFXp00evOCzfzgGO7sa-dc6pM1"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
stories = soup.find_all("div","release_info_text")
count = 1
for s in stories:
    print(count,s.find("div","release_movie_name").a.text.strip())
    count += 1