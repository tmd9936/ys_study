# 데이터 가공하기
# 데이터 전처리(분석하고자 하는 형태로 데이터 가공하는것)

#전처리(Preprocessing)시 자주 사용하는 패키지(dplyr)
#
library(dplyr)
library(ggplot2)
exam <- read.csv("csv_exam.csv")

# %>% 파이프 연산자 파이썬에서 .과 비슷함
# exam에서 class가 1인 데이터 추출하기
exam %>% filter(class==1)
exam %>% filter(class==2)
exam %>% filter(class != 1)

exam %>% filter(math > 50)

# 여러 조건을 만족하는 행 추출하기
exam %>% filter(class == 2 & english >= 70)
exam %>% filter(class == 1 & math >=50)
exam %>% filter(class == 3 & science <= 70)
exam %>% filter(math >=90 | english >=90)

exam %>% filter(class==1 | class==3 | class ==5)

# %in% (match operater)
exam %>% filter(class %in% c(1,3,5)) # 1,3,5 반에 해당하는 데이터 추출


# 추출한 행으로 데이터 만들기
class1 <- exam %>% filter(class == 1)
class2 <- exam %>% filter(class == 2)



mean(class1$math) # 1반 수학 평균점수
mean(class2$math) # 2반 수학 평균점수


mpg4 <- mpg %>% filter(displ <= 4)
mpg5 <- mpg %>% filter(displ >= 5)

mean(mpg4$hwy) # 25.96319
mean(mpg5$hwy) # 18.07895

# audi인 차를 구하고 cty열만 가져옴옴
m_audi <- mpg %>% filter(manufacturer == "audi") %>% select(cty)
m_toyota <- mpg %>% filter(manufacturer == "toyota")

mean(m_audi$cty) # 17.61111
mean(m_toyota$cty) # 18.52941

m_cfh <- mpg %>% filter(manufacturer %in% c("chevrolet", "ford", "honda"))
mean(m_cfh$hwy) # 22.50943


# 변수(컬럼) 추출
exam %>% select(math)
exam %>% select(english, math, science)
exam %>% select(-math, - english)

# filter와 select을 조합해서 추출하기

# class가 1인 행만 추출하고 english열만 추출
exam %>% 
  filter(class==1) %>% 
  select(english)


exam %>% 
  select(id, math) %>% 
  head(10)

mpg = as.data.frame(ggplot2::mpg)

mpgn <- mpg %>% select(class, cty)
head(mpgn,10)

suv = mpgn %>% filter(class=="suv")
compact = mpgn %>% filter(class=="compact")

mean(suv$cty)
mean(compact$cty)
 
# 정렬하기
# 기본값은 오름차순
exam %>% arrange(math) 
exam %>% arrange(desc(math)) # 내림차순

# 정렬 기준 변수를 여러개 지정하기기
exam %>% arrange(class, math) # class 및 math 오름차순

mpg <- as.data.frame(ggplot2::mpg)

mpg %>% 
  filter(manufacturer=="audi") %>% 
  arrange(desc(hwy)) %>% 
  head(5)


# dplyr 패키지의 mutate()함수를 이용한 파생변수 추가하기

exam %>% 
  mutate(total = math + english + science) %>% 
  head

# 여러개의 파생변수를 한 번에 추가하기
exam %>% 
  mutate(total = math + english, science,
         mean = (math + english + science)/3) %>% 
  head

# mutate() 함수에 ifelse() 적용하기
exam %>% 
  mutate(test = ifelse(science >= 60, "pass","fail")) %>% 
  head

exam %>%
  mutate(total = math + english + science) %>% 
  arrange(total) %>% 
  head

mpg <- as.data.frame(ggplot2::mpg)
mpg <- mpg %>% 
  mutate(chsum = cty + hwy)

mpg <- mpg %>% 
  mutate(chmean = chsum/2)

mpg %>% arrange(desc(chmean)) %>% 
  head(3)

ggplot2::mpg %>% 
  mutate(chsum = cty + hwy, chmean = chsum/2) %>% 
  arrange(desc(chmean)) %>% 
  head(3)

# 집단별로 요약 통계치 산출하기
exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math))

# 여러개의 요약 통계량을 한 번에 산출
exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math), # 수학평균
            sum_math = sum(math), # 수학 합계
            median_math = median(math),  # 수학의 중앙값값
            n = n()) # 행의 개수(학생 수)


mpg %>% 
  group_by(manufacturer, drv) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  head(10)

mpg %>% 
  group_by(manufacturer) %>% 
  filter(class=="suv") %>% 
  mutate(tot=(cty + hwy)/2) %>% 
  summarise(mean_tot = mean(tot)) %>% 
  arrange(desc(mean_tot)) %>% 
  head(5)


mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  arrange(desc(mean_cty))

mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mean_hwy = mean(hwy)) %>% 
  arrange(desc(mean_hwy)) %>% 
  head(3)

mpg
mpg %>% 
  filter(class=="compact") %>% 
  group_by(manufacturer) %>% 
  summarise(count = n()) %>% 
  arrange(desc(count))

# 데이터 합치기(가로, 세로)
test1 <- data.frame(id = c(1,2,3,4,5),
                   midterm = c(60,90,60,90,85))

test2 <- data.frame(id = c(1,2,3,4,5),
                   final = c(70,60,80,55,90))

test1
test2

# id 기준으로 합치기
total <- left_join(test1, test2, by="id")
total

name <- data.frame(class = c(1,2,3,4,5),
                   teacher = c("kim","park","lee","kang","hong"))

name

# class 기준으로 합치기
exam_new <- left_join(exam, name, by="class")

exam_new


# 세로 합치기
# 1~5번
group_a <- data.frame(id = c(1,2,3,4,5),
                      test = c(60,90,70,90,85))

# 6~10번
group_b <- data.frame(id = c(6,7,8,9,10),
                      test = c(78,56,23,67,11))

group_all <- bind_rows(group_a, group_b)
group_all

# Factor(범주형)
#   명묵형 : 성별 (카테고리 별 분류형 데이터) 남성을 1 여성을 2로 분류
#   순서형 : 적정온도 
#           10도 이상는 L 20도이상은 M 30도이상은 H

# 수치형
#   연속형 : 키, 길이
#   이산형 : 사람수, 나이

fuel <- data.frame(fl = c('c','d','e','p','r'),
                   price_fl = c(2.35, 2.38, 2.11, 2.76, 2.22),
                   stringsAsFactors = F)

nmpg = left_join(mpg, fuel, by="fl")
nmpg %>% 
  select(model, fl, price_fl) %>% 
  head(5)

midwest <- midwest %>% 
  mutate(perkids = (poptotal - popadults)/poptotal*100)
midwest %>% select(perkids)

midwest %>% 
  arrange(desc(perkids)) %>% 
  head(5)

midwest <- midwest %>% 
  mutate(perkidssize = ifelse(perkids >= 40,"large", ifelse(perkids >= 30,"middle","small")))

midwest %>% select(perkids, perkidssize)












