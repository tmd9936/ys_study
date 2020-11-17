# 변수
# 패키지로드
library(ggplot2)

str1 <- c("a", "b", "c")
li1 <- seq(1,10,by=2)

li1

# mpg 데이터의 변수를 다루기
head(mpg)

mean(mpg$hwy) # hwy 평균값
max(mpg$hwy) # 최대값
min(mpg$hwy)
hist(mpg$hwy)

# 변수 만들기
a <- 100
c <- 300
c <- 3.5

# 변수로 연산하기
a+c

# 연속값이 있는 변수 만들기
# c()함수 이용

dd <- c(1,2,3,4,5)
ee <- c(1:5)

sse <- seq(1,20, by=3.5)

ff <- seq(1,4)
ff
gg <- seq(1,10, by=2)

# 연속값 변수로 연산하기
dd + ee

# 문자 변수 만들기
a2 <- "a"
a2
b2 <- "world"
c2 <- "Hello world!"
c2

# 문자변수의 연산
a2+c2 # error

# 연속된 문자 변수를 만들기
d2 <- c("a","c","e")
d2
e2 <- c("Hello!!", "world", "is", "good")
e2

# 문자배열의 연산
d2+"11" #error











