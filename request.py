from app.models import FinanceLiteracy
from newsapi import NewsApiClient
from .config import Config
import urllib.request,json

api_key=None
base_url=None
base_url_for_everything=None
base_url_top_headlines=None
base_source_list=None



def publishedArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)

    get_articles = newsapi.get_everything(sources= 'cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')

    all_articles = get_articles['articles']

    articles_results = []

    id = []
    img = []
    title = []
    short_desscription = []
    post_content=[]

    for i in range(len(all_articles)):
        article = all_articles[i]

        id.append(article['id'])
        title.append(article['title'])
        short_desscription.append(article['short_description'])
        post_content.append(article['post_content'])
        img.append(article['urlToImage'])
    

        article_object = FinanceLiteracy(id, title, short_desscription, post_content)

        articles_results.append(article_object)

        contents = zip(id, title, short_desscription,post_content)

    return  contents

