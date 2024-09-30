import sys, csv, requests
from bs4 import BeautifulSoup as bs
sys.path.append("./")
from utils import tupleEquals

targetUrl = f"https://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html"
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def main():
  resp = requests.get(targetUrl, headers=header)
  print("获取目标网页...")
  html = resp.text
  print("转换对象中...")
  bsSoup = bs(html, "lxml")
  findTargetdElm("div", ["wrapper", "clearfix"], bsSoup)

def findTargetdElm(tagType: str, className: tuple, bsObj: bs):
  allTags = bsObj.find_all(tagType)
  for item in allTags:
    if item["class"] and tupleEquals(item["class"], className):
      return item

if __name__ == "__main__":
  main()