from app import app
from flask import render_template 
from .request import  publishedArticles





@app.route('/')
def home():
    articles = publishedArticles()

    return  render_template('home.html', articles = articles)



@app.route('/articles')
def articles():
    random = randomArticles()

    return  render_template('articles.html', random = random)

