from config.database.session import SessionLocal
from product.infrastructure.orm.product_fund import ProductFundORM
from scheduler.adapter.fund.fund_api import FundAPI
from scheduler.utils.date_utils import to_datetime_yyyymmdd

class FundService:

    @staticmethod
    def save_fund_info():
        db = SessionLocal()

        try:
            items = FundAPI.fetch_fund_list()

            if not items:
                print("[WARN] API에서 아이템이 없습니다.")
                return

            for item in items:
                record = ProductFundORM(
                    basDt=to_datetime_yyyymmdd(item.get("basDt")),
                    srtnCd=item.get("srtnCd"),
                    fndNm=item.get("fndNm"),
                    ctg=item.get("ctg"),
                    setpDt=to_datetime_yyyymmdd(item.get("setpDt")),
                    fndTp=item.get("fndTp"),
                    prdClsfCd=item.get("prdClsfCd"),
                    asoStdCd=item.get("asoStdCd"),
                )
                db.add(record)

            db.commit()
            print(f"[INFO] 펀드 정보 {len(items)}건 저장 완료")

        except Exception as e:
            db.rollback()
            print("[ERROR] save_fund_info:", e)

        finally:
            db.close()
