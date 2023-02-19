from newspaper import Article
from textblob import TextBlob
import nltk
nltk.download('punkt')
def urltext(url):
    article=Article(url)
    article.download()
    article.parse()
    article.nlp()
    text=article.summary
    obj=TextBlob(text)
    sentiment=obj.sentiment.polarity
    return sentiment
def text(line):
    obj=TextBlob(line)
    sentiment=obj.sentiment.polarity
    return sentiment
def resultanalysis(sentiment):
    print('Sentiment analysis')
    if sentiment<-0.1 :
        print('The article is negative with polarity:',sentiment)
        print("\U0001F608")
    elif sentiment>-0.1 and sentiment <0.1 :
        print('The article is neutral with polarity:',sentiment)
        print("\U0001F642")
    else:
        print('The article is positive with polarity:',sentiment)
        print("\U0001F60D")
do='yes'
while do=='yes':
     print('''1.url article analysis
2.text analysis

choose one''')
     ch=int(input('Enter:'))
     if ch==1:
         print('Enter URL:')
         url=input()
         result=urltext(url)
         resultanalysis(result)
         do=input('Do you want to continue?')
     elif ch==2:
          print('Enter text:')
          line=input()
          result=text(line)
          resultanalysis(result)
          do=input('Do you want to continue?')
          


This project is done by PR.KRITHIKA PRIYA
