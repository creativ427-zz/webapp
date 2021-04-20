from flask import render_template,redirect,url_for
from . import main
from ..request import get_sources,get_articles


# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting the news sources
    sports_sources = get_sources('sports')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    general_sources = get_sources('general')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    tech_sources = get_sources('technology')

    title = 'WatchDogs News App'
    return render_template('index.html', title=title, business=business_sources,
                           entertainment=entertainment_sources, general=general_sources, health=health_sources,
                           science=science_sources, sports=sports_sources, tech=tech_sources)


@main.route("/watchdogs/<source_id>")
def news_source(source_id):
    '''
    View new_source page function that returns a news source page and its data
    '''
    title=f"{source_id}-page"
    articles = get_articles(source_id)
    majorArticle= articles[0]
    major2Article=articles[1:5]
    latestArticle=articles[5:15]
    moreArticle=articles[15:]
    return render_template('newsSource.html', title=title,articles=articles,majorArticle=majorArticle,major2Article=major2Article,latestArticle=latestArticle,moreArticle=moreArticle)
