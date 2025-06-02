from apscheduler.schedulers.blocking import BlockingScheduler
from agent.vectorstore import build_vectorstore
from agent.post_generator import generate_post
import os
from agent.config import DB_DIR

def schedule_agent():
    scheduler = BlockingScheduler()
    scheduler.add_job(generate_post, 'cron', day_of_week='mon,wed,fri', hour=9)
    scheduler.add_job(run_news_commenting, 'cron', day_of_week='tue,thu', hour=9)
    print("Ghostwriter agent is running. Posts and comments will be auto-generated at scheduled times.")
    scheduler.start()

if __name__ == "__main__":
    schedule_agent()