"""Server for youtube_YourModelNameLowerCaseSingularStats app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Video, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_videos():

    stats=crud.get_videos()
    
    channel_name=[q[0] for q in db.session.query(Video.channel_name).all()]

    video_number=[q[0] for q in db.session.query(Video.video_number).all()]
       
    video_title=[q[0] for q in db.session.query(Video.video_title).all()]

    length_hours=[q[0] for q in db.session.query(Video.length_hours).all()]

    length_minutes=[q[0] for q in db.session.query(Video.length_minutes).all()]

    length_seconds=[q[0] for q in db.session.query(Video.length_seconds).all()]

    views=[q[0] for q in db.session.query(Video.views).all()]

    release_date=[q[0] for q in db.session.query(Video.release_date).all()]

    comments=[q[0] for q in db.session.query(Video.comments).all()]

    likes=[q[0] for q in db.session.query(Video.likes).all()]

    dislikes=[q[0] for q in db.session.query(Video.dislikes).all()]

    description=[q[0] for q in db.session.query(Video.description).all()]

    last_updated=[q[0] for q in db.session.query(Video.last_updated).all()]

    video_list= db.session.query(Video.video_number, Video.description).all()

    return render_template('videos.html', channel_name=channel_name, video_number=video_number, video_title=video_title, length_hours=length_hours, length_minutes=length_minutes, length_seconds=length_seconds, views=views, release_date=release_date, comments=comments, likes=likes, dislikes=dislikes, description=description, last_updated=last_updated, video_list=video_list)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()