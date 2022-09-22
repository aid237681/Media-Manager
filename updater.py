from db_models import YT_Main, YT_Channel, YT_Video


def update_youtube():
    yt_data = YT_Main.objects.first()
    feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id="
    for channel in YT_Channel.objects:
        pass
