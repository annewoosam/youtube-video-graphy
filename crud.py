"""CRUD operations."""

from model import db, Video, connect_to_db

import datetime


def create_video(channel_name, video_number, video_title, length_hours, length_minutes, length_seconds, views, release_date, comments, likes, dislikes, description, last_updated):
   

    video = Video(channel_name=channel_name,
                  video_number=video_number,
                  video_title=video_title,
                  length_hours=length_hours,
                  length_minutes=length_minutes,
                  length_seconds=length_seconds,
                  views=views,
                  release_date=release_date,
                  comments=comments,
                  likes=likes,
                  dislikes=dislikes,
                  description=description,
                  last_updated=last_updated)

    db.session.add(video)

    db.session.commit()

    return video

def get_videos():
    """Return all rows of video monthly data."""

    return Video.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
