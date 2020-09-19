import pymongo

mem = {
    '이름':'홍길동',
    '나이':30,
    '주소':'인천',
    '전화번호':'010-2323-2323',
    '프로필사진':['a.jpg', 'b.jpg']
}

# schema-less : 스키마가 없기 때문에 아래와 같이 입력을 하더라도 
# 에러가 발생하지 않음
mem2 = {
    "이름" : "주부도",
    "나이" : 55,
    "주소" : "대구",
    "학교" : "우리대",
}

# 접속 객체 리턴(MongoClient: 접속해주는 라이브러리, 주소와 포트를 매개변수로 사용)
conn = pymongo.MongoClient("localhost", 27017)

# test라는 데이터베이스가 없으면 새로 생성한다. db라는 이름으로 받았음
# db는 test 데이터베이스를 의미함
db = conn.test

# members라는 컬렉션이 있으면 받아오고, 없으면 새로 생성을 한다
collection = db.members

# 데이터 삽입하기
# collection.insert(mem)
# collection.insert(mem2)

# 데이터 검색(조회)

# cursor 객체가 리턴됨
results = collection.find()
# print(results) # 커서 객체 출력
# results = collection.find({"이름":"강길동", "학교":"우리대"}) # and 연산
# results = collection.find({"$or" : [{"이름":"강길동"}, {"주소":"대구"}, {"주소":"인천"}]}) # or 연산

# 첫 번째 조회된 document 객체 하나만 가져옴
# result = collection.find_one({"이름":"고길동"})
# print(result)

# results = collection.find({"나이":{"$gt":50}}) # 나이 > 50 보다 큰 객체 greater than
# results = collection.find({"나이":{"$gte":50}}) # 나이 >= 50
# results = collection.find({"나이":{"$gt":30, "$lt": 60}}) # 30 < 나이 < 60

# 원하는 필드만 출력하기
# results = collection.find({"나이":{"$gt":30, "$lt": 60}}, {"_id":False,"이름": True}) # 30 < 나이 < 60

# _id 필드는 생략하고, 이름필드, 주소 필드만 출력하세요.
# results = collection.find({"나이":{"$gt":30, "$lt": 60}}, {"_id":False,"이름": True, "주소":True}) # 30 < 나이 < 60

# 상위 2개만 출력
# results = collection.find({"나이":{"$gt":30, "$lt": 60}}, {"이름": True, "주소":True}).limit(2)

# 상위 2개를 건너 뜀
# results = collection.find({"나이":{"$gt":30, "$lt": 60}}, {"이름": True, "주소":True}).skip(2).limit(2)

# sort(정렬): 1이면 내림차순 -1이면 오름차순
results = collection.find({"나이":{"$gt":30, "$lt": 60}}, {"이름": True, "나이":True}).sort("나이",-1)

for r in results:
    print(r)