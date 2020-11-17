## 데이터 정제
# 결측치(Missing value, NA) : 누락된 값, 비어있는 값

df <- data.frame(sex = c("M","F", NA, "M", "F"), score = c(5,4,3,4,NA))

# 결측치는 TRUE 아니면 FALSE로 표시
is.na(df)

# 결측치를 눈으로 일일이 확인하기 어려울 때
table(is.na(df))

# table
table(is.na(df$sex))
table(is.na(df$score))

# 결측치 포함된 상태에서 분석했을 경우
mean(df$sex)
mean(df$score)


# 결측치 제거
library(dplyr)

# score가 NA인 데이터만 출력
# 결측치가 TURE인것만 남음
df %>% filter(is.na(score))

#결측치 제외한 데이터 할당
df2 <- df %>% filter(!is.na(score))

# 결측치 제거후 분석
mean(df2$score)
sum(df2$score)

# 여러 벼수의 결측치를 동시에 제거하기
df_nomiss <- df %>% filter(!is.na(score) & !is.na(sex))
df_nomiss



# na.omit()은 결측치가 하나라도 있으면 제거
# 편리하기는 한데 실제로 잘 사용하지 않는다.
# a,b,c 열이 있을 때 a,b만 데이터분석 하려고 한다면
# omit쓰면 c만 결측치인 데이터까지 다 지움
# 예외로는 머신러닝 모형만들때, 데이터가 엄청 많을때는 씀

df_nomiss2 <- na.omit(df)
df_nomiss2

# na.rm = T : 결측치 제외하는 기능의 인자
df
# 결측치 제외 후 평균 구하기
mean(df$score, na.rm = TRUE)
# 결측치 제외 후 합계 구하기기
sum(df$score, na.rm = T)

exam <- read.csv("csv_exam.csv")

exam[c(5, 10, 15), "math"] <- NA

exam[c(3, 6, 9), c("english","math")]

# 평균값 오류 : NA출력
exam %>% summarise(mean_math = mean(math))

exam %>% summarise(mean_math = mean(math, na.rm = T), 
                   sum_math = sum(math, na.rm = T),
                   median_math = median(math, na.rm = T),
                   max_math = max(math, na.rm = T))

# 걸측치 대체(Inputation)하기
# 대표값(평균, 최빈값 등)으로 일괄 대체
# 최근에는 머신러닝 모형을 이용해 다른 변수를 입력하여 추정된 값으로 대체
# 여전히 가장 많이 사용하는 방법으로는 평균 대체법이다.

# 평균을 구해서
mean(exam$math, na.rm=T)

# 결측치에 대입
exam$math <- ifelse(is.na(exam$math), 59, exam$math)
table(is.na(exam))

exam

# 대체된 값으로 평균 출력
mean(exam$math)

library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
mpg[c(65, 124, 153, 212), "hwy"] <- NA

table(is.na(mpg$hwy))
table(is.na(mpg$drv))

mpg %>% 
  filter(!is.na(hwy)) %>% 
  group_by(drv) %>% 
  summarise(hwy_mean = mean(hwy))

###########################
# 이상치 : 논리적 오류값, 극단적인 값

outlier <- data.frame(sex = c(1, 2, 1, 5, 2, 1), # 성별 1, 2일 때
                      score = c(5, 4, 3, 4, 2, 7)) # score 최대 점수 5

outlier

# 빈도 수로 이상치 확인
table(outlier$sex) # 5라는 이상치 발견
table(outlier$score) # 7이라는 이상치 발견

outlier$sex <- ifelse(outlier$sex == 5, NA, outlier$sex)
outlier$score <- ifelse(outlier$score > 5, NA, outlier$score)

outlier

# 결측치 제거후 성별에 따른 score 분석
outlier %>% 
  filter(!is.na(sex) &!is.na(score)) %>% 
  group_by(sex) %>% 
  summarise(mean_score = mean(score))

# 극단적인 값 제거하기
# 논리적 판단, 통계치 판단, boxplot이용하여 제거

mpg <- as.data.frame(ggplot2::mpg)

min(mpg$hwy)
max(mpg$hwy)

boxplot(mpg$hwy)

# boxplot의 전체 통계치
boxplot(mpg$hwy)$stat


mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)

table(is.na(mpg$hwy))

mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy, na.rm = T))

mpg <- as.data.frame(ggplot2::mpg)

mpg[c(10, 14, 58, 93),"drv"] <- "k"
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42)


table(mpg$drv)
mpg$drv <- ifelse(mpg$drv == "k", NA, mpg$drv)
table(is.na(mpg$drv))

mpg$drv <- ifelse(mpg$drv %in% c(4,"f","r"), mpg$drv, NA)

boxplot(mpg$cty)$stat
mpg$cty <- ifelse(mpg$cty < 9 | mpg$cty > 26, NA, mpg$cty)
table(is.na(mpg$cty))

mpg %>% 
  filter(!is.na(drv) & !is.na(cty)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))

























































