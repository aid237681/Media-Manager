from sys import exit
import requests
from bs4 import BeautifulSoup
from db_models import YT_Channel


def add_yt_channel(link):
    feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id="
    # Create new YT_Channel object
    new_channel = YT_Channel()
    # Scrape the title and the Youtube Unique Channel ID from the provided URL
    response1 = requests.get(link, cookies={"CONSENT": "YES+42"})
    soup = BeautifulSoup(response1.text, "html.parser")
    new_channel.title = soup.find("meta", {"property": "og:title"}).get("content")
    new_channel.yt_uid = soup.find("meta", {"itemprop": "channelId"}).get("content")
    # Mark all videos but the last as "done"
    response2 = requests.get(feed_url + new_channel.yt_uid)
    soup = BeautifulSoup(response2.text, "xml")
    for entry in soup.find_all("entry")[1:]:
        new_channel.done_uids.append(entry.find("yt:videoId").text)

    # exit(soup.prettify())
    print(new_channel.to_json())
