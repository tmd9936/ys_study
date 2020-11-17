library(caret)

rawdata <- read.csv(file="wine.csv", header=T)
rawdata$Class <- as.factor(rawdata$Class)
str(rawdata)

analdata <- rawdata

set.seed(2020)
datatotal <- sort(sample(nrow(analdata), nrow(analdata)*.7))
train <- rawdata[datatotal,]
test <- rawdata[-datatotal,]

str(train)

ctrl <- trainControl(method="repeatedcv", repeats = 5)
nbFit <- train(Class ~ .,
               data = train,
               method ="naive_bayes",
               trControl = ctrl,
               preProcess= c("center", "scale"),
               metric="Accuracy"
               )

nbFit

plot(nbFit)

pred_test <- predict(nbFit, newdata = test)
confusionMatrix(pred_test, test$Class)

importance_nb <- varImp(nbFit, scale=F)
plot(importance_nb)



##########################
## naive bayes 결과 해석하기

# 커널 밀도 추정(kerneal Density Estimation)
# 데이터의 히스토그램을 이용하여 실제 분포를 측정하는 방식
# 히스토그램을 부드러운 곡선으로 표현함

# usekernel은 kde를 사용했는지 의미함

# 커널 밀도의 높이(세로)깂의 범위를 bandwidth로 보고
# 그 값이 달라지면 커널밀도추정(kdw)함수의 형태가 달라진다.

# adjust => bandwidth를 조정한다는 의미

## 라플라스 스무딩(Laplace Smoothing or Additive Smoothing)

# 데이터 수가 적을 경우, 0또는 1과 같이 극단적인 값으로 추정되는것을 방지하는 것

# x가나온 획수 + 알파
# -------------------- ==> 여기서 알파값은 x가 나온횟수가 0일 경우를 차단하기 위한 값값
# 전테 시행 횟수 + 알파














