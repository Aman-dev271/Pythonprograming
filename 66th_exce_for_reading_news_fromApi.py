import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
if __name__ == '__main__':
    p = 16
    speak(f"may i have yur attentions plese now i am gone share with  you the {p} news ")
    url = ('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=fe216fa7a6834d7d923181b929ba2920')
    response = requests.get(url).text
    news_dict = json.loads(response)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        print(article)
        speak(article['title'])
        speak("Moving to the next news ...Listen Carefully")
    speak("news end...")
