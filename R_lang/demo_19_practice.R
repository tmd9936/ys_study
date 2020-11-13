# age 나이
# job 직업
# martial 결혼유무
# education 학벌
# default 파산 유무
# housing 주택 대출 유무
# loan 개인 대출
# contact 연락 수단
# month 마지막으로 연락한 달
# day_of_week 마지막으로 연락한 요일
# duration 마지막 연락으로부터 경과 시간
# campaign 해당 마케팅 홍보 횟수
# previous 이전 마케팅 홍보 횟수
# poutcome 예전 마케팅 성공 여부
# emp.var.rate 고용 변동성
# cous.conf.price 소비자 물가지수
# cous.conf.idx 소비자 신뢰지수
# euribor3m 유리보3달(유로 기준 금리)
# ur.emplyed 고용지수
# target 마케팅 성공 여무(예금 등록 여부)

#################################################

# 전처리
## 결측치 처리 (컴퓨팅 환경에 따라 아예 지워버리는게 나을 수 있음..)
library(caret)
rawdata <- read.csv("financial_marketing.csv", header = T)
str(rawdata)
# 결측치 갯수
table(is.na(rawdata))

table(rawdata$education)

# 이상치 확인
# unknown -> 결측치
unique(rawdata$age)
unique(rawdata$job)
unique(rawdata$marital)
unique(rawdata$education)
unique(rawdata$default)
unique(rawdata$housing)
unique(rawdata$loan)
unique(rawdata$contact)
unique(rawdata$month)
unique(rawdata$day_of_week)
unique(rawdata$duration)
unique(rawdata$campaign)
unique(rawdata$previous)
unique(rawdata$poutcome)
unique(rawdata$emp.var.rate)
unique(rawdata$cons.price.idx)
unique(rawdata$cons.conf.idx)
unique(rawdata$euribor3m)
unique(rawdata$nr.employed)
unique(rawdata$target)

# unknown -> NA
rawdata[rawdata=="unknown"] <- NA

# na로 바꾸기
sum(is.na(rawdata))

# na omit -> na 데이터 지우기
rawdata <- na.omit(rawdata)
rawdata <- data.frame(rawdata)


# 히스토그램 
par(mfrow=c(3,3), mar=c(5,4,4,2))
hist(rawdata$age, main = "고객 나이", xlab="duration(time)", col='green')
hist(rawdata$duration, main = "마지막 연락으로부터 경과 시간",xlab="duration(time)", col='orange')
hist(rawdata$campaign, main = "해당 마케팅 홍보 횟수부",xlab="duration(time)", col='yellow')
hist(rawdata$previous, main = "이전 마케팅 성공 여부",xlab="duration(time)", col='grey')
hist(rawdata$emp.var.rate, main = "고용변동성", xlab="duration(time)", col='brown')
hist(rawdata$cons.price.idx, main= "소비자 물가지수", xlab="duration(time)", col='gold')
hist(rawdata$cons.conf.idx, main = "소비자 신뢰지수", xlab="duration(time)", col='blue')
hist(rawdata$euribor3m, main = "유리보3달", xlab="duration(time)", col='red')
hist(rawdata$nr.employed , main = "고용지수", xlab="duration(time)", col='purple')


# 표준화 scale
rawdata$age <- scale(rawdata$age)
rawdata$duration <- scale(rawdata$duration)
rawdata$campaign <- scale(rawdata$campaign)
rawdata$previous <- scale(rawdata$previous)
rawdata$emp.var.rate <- scale(rawdata$emp.var.rate)
rawdata$cons.price.idx <- scale(rawdata$cons.price.idx)
rawdata$cons.conf.idx <- scale(rawdata$cons.conf.idx)
rawdata$euribor3m <- scale(rawdata$euribor3m)
rawdata$nr.employed <- scale(rawdata$nr.employed)


# 주성분 분석 pca

head(rawdata)
str(rawdata)


# Factor Data
par(mfrow=c(4,3), mar=c(5,4,4,2))
barplot(prop.table(table(rawdata$job)), main="jop proportion" )
barplot(prop.table(table(rawdata$marital)), main="marital proportion" )
barplot(prop.table(table(rawdata$education)), main="education proportion" )
barplot(prop.table(table(rawdata$default)), main="default proportion" )
barplot(prop.table(table(rawdata$housing)), main="housing proportion" )
barplot(prop.table(table(rawdata$loan)), main="loan proportion" )
barplot(prop.table(table(rawdata$contact)), main="contact proportion" )
barplot(prop.table(table(rawdata$month)), main="month proportion" )
barplot(prop.table(table(rawdata$day_of_week)), main="day_of_week proportion" )
barplot(prop.table(table(rawdata$poutcome)), main="poutcome proportion" )
barplot(prop.table(table(rawdata$target)), main="target proportion" )

# categotical Data pie
par(mfrow=c(4,3), mar=c(5,4,4,2))
pie(prop.table(table(rawdata$job)), main="jop proportion" )
pie(prop.table(table(rawdata$marital)), main="marital proportion" )
pie(prop.table(table(rawdata$education)), main="education proportion" )
pie(prop.table(table(rawdata$default)), main="default proportion" )
pie(prop.table(table(rawdata$housing)), main="housing proportion" )
pie(prop.table(table(rawdata$loan)), main="loan proportion" )
pie(prop.table(table(rawdata$contact)), main="contact proportion" )
pie(prop.table(table(rawdata$month)), main="month proportion" )
pie(prop.table(table(rawdata$day_of_week)), main="day_of_week proportion" )
pie(prop.table(table(rawdata$poutcome)), main="poutcome proportion" )
pie(prop.table(table(rawdata$target)), main="target proportion" )

# 문자가 들어간 feature의 처리
rawdata$job = as.factor(rawdata$job)
rawdata$marital = as.factor(rawdata$marital)
rawdata$education = as.factor(rawdata$education)
rawdata$default = as.factor(rawdata$default)
rawdata$housing = as.factor(rawdata$housing)
rawdata$loan = as.factor(rawdata$loan)
rawdata$contact = as.factor(rawdata$contact)
rawdata$month = as.factor(rawdata$month)
rawdata$day_of_week = as.factor(rawdata$day_of_week)
rawdata$poutcome = as.factor(rawdata$poutcome)
rawdata$target = as.factor(rawdata$target)

# factor 대조군이 1개만 있는 컬럼 삭제
rawdata[,"default"] <- NULL
str(newdata)

set.seed(2020)
newdata <- rawdata

datatotal <- sort(sample(nrow(newdata), nrow(newdata)*.7))
train <- newdata[datatotal,]
test <- newdata[-datatotal,]

ctrl <- trainControl(method="repeatedcv", repeats = 5)

# 로지스틱 회귀분석
logistic_Fit <- train(target ~ .,
               data = train,
               method ="regLogistic",
               trControl = ctrl,
               metric="Accuracy")

logistic_Fit
plot(logistic_Fit)

logistic_pred = predict(logistic_Fit, newdata = test)
confusionMatrix(logistic_pred, test$target)

importance_logit <- varImp(logistic_Fit, scale=F)
plot(importance_logit)


# Boosted 로지스틱
boosted_Fit <- train(target ~ .,
                      data = train,
                      method ="LogitBoost",
                      trControl = ctrl,
                      metric="Accuracy")

boosted_Fit
plot(boosted_Fit)

boosted_pred = predict(boosted_Fit, newdata = test)
confusionMatrix(boosted_pred, test$target)

# 로지스틱 모형트리 (LMT)
lmt_Fit <- train(target ~ .,
                     data = train,
                     method ="LMT",
                     trControl = ctrl,
                     metric="Accuracy")

lmt_Fit
plot(lmt_Fit)

lmt_pred = predict(lmt_Fit, newdata = test)
confusionMatrix(lmt_pred, test$target)

# Penalized 로지스틱
plr_fit <- train(target ~ .,
                 data = train,
                 method ="plr",
                 trControl = ctrl,
                 metric="Accuracy")

plr_fit
plot(plr_fit)

plr_pred = predict(plr_fit, newdata = test)
confusionMatrix(plr_pred, test$target)

# Regularized 로지스틱

# 나이브 베이즈
nb_fit <- train(target ~ .,
                 data = train,
                 method ="naive_bayes",
                 trControl = ctrl,
                 metric="Accuracy")

nb_fit
plot(nb_fit)

nb_pred = predict(nb_fit, newdata = test)
confusionMatrix(nb_pred, test$target)

# 랜덤포레스트
rf_fit <- train(target ~ .,
                data = train,
                method ="rf",
                trControl = ctrl,
                metric="Accuracy")

rf_fit
plot(rf_fit)

rf_pred = predict(rf_fit, newdata = test)
confusionMatrix(rf_pred, test$target)

# 서포트 벡터머신
lin_fit <- train(target ~ .,
                data = train,
                method ="svmLinear",
                trControl = ctrl,
                metric="Accuracy")

lin_fit
plot(lin_fit)

lin_pred = predict(lin_fit, newdata = test)
confusionMatrix(lin_pred, test$target)

# 커널 서포트 벡터 머신
poly_fit <- train(target ~ .,
                 data = train,
                 method ="svmPoly",
                 trControl = ctrl,
                 metric="Accuracy")

poly_fit
plot(poly_fit)

poly_pred = predict(poly_fit, newdata = test)
confusionMatrix(poly_pred, test$target)


########################
# 0.8810802  0.8175 
# 0.8630969  0.8102 
# 0.8723595  0.8321

#
#
# 0.72 0.708
# 0.8601399 0.8686
# 0.8744373 0.8394
# 














