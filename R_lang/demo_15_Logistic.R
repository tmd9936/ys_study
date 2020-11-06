library(caret)

rawdata <- read.csv(file="heart.csv", header = T)
str(rawdata)

# target : 심장병 유무
# cp : 통증 타입
# trestbps : 혈압
# chol : 콜레스테롤
# fbs : 공복혈당 > 120
# restecg : 심전도 결과
# thalach : 심박수
# exang : 협심증
# oldpeak : 운동에 의해 정하되는 ST
# slope : ST 분절 기울기
# ca : 형광투시법에 착색되는 주요 혈관수
# thal : 결함 유무무

# 타겟(정답, class) 변수의 범주화
rawdata$target <- as.factor(rawdata$target)

# 연속형 독립변수에 대해서는 표준화를 한다.
rawdata$age <- scale(rawdata$age)
rawdata$trestbps <- scale(rawdata$age)
rawdata$chol <- scale(rawdata$age)
rawdata$thalach <- scale(rawdata$age)
rawdata$slope <- scale(rawdata$age)


# 범주형 독립변수는 범주화
newdata <- rawdata
factVar <- c("sex","cp","fbs","restecg","exang","ca","thal")

# factVar을 lapply함수를 이용하여 한번에 factor로 바꿔주기
# lapply(c,mean) : x(리스트, 데이터)에 mean함수를 적용한 결과를 리턴한다.

newdata[,factVar] = lapply(newdata[, factVar], factor)


# 트레이닝 - 테스트 데이터 분할
set.seed(2020)
datatotal <- sort(sample(nrow(newdata), nrow(newdata)*0.7))
train <- newdata[datatotal, ]
test <- newdata[-datatotal, ]

# 학습모델 생성 

# "LogitBoost", "LMT", "plr", "regLogistic"
ctrl <- trainControl(method= "repeatedcv", repeats = 5)
logitFit <- train(target ~ ., 
                  data = train,
                  method = "regLogistic",
                  trControl = ctrl,
                  metric = "Accuracy")

# nIter : 반복 횟수
logitFit

plot(logitFit)

# 모델을 이용한 예측
pred_test <- predict(logitFit, newdata = test)
confusionMatrix(pred_test, test$target)

# 변수의 중요도
importance_logit <- varImp(logitFit, scale=F)
plot(importance_logit)

# 로지스틱 회귀분석에 사용된 패키지
# 1. Boosted Logistic Regression(method ='LogitBoost')
# -> 각각의 피처를 돌리고 다른피처 돌리고 더하고 ....
# -> 가장 간단한 모형으로 시작해서 점차 개전된 모형으로 개선시키는 방식식

# 2. Logistic Model Trees(method = 'LMT')
# -> 로지스틱회귀와 의사결정나무를 합친 모형

# 3. penalized Logistic Regression(method = 'plr')
# -> 정규화(Regularization)를 통해 모텔의 복잡성을 조절하는 방식(L2 정규화)
# -> 정규화를 하는이유는 오버피팅을 피하기 위함
# 결과 해석시에 람다의 크기에 따라 베타영역의 크기가 달라짐(람다:λ)
# λ∑β² < t

# 4. Regularized Logistic Regression(method = 'regLogistic')
# -> L1정규화와 L2정규화를 모두 사용할 수 있는 방식
# -> 결과 해석 
# primal : 베타 파라미터를 기준으로 최적화
# dual : 람다 제약변수를 기준으로 최적화
# 

## L1 : 베타값을 절대값으로 변환해서 마름모 꼴로 만듦
## L2 : 베타값을 제곱함


















