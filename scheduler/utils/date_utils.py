from datetime import datetime

def to_datetime_yyyymmdd(date_str: str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y%m%d")
    except:
        return None