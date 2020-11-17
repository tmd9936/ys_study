# 데이터 파악하기
# 함수       기능
# head()     데이터의 앞부분 출력
# tail()     데이터의 뒷부분 출력
# View()     원본 데이터를 확인
# dim()      데이터의 차원(행,열)
# str()      데이터의 속성(변수) 출력
# summary()  요약된 통계치 출력력

library(ggplot2)

# 데이터 준비하기
exam <- read.csv("csv_exam.csv")
head(exam, 10) # 앞에서 부터 10행까지 출력

tail(exam, 10)

View(exam)

# dim() : 몇 행 몇열로 구성되었는지 파악
dim(exam)

dim(exam)

# str() : 속성(변수) 파악
str(exam)

# summary() : 요약된 통계량 산출
summary(exam)

head(mpg, 20)
tail(mpg, 20)

dim(mpg)
str(mpg)
str(mpg)

# 변수만 파악
names(exam)

## mpg 데이터 파악하기
# data.frame()

library(help="datasets")

BOD
?quakes

dim(quakes)
dim(mpg)

data()

# 열x행으로 계산되기 때문에 5열 1000행인 데이터는 5000으로 해줘야 전부 출력됨
options(max.print = 5000)
quakes

## ggplot2의 mpg데이터를 데이터 프레임 형태로 불러오기
mpg <- as.data.frame(ggplot2::mpg)
mpg

head(mpg)

# 데이터 수정하기 - 변수명 바쑤기
install.packages(dplyr)
library(dplyr)

df_raw <-  data.frame(var1 = c(1,2,3), var2=c(2,3,2))
df_raw

df_new <-  df_raw
df_new

# 변수명 바꾸기
# rename() '새변수=기존변수' 순서로 사용
# var2를 v2로 수정
df_new <- rename(df_new, v2 = var2)
df_new

my_df <- data.frame(age=numeric(0), gender=character(0), weight=numeric(0))
# UI창으로 데이터 편집하기
my_df <- edit(my_df)

df_test = data.frame(var1=c("a","b","c"), p1=c(1:3))
df_test

# 파생 변수 만들기
df <- data.frame(var1 = c(4,3,8), var2=c(2,6,8))
df

df$var_sum = c("Hello","HI","Bye")
df$sum = df$var1 + df$var2

df$var_mean = (df$var1 + df$var2)/2
df <- edit(df)

# mpg 파생변수 생성
mpg$total <- (mpg$cty + mpg$hwy)/2

# 조건문 활용한 파생변수 생성
summary(mpg$total)

hist(mpg$total)

# ifelse를 이용한 합격 판정 변수 만들기
mpg$test <- ifelse(mpg$total >= 20, "pass", "fail")

head(mpg, 20)

# 합격/불합격 자동차 수 확인하기
table(mpg$test)

# 그래프 시각화
qplot(mpg$test)

mpg$grade <- ifelse(mpg$total >= 30, "A", 
                    ifelse(
                      mpg$total >= 25, "B",
                      ifelse(
                          mpg$total >= 20, "C", "D"
                        )
                      )
                    )
table(mpg$total)
head(mpg,50)

# 빈도수를 이용한 연비 등급 파악하기
table(mpg$grade) # 등급 빈도표 생성성
qplot(mpg$grade)

mpg %>% filter(grade == 'A')

midwest <- data.frame(midwest)

head(midwest)
tail(midwest)
View(midwest)
dim(midwest)
str(midwest)
summary(midwest)


midw <- rename(midwest, total=poptotal)
midw <- rename(midw, asian=popasian)
head(midw,20)
midw$perasian <- (midw$asian/midw$total)*100
hist(midw$perasian)
qplot(midw$county, midw$perasian)


midw_asianper_mean <- sum(midw$perasian)/count(midw)
midw_asianper_mean
midw$asiansize <- ifelse(mean(midw$perasian) < midw$perasian,"large","small")
table(midw$asiansize)
qplot(midw$asiansize)

dim(midw)
str(midw)
