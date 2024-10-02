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
  wrapperElm = findTargetdElm("div", ["wrapper", "clearfix"], bs(resp.text, "lxml"))
  if not wrapperElm: failAndExit()
  listElm = findTargetdElm("ul", ["clearfix"], wrapperElm)
  if not listElm: failAndExit()
  print()

def findTargetdElm(tagType: str, className: tuple, bsObj: bs):
  allTags = bsObj.find_all(tagType)
  for item in allTags:
    if item.has_attr("class") and tupleEquals(item["class"], className):
      return item
  return None

def failAndExit(msg="爬取网页失败"):
  print(msg)
  exit(-1)

if __name__ == "__main__":
  main()