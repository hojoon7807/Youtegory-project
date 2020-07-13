from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import requests
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import googleapiclient.discovery
app = Flask(__name__)

client = MongoClient('mongodb://test:test@13.125.238.45',27017)
db = client.youtegory

def get_videos(category):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBP7wo8LVQcNgdUo5BQKMzZZejqgMI5Rds"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        maxResults=10,
        regionCode="KR",
        videoCategoryId=category
    )
    response = request.execute()
    items = response["items"]
    category = category
    idName = {"1":"Film&Animation", '2':"Cars&Vehicles", '10':"Music", '15':"Pets&Animals", '17':"Sports",
            '19':"Travel&Events", '20':"Gaming", '22':"People&Blogs", '23':"Comedy", '24':"Entertainmetn", '25':"News&Politics",
            '26':"Howto&Style", '27':"Education", '28':"Science&Technology", '29':"Nonprofits&Activism" }
    urls = []
    for item in items:
        ID = item["id"]
        url = "https://www.youtube.com/embed/" + ID
        doc={
            'url':url,
            'category':idName[category],
            'id':category
            }
        db.youtegory.insert_one(doc)    


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/category')
def category_page():
    return render_template('categoryPage.html')

@app.route('/api/list', methods=['GET'])
def show_list():
    idName = {"1":"Film&Animation", '2':"Cars&Vehicles", '10':"Music", '15':"Pets&Animals", '17':"Sports",
            '19':"Travel&Events", '20':"Gaming", '22':"People&Blogs", '23':"Comedy", '24':"Entertainmetn", '25':"News&Politics",
            '26':"Howto&Style", '27':"Education", '28':"Science&Technology", '29':"Nonprofits&Activism" }
    videosList = {}
    for category in idName.values():
        videos = list(db.youtegory.find({'category':category}, {'_id': False, 'category':False, 'id':False}))
        if(videos):
            videosList[category] = videos
    return jsonify({'result': 'success', 'videos': videosList})

@app.route('/api', methods=['POST'])
def get_category():
    category_receive = request.form['category_give']
    get_videos(category_receive)
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})
@app.route('/api/delete', methods=['POST'])
def category_delete():
    category_receive = request.form['category_give']
    db.youtegory.delete_many({'category':category_receive})
    return jsonify({'result': 'success','msg':'삭제되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



