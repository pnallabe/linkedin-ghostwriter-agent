import argparse
from agent.post_generator import generate_post
from agent.financial_news_scraper import run_news_commenting
from scheduler.cron_scheduler import schedule_agent


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--manual", action="store_true", help="Run once and exit")
    args = parser.parse_args()

    if args.manual:
        # generate_post()
        run_news_commenting()
    else:
        schedule_agent()