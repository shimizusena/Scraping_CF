from bs4 import BeautifulSoup
import requests

url = "https://camp-fire.jp/projects/category/food"
base_url = "https://camp-fire.jp"
res = requests.get(url)
soup = BeautifulSoup(res.text , 'html.parser')


# 取得したい情報
# timeline画面:　　title リンク
# 詳細画面：　　支援者数,残り日数,支援総額,目標金額,達成率,説明
item_info = {"title":"","link":"","支援者数":0,"残り日数":0,"目標金額":0,"支援総額":0,"達成率":0}
item_arr = []


info = soup.find("div",{"class":"boxes4 clearfix"})
# titleの取得
titles = info.find_all('h4')
title_arr = [title.get_text() for title in titles]

# linkの取得
link_arr = []
links = info.find_all('div',{"class":"box-thumbnail"})
for l in links:
    links_a = l.find_all('a')
    if len(links_a) > 1:
        u = links_a[len(links_a)-1].get("href")
    link_arr.append(base_url + u)

# 支援者数
supporter_count = info.find_all('div',{"class":"rest"})
supporters = [(sc.get_text()).replace("\n","")  for sc in supporter_count]

#残り日数
 

# print(supporters)

for i in range(len(title_arr)):
    item_info["title"] = title_arr[i]
    item_info["link"] = link_arr[i]
    item_arr.append(item_info)

# print(len(item_arr))
