import requests
from bs4 import BeautifulSoup

for i in range(1, 20):
    res = requests.get(f"https://news.ycombinator.com/news?p={i}")
    soup = BeautifulSoup(res.text, "html.parser")
    link = soup.select(".storylink")
    subtext = soup.select(".subtext")
    for idx, item in enumerate(link):
        text = item.text
        href = item.get("href")
        votes = subtext[idx].select(".score")
        if len(votes):
            points = int(votes[0].text.replace(" points", ""))
            if points > 1000:
                print(f"{i}, {text}: {points}, {href} \n")
