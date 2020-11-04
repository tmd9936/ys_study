install.packages("foreign")

library(foreign)

library(dplyr)
library(ggplot2)

raw_welfare <- read.spss("data_spss_Koweps2014.sav", to.data.frame = T)

welfare <- raw_welfare
welfare

dim(welfare)
# 이데이터는 아래 명령으로는 파악하기 어렵다.
# 파악하는 방법은 전처리를 하면서 하나하나 검토
# 하는 방법을 사용한다.
str(welfare)

head(welfare)
summary(welfare)
View(welfare)

# 분석하고자 하는 변수의 코드를 알기쉽게 변경
welfare <- rename(welfare, 
                  sex = h0901_4, # 성별
                  birth = h0901_5, # 태어난 연도
                  income = h09_din) # 소득

######################################################3
# 분석 1 : 성별에 따른 소득
# 성별 변수 검토 (성별 전처리)
class(welfare$sex) # 속성 파악

# 무응답 없음
summary(welfare$sex)
table(welfare$sex)

# 만일 9가 있으면 NA처리
welfare$sex <- ifelse(welfare$sex == 9, NA, welfare$sex)

table(is.na(welfare$sex))

# 성별 항목 이름 부여
welfare$sex <- ifelse(welfare$sex == 1, "male", "female")

table(is.na(welfare$income))

table(welfare$sex)
# 가구주 단위로 보기때문에 male이 2배 더 많은것 처럼보임
qplot(welfare$sex)

# 소득 변수 전처리
# 변수에 대한 검토
class(welfare$income)

# 단위를 알 수 없음, 평균 수입이 낮게 나오는 이유
# 1인가구 포함, 미성년자, 고령층 포함
# 데이터의 특성을 파악하고 그것에 맞게 해석하는 것이 중요함
summary(welfare$income)


qplot(welfare$income)

qplot(welfare$income) + xlim(0,10000)

table(is.na(welfare$income))

# 성별 소득 평균 분석
# 평균표 만들기

sex_income <- welfare %>% 
  group_by(sex) %>% 
  summarise(mean_income = mean(income))

sex_income

# ggplot을 이용한 그래프 생성
ggplot(data = sex_income, aes(x = sex, y=mean_income)) + geom_col()

# 그래프의 해석: 남성이 여성보다 2배넘게 소득이 많다
# 실제로 남자의 소득이 여성의 소득의 2배라고 보면 안된다.
# 가구주 남성의 소득평균, 가구주 여성의 소득평균
# 가구주가 여성인 경우 1인가구 이거나 여성혼자 아이를 키우는 경우가 많다. 
# 즉, 남성에 비해 상대적으로 여성의 가구가 1인이거나 가구수가 적은 경우가 많다

# 따라서, 가구의 구성원 수를 파악하거나, 1인가구, 다인가구끼리 비교를 해야겠다는
# 아이디어를 도출할 수 있다. 좀 더 세밀한 분석을 하게된다.

######################################
# 분석 2 : 나이와 소득의 관계

# 이 데이터는 나이변수가 따로 없음.
# 태어난 연도로 나이를 계산

class(welfare$birth)


# 이 데이터는 일부러 노년층의 특석을 더 반영하기 위해서 노년층의 데이터를 더 
# 많이 표집했음을 알 수 있다.
# 다른 집단에 비해서 과대표집되어 있는 경향의 자료이다.

qplot(welfare$birth)

# 이상치가 없다는 것을 알 수 있음
# 최대값이 9999이면 이상치
summary(welfare$birth)
table(welfare$birth)

# 이상치가 있는 경우에는 결측처리
welfare$birth <- ifelse(welfare$birth == 9999, NA, welfare$birth)
table(is.na(welfare$birth))

# 지금까지의 결과를 보면 생년 변수에 오류가 없다는 것을 확인했음. 그럼,
# 나이라는 파생변수를 만들어 준다.

welfare$age <- 2014 - welfare$birth + 1

summary(welfare$age)

qplot(welfare$age)

# 나이 변수의 전처리가 끝났음.

# 나이별 소득 평균 분석하기
# 평균표 만들기
age_income <- welfare %>% 
  group_by(age) %>% 
  summarise(mean_income = mean(income))

age_income

# 그래프 만들기 - 산점도
ggplot(data = age_income, aes(x= age, y=mean_income)) + geom_point()

# 이 그래프의 오류를 찾아보자
# 이 그래프는 나이별로 그룹핑을 해서 평균을 구한 것임.
# 따라서, 13세가 1명인 경우에는 대표할 수 없는 평균임
# 의미있는 통계치로 사용하기에는 부적합하다.
# 연령대 별로 나눠서 보면 좋겠다는 아이디어를 도출해 낼 수 있다.

#####################################################
# 분석 3 : 연령대에 따른 소득

# 연령대 변수 생성
welfare <- welfare %>% 
  mutate(age_gp = ifelse(age < 30, "young", ifelse(age <= 59, "middle", "old")))


# young은 다른 그룹에 비해서 빈도수가 너무 적다. 따라서, 비교할 수 있는 대표성이 
떨어진다.
table(welfare$age_gp)

# young은 분석에서 제외하는 것이 타당하다는 판단을 할 필요가 있다.
qplot(welfare$age_gp)

# 연령대별 소득 평균표 생성(young 제외)
welfare_income <- welfare %>% 
  filter(age_gp != "young") %>% 
  group_by(age_gp) %>% 
  summarise(mean_income = mean(income))

# 그래프 생성하기
welfare_income
ggplot(data = welfare_income, aes(x = age_gp, y = mean_income)) + geom_col()


welfare_income <- welfare %>% 
  filter(age_gp != "young") %>% 
  group_by(age_gp, sex) %>% 
  summarise(mean_income = mean(income))

welfare_income
ggplot(data = welfare_income, aes(x=age_gp, y= mean_income, fill=sex)) +geom_col(position = "stack")
ggplot(data = welfare_income, aes(x=age_gp, y= mean_income, fill=sex)) +geom_col(position = "dodge")

sex_age <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age,sex) %>% 
  summarise(mean_income = mean(income))

sex_age
ggplot(data = sex_age, aes(x=age, y= mean_income, col = sex)) + geom_line() + xlim(20,90)


