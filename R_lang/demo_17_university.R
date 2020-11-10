# 로지스틱 회귀분석을 이용한 예측 (전에 하던거는 분석)

## 변수 설명

# GRE.Score : GRE 점수
# TOEFLE.Score : 토플 점수
# Univercity.Rating : 학부 대학 레이팅
# SOP : 자기소개서 점수
# LOR : 추천서 점수
# CGPA : 학부학점
# Research : 연구경험 유무
# Chance.of.Admit : 대학원 합격 확률

rawdata1 <- read.csv("university.csv", header=T)
str(rawdata1)

# FALSE = 0, TRUE = 1, 결과가 0이면 결측치 없음
sum(is.na(rawdata1$GRE.Score))
sum(is.na(rawdata1$TOEFL.Score))
sum(is.na(rawdata1$University.Rating))
sum(is.na(rawdata1$SOP))
sum(is.na(rawdata1$LOR))
sum(is.na(rawdata1$CGPA))
sum(is.na(rawdata1$Research))
sum(is.na(rawdata1$Chance.of.Admit))

unique(rawdata1$GRE.Score)
unique(rawdata1$TOEFL.Score)
unique(rawdata1$University.Rating)
unique(rawdata1$SOP)
unique(rawdata1$LOR)
unique(rawdata1$Research)
unique(rawdata1$Chance.of.Admit)

research_table <- table(rawdata1$Research)
research_table

# 타겟변수 최대,최소값 확인
max(rawdata1$Chance.of.Admit)
min(rawdata1$Chance.of.Admit)

# 연속형 => regression(회귀분석)
# 타겟의 데이터 범위가 0과 1사이에 있기 때문에 로시즈틱 회귀분석을 이용

# 변수 별 히스토그램
par(mfrow=c(3,2), mar=c(3,4,4,2))
hist(rawdata1$GRE.Score, main="GRE score histogram", xlab="GRE scoer", col="orange")
hist(rawdata1$TOEFL.Score, main="TOEFL", xlab="toefl scoer", col="green")
hist(rawdata1$SOP, main="SOP histogram", xlab="sop", col="blue")
hist(rawdata1$CGPA, main="CGPA score histogram", xlab="cgpa", col="red")
hist(rawdata1$LOR, main="LOR histogram", xlab="LOR", col="yellow")
hist(rawdata1$Chance.of.Admit, main="C.o.A histogram", xlab="chance_of_admit", col="brown")

# 산점도 Acceptance rate
plot(rawdata1)

# 트레이닝 / 테스트 데이터 나누기
set.seed(2020)
newdata <- rawdata1
train_ratio <- 0.7
datatotal <- sort(sample(nrow(newdata), nrow(newdata)*train_ratio))

train <- newdata[datatotal,]
test <- newdata[-datatotal,]

# 회귀분석으로 대학원 합격률 예측(caret패키지 사용)
library(caret)

# 로지스틱 회귀분석
# 오차최소값, rmse
ctrl <- trainControl(method = "repeatedcv", repeats=5)
logistic_fit <- train(Chance.of.Admit ~ .,
                      data=train,
                      method="glm",
                      trControl = ctrl,
                      preProcess = c("center", "scale"),
                      metric = "RMSE")

logistic_fit

# Rsquared(R제곱값) : 전체 변동성 중 설명가능한 변동성 비율율
logistic_pred <- predict(logistic_fit, newdata=test)
# 각 피처에 대한 합격률
logistic_pred









