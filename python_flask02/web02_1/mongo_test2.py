import pymongo

conn = pymongo.MongoClient("localhost", 27017)
db = conn.test
collection = db.members

##################### 데이터 수정 ######################
# rs = collection.find({"이름":"강길동"})

# 아래처럼 이름을 고말똥으로 수정하는 경우 이름 필드외에 나머지 필드는 모두 삭제됨
# 데이터를 날릴 수 있음
# collection.update({"이름":"강길동"},{"이름":"고말똥"})

# $set을 이용하면 나머지 필드는 모두 존재함
# 첫번째 document만 수정
# collection.update({"이름":"김유동"}, 
#             {"$set":
#                 {
#                     "이름":"손흥민"
#                 }
#             })

# mlti=True를 해주면 여러개의 document를 동시에 수정
# collection.update({"이름":"고길동"},
#             {"$set": 
#                 {
#                     "이름":"손흥민"
#                 }
#             }, multi=True)

# nosql이기때문에 필드를 동적으로 생성 할 수 있음
# collection.update({"이름":"손흥민"},
#             {"$set": 
#                 {
#                     "별명":"축구맨"
#                 }
#             })

# 이름 박지성이 없기 때문에 아무 변화가 없음
# collection.update({"이름":"박지성"}, {"$set":{"별명":"박짱"}})

# upsert= True => 대상이 존재 하지 않을 때 insert를 실행 있으면 update를 실행
# collection.update({"이름":"박지성"}, {"$set":{"별명":"박짱"}}, upsert= True)

# for r in rs:
#     print(r)


##################### 데이터 삭제 ######################
# collection.remove({"이름":"박지성"})

# 컬렉션의 데이터가 모두 날아감
# collection.remove({})

# collection.delete_one({"이름":"손흥민"})
collection.delete_many({"이름":"손흥민"})

