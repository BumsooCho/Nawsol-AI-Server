# scheduler/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.infrastructure.fund.fund_service import FundService
from scheduler.infrastructure.bond.bond_service import BondService  # 다른 API 있을 경우

def start_scheduler():
    scheduler = BackgroundScheduler()

    # 펀드 기본 정보 매일 03:30
    scheduler.add_job(FundService.save_fund_info, "cron", hour=3, minute=30)

    # 채권 정보 매일 04:00
    scheduler.add_job(BondService.save_bond_info, "cron", hour=4, minute=0)

    scheduler.start()
    print("[INFO] 스케줄러 시작됨")
