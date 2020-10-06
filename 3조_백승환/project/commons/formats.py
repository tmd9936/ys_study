from project import app
from datetime import timedelta, datetime
import time

@app.template_filter("datetime_format")
def datetime_format(value):
    if value is None:
        return ""
    
    now_timestamp = time.time()

    # 클라이언트의 local 타임을 datetime형식으로 출력
    local_datetime = datetime.fromtimestamp(now_timestamp)
    print(local_datetime)

    # utcgromtimestamp는 UTC datetime을 리턴
    utc_datetime = datetime.utcfromtimestamp(now_timestamp)
    print(utc_datetime)

    offset_time = local_datetime - utc_datetime
    print("offset_time : ", offset_time)
    

    value = datetime.fromtimestamp((int(value) / 1000)) + offset_time

    # 글작성 날짜
    write_data = value.strftime('%Y-%m-%d')
    # 오늘 날짜
    today_data = utc_datetime.strftime('%Y-%m-%d')

    if write_data == today_data:
        return value.strftime('%H:%M:%S')
    else:
        return value.strftime("%Y-%m-%d")


