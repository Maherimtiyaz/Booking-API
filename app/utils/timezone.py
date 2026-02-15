from zoneinfo import ZoneInfo
from datetime import datetime, timezone

IST = ZoneInfo("Asia/Kolkata")

def convert_to_ist(dt: datetime):
    if dt.tzinfo is None:
       dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(IST)