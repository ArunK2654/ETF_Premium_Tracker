from apscheduler.schedulers.asyncio import AsyncIOScheduler
from service.job_service import run_etf_job
from core.logger import logger

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(func=run_etf_job, trigger="cron", minute="*/1") # to run once a day: scheduler.add_job(run_etf_job, trigger="cron", hour=0, minute=0)
    scheduler.start()
    logger.info("Scheduler started...")

def stop_scheduler():
    scheduler.shutdown()
    logger.info("Scheduler stopped.")
