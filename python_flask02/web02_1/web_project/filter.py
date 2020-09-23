from web_project import datetime, app, time

######################################
# flask에서 사용하는 template filter
@app.template_filter("datetime_format")
def datetime_format(value):
    if value is None:
        return ""

    # 클라이언트의 현재 시스템의 local 타임 (컴퓨터의 시간)
    now_timestamp = time.time()

    # datetime 객체에는 fromtimestamp, utcfromtimestaop 함수가 있다.

    # fromtimestamp를 이용하면 클라이언트의 시간을 기준으로
    # datetime 객체를 만들어 준다.
    # 클라이언트의 local 타임을 datetime형식으로 만들어서 표현해줌
    print(datetime.fromtimestamp(now_timestamp))

    # utcfromtimestamp는 UTC datetime을 리턴한다.
    # db에 저장된 UTC format
    print(datetime.utcfromtimestamp(now_timestamp))

    # 클라이언트의 현재 datetime형식의 시간 - 현재 datetime형식의 UTC 시간
    offset_time = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    print("offset_time : ", offset_time)

    # value는 db에 저장되어 있는 timestamp형식의 utc타임
    # value를 datetime 객체로 만든후 시간차를 더해줌
    value = datetime.fromtimestamp((int(value) / 1000)) + offset_time

    return value.strftime("%Y-%m-%d %H:%M:%S")