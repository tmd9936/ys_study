BEGIN TRANSACTION;
CREATE TABLE users(            id INTEGER PRIMARY KEY,             username TEXT,             email TEXT,             tel TEXT,             website TEXT,             reg_date TEXT);
INSERT INTO "users" VALUES(1,'KIM','test@naver.com','010-1233-1232','www.test.com','2020-08-18 17:26:18');
INSERT INTO "users" VALUES(2,'Park','test2@naver.com','010-1231-1232','www.test.com','2020-08-18 17:26:18');
INSERT INTO "users" VALUES(3,'Choi','test@google.com','010-1234-1234','www.chol.com','2020-08-18 17:26:18');
INSERT INTO "users" VALUES(4,'Lee','test4@google.com','010-9221-1234','www.lee.com','2020-08-18 17:26:18');
INSERT INTO "users" VALUES(5,'Joo','test5@google.com','010-6655-1234','www.joo.com','2020-08-18 17:26:18');
COMMIT;
