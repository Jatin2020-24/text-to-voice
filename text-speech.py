from newspaper import Article
import nltk
from gtts import gTTS
import os

article = Article('D:\Reasearch Paper\hello.pdf')
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
myText = article.text
language = 'en-us'
myobj = gTTS(text=myText, lang=language, slow=False)
myobj.save("read_article.mp3")
os.system("start read_article.mp3")
