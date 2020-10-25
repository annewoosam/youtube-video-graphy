"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb youtube_videos')

os.system('createdb youtube_videos')

model.connect_to_db(server.app)

model.db.create_all()


# Create video table's initial data.

with open('data/video.json') as f:

    video_data = json.loads(f.read())

video_in_db = []

for video in video_data:
    channel_name, video_number, video_title, length_hours, length_minutes, length_seconds, views, release_date, comments, likes, dislikes, description, last_updated= (
                                   video['channel_name'],
                                   video['video_number'],
                                   video['video_title'],
                                   video['length_hours'],
                                   video['length_minutes'],
                                   video['length_seconds'],
                                   video['views'],
                                   video['release_date'],
                                   video['comments'],
                                   video['likes'],
                                   video['dislikes'],
                                   video['description'],
                                   video['last_updated'])

    db_video = crud.create_video(
                                 channel_name,
                                 video_number,
                                 video_title,
                                 length_hours,
                                 length_minutes,
                                 length_seconds,
                                 views,
                                 release_date,
                                 comments,
                                 likes,
                                 dislikes,
                                 description,
                                 last_updated)

    video_in_db.append(db_video)
