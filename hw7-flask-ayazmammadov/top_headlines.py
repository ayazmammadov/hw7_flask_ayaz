'''
Name: Ayaz Mammadov
Uniqname:ayazm
'''

import secrets
import json

from flask import Flask,render_template
import requests



API_KEY = secrets.api_key
SECTION = "technology"
BASE_URL = "https://api.nytimes.com/svc/topstories/v2/"

app = Flask('/')

@app.route('/')
def index():
    return f'<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def welcome_name(nm):
    return render_template('name.html', name=nm, display_headlines="false", top_headlines=None)

@app.route('/headlines/<nm>')
def headlines(nm):
    top_headlines = top_five_headlines()
    return render_template('name.html', name=nm, display_headlines="true", top_headlines=top_headlines)


def build_url():
    return BASE_URL + SECTION + ".json?api-key=" + API_KEY

def top_stories():
    url = build_url()
    resp = requests.get(url)
    return json.loads(resp.text)['results']

def top_five_headlines():
    all_stories = top_stories()
    top_titles = []
    for title in all_stories:
        if title['section'] == 'technology':
            title_name = title['title']
            top_titles.append(title_name)
    if len(top_titles) < 5:
        return top_titles
    else:
        return top_titles[0:5]

if __name__ == '__main__':
    app.run(debug=True)


