import sys, csv, requests, os
from bs4 import BeautifulSoup as bs
sys.path.append("./")
from utils import tupleEquals

targetUrl = f"https://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html"
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
userPath = os.path.expanduser("~")
fileName = "phoneRank.csv"


def main():
  resp = requests.get(targetUrl, headers=header)
  wrapperElm = findTargetdElm("div", ["wrapper", "clearfix"], bs(resp.text, "lxml"))
  if not wrapperElm: failAndExit()
  listElm = findTargetdElm("ul", ["clearfix"], wrapperElm)
  if not listElm: failAndExit()
  phoneList = []
  for item in listElm.children:
    if item.name == "li":
      phoneList.append(item)
  dataList = savePhoneData(phoneList)
  writeData(userPath, dataList)


def findTargetdElm(tagType: str, className: tuple, bsObj: bs):
  allTags = bsObj.find_all(tagType)
  for item in allTags:
    if item.has_attr("class") and tupleEquals(item["class"], className):
      return item
  return None

"""
every data in dict like:
{
  phoneName,
  price,
  score,
}
"""
def savePhoneData(phoneList: list = []) -> list:
  dataList = []
  for data in phoneList:
    h3 = data.h3
    phoneData = []
    if h3:
      phoneData.append(h3.a["title"])
    else:
      continue

    priceText = findTargetdElm("b", ["price-type"], data)
    if priceText:
      phoneData.append(priceText.string)

    scoreText = findTargetdElm("span", ["score"], data)
    if scoreText:
      phoneData.append(scoreText.string)
    
    dataList.append(phoneData)
  
  return dataList


def writeData(userPath: str, dataList: list):
  filePath = os.path.join(userPath, fileName)
  with open(filePath, mode="w", newline="") as file:
    csvWriter = csv.writer(file)
    csvWriter.writerows([
      [
        "手机型号",
        "手机价格",
        "手机评分"
      ]
    ])
    for data in dataList:
      csvWriter.writerows([data])


def failAndExit(msg="爬取网页失败"):
  print(msg)
  exit(-1)


if __name__ == "__main__":
  main()