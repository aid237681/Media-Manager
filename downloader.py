import youtube_dl


def download_video_yt(link, filename=None):
    class MyLogger:
        def __init__(self, link):
            self.link = link

        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            return f"Error while downloading: {self.link} - {msg}"

    ytdl_options = {
        "format": "best[ext=mp4]",
        "outtmpl": "%{id}s" if not filename else str(filename),
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
        "logger": MyLogger(link),
        "writethumbnail": True,
    }

    with youtube_dl.YoutubeDL(ytdl_options) as yt_dl:
        return yt_dl.download([link])


def download_video_tw(link, filename):
    class MyLogger:
        def __init__(self, link):
            self.link = link

        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            return f"Error while downloading: {self.link} - {msg}"

    ytdl_options = {
        "format": "best[ext=mp4]",
        "outtmpl": str(filename),
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
        "logger": MyLogger(link),
        "writethumbnail": True,
    }

    with youtube_dl.YoutubeDL(ytdl_options) as yt_dl:
        return yt_dl.download([link])


def download_audio_tw(link, filename):
    class MyLogger:
        def __init__(self, link):
            self.link = link

        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            return f"Error while downloading: {self.link} - {msg}"

    ytdl_options = {
        "format": "bestaudio",
        "outtmpl": str(filename),
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
        "logger": MyLogger(link),
        "writethumbnail": True,
    }

    with youtube_dl.YoutubeDL(ytdl_options) as yt_dl:
        return yt_dl.download([link])


def download_youtube_dl(link, filename):
    class MyLogger:
        def __init__(self, link):
            self.link = link

        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            return f"Error while downloading: {self.link} - {msg}"

    ytdl_options = {
        "outtmpl": filename,
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
        "logger": MyLogger(link),
    }

    with youtube_dl.YoutubeDL(ytdl_options) as yt_dl:
        return yt_dl.download([link])
