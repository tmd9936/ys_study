# Caret 패키지 : 
# 머신러닝을 쉽게 할 수 있도록 도와주는 패키지
install.packages('caret', dependencies = TRUE)
library(caret)

rawdata <- read.csv(file="wine.csv", header=T)
rawdata$Class <- as.factor(rawdata$Class) # 범주형 데이터로 변환

str(rawdata)

# 트레이닝 - 테스트 데이터로 분할하기
analdata <- rawdata

set.seed(2020)

# sample(a, b) : 1부터 a까지의 숫자중에 b개를 추출
# nrow : 데이터의 행(row)수
datatotal <- sort(sample(nrow(analdata), nrow(analdata)*0.7))

train <- rawdata[datatotal, ]
test <- rawdata[-datatotal,]

train_X <- train[,1:13]
train_y <- train[,14]

test_x <- test[,1:13]
test_y <- test[,14]

# 데이터 훈련관정의 파라미터 설정하기 = trainContrlol
# method = "repeatedcv : cross-validation 반복
# number = 10 : 훈련데이터의 fold 갯수
# repeats = 5 : cross-validation의 반복 횟수
ctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 5)

# k 범위 설정 
customGrid <- expand.grid(k=1:10)

# 알고리즘을 이용해 데이터 학습을 통한 모델 생성 - train()
knnFit <- train(
  Class ~., # .은 모든데이터를 쓰겠다
  data = train,
  method = "knn",
  trControl = ctrl,
  preProcess = c("center", "scale"),
  tuneGrid = customGrid,
  metric = "Accuracy"
)

knnFit



plot(knnFit)

pred_test <- predict(knnFit, newdata = test)
confusionMatrix(pred_test, test$Class)


# 변수의 중요도
importance_knn <- varImp(knnFit, scale=F)
plot(importance_knn)





