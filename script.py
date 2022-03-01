
from newsapi import NewsApiClient

# this my api key
key  = "key api here"


# Init
newsapi = NewsApiClient(api_key=key)


# get everything from news-api depends on topic and plan you choose free plan is very limited 
all_articles = newsapi.get_everything( q='ukraine',
                                       sources='bbc-news,the-verge',
                                       domains='bbc.co.uk,techcrunch.com',
                                       from_param='2022-02-25',
                                       to='2022-02-28',
                                       language='en',
                                       sort_by='relevancy',
                                       page=2)



#  Loop Through articles of q topic (q="ukraine") 
#  print title and description

articles = all_articles["articles"]

print(type(articles))

for article in articles:
    print(article["title"]+" => "+article["description"])
    print('*******************************************')

