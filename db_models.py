from mongoengine import PULL, Document, StringField, IntField, ListField, ReferenceField


class YT_Video(Document):
    uid = IntField()
    yt_uid = StringField()
    title = StringField()
    video_path = StringField()


class YT_Channel(Document):
    uid = IntField()
    yt_uid = StringField()
    title = StringField()
    videos = ListField(ReferenceField(YT_Video, reverse_delete_rule=PULL), default=list)
    done_uids = ListField(StringField(), default=list)


class YT_Main(Document):
    last_id = IntField()
