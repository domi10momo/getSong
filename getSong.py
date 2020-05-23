import urllib.request
from bs4 import BeautifulSoup
import re

baseUrl = 'http://j-lyric.net'
artistUrl = '/artist/a0555ea'

def getHtml(url):
  return urllib.request.urlopen(url).read()

def getSoup(html):
  return BeautifulSoup(html, "lxml")

def getPath(p):
  a = p.find('a')
  path = a.get('href')
  return path
 
def getTitle(p):
  title = p.text
  title = title.replace(',', '，')
  title = title.replace('"', '”')
  return title

def createKashiUrl(p):
  return baseUrl + p

def parseAuthor(list):
  return list[1].text + '\n' + list[2].text

def parseKashiPage(url):
  kashiPage = getHtml(url)
  soup = getSoup(kashiPage)

  metaInfo = soup.find_all('p', class_='sml')
  author = parseAuthor(metaInfo)
  planeKashi = soup.find(id='Lyric').text
  kashi = re.sub(r'【.{1,3}】', '', planeKashi)
  return author + '\n' +kashi

def inputSong(filename, text):
  with open(filename, 'a') as f:
    #f.writelines(titles)
    f.write(text)

def writeSonglist(group, titles):
  filename = 'songlist/' + group + '.csv'
  songname = '\n'.join(titles)
  inputSong(filename, songname)


url = baseUrl + artistUrl
html = getHtml(url)
soup = getSoup(html)
group = soup.find(class_="cap").text.split('の歌詞リスト')[0]
pTags = soup.find_all("p", class_="ttl")
paths = [getPath(p) for p in pTags]
titles = [getTitle(p) for p in pTags]
print(titles)
#kashiUrls = [createKashiUrl(p) for p in paths]
#data = [parseKashiPage(k) for k in kashiUrls]
# data = parseKashiPage(kashiUrls[0])
writeSonglist(group, titles)
