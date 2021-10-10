from bs4 import BeautifulSoup
import requests

url = "https://camp-fire.jp/projects/category/food"
base_url = "https://camp-fire.jp"
res = requests.get(url)
soup = BeautifulSoup(res.text , 'html.parser')


# 取得したい情報
# 先に情報を全部取得し一つづつ関連付けて辞書型にしてからリストに保管する
# timeline画面:　　title リンク
# 詳細画面：　　支援者数,残り日数,支援総額,目標金額,達成率,説明

# 最終的に表示する辞書型とそのリスト
item_info = {"title":"","link":"","支援者数":0,"残り日数":0,"目標金額":0,"支援総額":0,"達成率":0}
item_arr = []

# info = soup.find_all("div",{"class":"box-in"})
# print(info)

for i in soup.find_all(["div",{"class":"box-title"},]):
    print(i)
    # if i.name == 'div' and i.get("class") == "box-thumbnail":
    #     print("tileのプリント",i.get_text(strip=True))
# print(info.find("div"))
# for i in info.find_all('div'):
#     print(i)
    # print(i.get("title"))
    # if i.title == 'div' and i.get("class") == "box-title":
    #     print("tileのプリント",i.get_text(strip=True))
    # else :
    #     print("")
# print("================================================================",info.get_text(),"=============================")