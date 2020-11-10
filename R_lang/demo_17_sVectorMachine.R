library(caret)

rawdata <- read.csv(file="wine.csv", header = T)
rawdata$Class <- as.factor(rawdata$Class)
str(rawdata)

# 테스트 데이터 분할
analdata <- rawdata

set.seed(2020)
datatotal <- sort(sample(nrow(analdata), nrow(analdata)*.7))
train <- rawdata[datatotal,]
test <- rawdata[-datatotal,]
str(train)

# 섢형 서포트 벡터 머신
ctrl <- trainControl(method = "repeatedcv", repeats = 5)
svm_linear_fit <- train(Class ~ .,
                        data=train,
                        method="svmLinear",
                        trControl = ctrl,
                        preProcess = c("center", "scale"),
                        metric="Accuracy")

svm_linear_fit

# prediction
pred_test <- predict(svm_linear_fit, newdata = test)
confusionMatrix(pred_test, test$Class)

# 변수의 중요도
importance_linear <- varImp(svm_linear_fit, scale = F)
plot(importance_linear)


# 비선형 서포트 벡터 머신
ctrl <- trainControl(method = "repeatedcv", repeats = 5)
svm_poly_fit = train(Class ~ .,
                     data = train,
                     mehod = "svmPoly",
                     trControl = ctrl,
                     preProcess = c("center", "scale"),
                     metric="Accuracy")

svm_poly_fit
plot(svm_poly_fit)

# prediction 예측
pred_test <- predict(svm_poly_fit, newdata = test)
confusionMatrix(pred_test, test$Class)

# 변수의 중요도
importance_poly <- varImp(svm_poly_fit, scale=F)
plot(importance_poly)





























