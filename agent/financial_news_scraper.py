import os
import requests
import datetime
from bs4 import BeautifulSoup
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from apscheduler.schedulers.blocking import BlockingScheduler
from .config import GOOGLE_NEWS_URL
from .config import TOPICS
from .rag_chain import get_rag_chain

def fetch_financial_news():
    response = requests.get(GOOGLE_NEWS_URL)
    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")
    news_items = []
    for item in items:
        title = item.title.text
        link = item.link.text
        print(title)
        if any(topic.lower() in title.lower() for topic in TOPICS):
            news_items.append((title, link))
    return news_items[:10]  # Limit to top 10 relevant news

def generate_news_comment(news_text, url):
    chain = get_rag_chain()
    prompt = f"write a 200 word insightful LinkedIn comment responding to this financial news : '{news_text}'."
    comment = chain.run(prompt)
    output = f"🗞️ News Headline: {news_text}\n🔗 {url}\n💬 Suggested Comment: {comment}\n"
    print("\n" + output)
    with open("output/news_comments.txt", "a") as f:
        f.write(output + "\n")
    return comment

def run_news_commenting():
    news_items = fetch_financial_news()
    print(news_items)
    for title, link in news_items:
        print('\n news items:title',title,'\t link:',link)
        generate_news_comment(title, link)