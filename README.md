# WatchDogs News App

#### 26/07/2019

## Description

[WatchDogs News App](https://watchdogs-news-app.herokuapp.com/) is web application that allows users to access news from all over the globe.The app fetches various news sources and sorts them based on categories.The application leverages the power of the [News API](https://newsapi.org/).A user can click on a News source and be directed to a page that contains **News Articles** from the selected News source. The article's title, image, date of publication and preview will be displayed.A user can click on the article to be directed to the source's site to read the entire article.

## Behaviour Driven Development

1.Feature Select A News Source

**Scenario:Selecting a news Source**

    Given There is/are news sources availabe
    When i click on a source
    Then i i will be redirected to that news source
    And i will see articles from that source

2.Feature Select an Article

**Scenario:Clicking an article**

    Given there are multiple articles
    When i click i on the articles's title
    Then i should be redirected to the articles news source page

3.Feature Clicking the watchdogs brand

**Scenario:Clicking the brand name**

    Given there is a brand name
    When i click the brand
    Then i should be redirected to the home page
    And i should see the various news sources

## Prerequisites

- Download and install Python3.6 if you wish to build the app from the ground up or improve on
- The requirements.txt file has all the dependencies for the project listed out

## Setup/Installation

- Click [This](https://watchdogs-news-app.herokuapp.com/) and you will be rerouted to where the app is hosted
- Requires internet connection

## Known Bugs

- Some news sources may not have data in them.Just navigate back and pick another source
- No Search feature has been implemented(Will be done by weeks end)
- The NewsAPi shuts down if request exceed 250 in a given day

## Technologies Used

- Python3.6
- Flask
- Html5
- Bootstrap
- Css

### License

MIT (c) 2019 **[PURITY KETER](https://github.com/creativ427/webapp)**
