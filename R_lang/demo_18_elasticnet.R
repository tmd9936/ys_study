## classification(분류)으로 합격 여부 예측하기

# target 값 --> 명목형(범주형) --> 분류(classification)
# target 값 --> 연속형 숫자 --> 회귀(Regression)

# 합격여부 판단을 위한 기준점 
library(caret)

rawdata2 <- read.csv("university.csv", header = T)

str(rawdata2)

par(mfrow=c(1,2), mar=c(5,4,4,2))
hist(rawdata2$Chance.of.Admit,main = "대학원 합격률 히스토그램", xlab="대학원 합격 확률", col='green')
boxplot(rawdata2$Chance.of.Admit, main= "대학원 합격률 박스플롯", col="purple")

summary(rawdata2$Chance.of.Admit)
target_median = median(rawdata2$Chance.of.Admit)
target_median

# 타깃의 연속형 값 --> 범주형
rawdata2[(rawdata2$Chance.of.Admit < target_median), "Chance.of.Admit"] = 0
rawdata2[(rawdata2$Chance.of.Admit >= target_median), "Chance.of.Admit"] = 1

rawdata2$Chance.of.Admit <- as.factor(rawdata2$Chance.of.Admit)
str(rawdata2)

unique(rawdata2$Chance.of.Admit)

rawdata2

# 트레이닝 / 테스트 분류
set.seed(2020)
newdata2 <- rawdata2
train_ratio <- 0.7
datatotal2 <- sort(sample(nrow(newdata2), nrow(newdata2)*train_ratio))
train2 <- newdata2[datatotal2,]
test2 <- newdata2[-datatotal2,]

# 분류 : Accuarcy, 회귀 : RMSE
# knn
ctrl <- trainControl(method="repeatedcv", repeats = 5)
customGrid <- expand.grid(k=1:20)
knn_fit <- train(Chance.of.Admit ~ .,
                  data=train2,
                  method="knn",
                  trControl=ctrl,
                  preProcess = c("center", "scale"),
                  tuneGrid = customGrid,
                  metric="Accuracy")

knn_fit

plot(knn_fit)

# 예측
pred_test <- predict(knn_fit, newdata = test2)
confusionMatrix(pred_test, test2$Chance.of.Admit)

# Boosted logistic
ctrl <- trainControl(method="repeatedcv", repeats = 5)
logitboost_fit <- train(Chance.of.Admit ~ .,
                       data=train2,
                       mehod="LogitBoost",
                       trControl=ctrl,
                       preProcess = c("center", "scale"),
                       metric="Accuracy")

logitboost_fit
plot(logitboost_fit)


pred_test <- predict(logitboost_fit, newdata = test2)
confusionMatrix(pred_test, test2$Chance.of.Admit)

importance_nb <- varImp(logitboost_fit, scale=F)
plot(importance_nb)


##  logit plr
ctrl <- trainControl(method="repeatedcv", repeats = 5)
logit_plr_fit2 <- train(Chance.of.Admit ~ .,
                        data=train2,
                        mehod="plr",
                        trControl=ctrl,
                        preProcess = c("center", "scale"),
                        metric="Accuracy")

logit_plr_fit2

pred_test <- predict(logit_plr_fit2, newdata = test2)
confusionMatrix(logit_plr_fit2, test2$Chance.of.Admit)

importance_nb <- varImp(logit_plr_fit2, scale=F)
plot(importance_nb)

## naive bayse 
# : 대학원 합격 여부를 결정하는 가각의 Feature를 독립사건으로 가정하고
# 조건부 확률을 적용하는 분류방법

ctrl <- trainControl(method="repeatedcv", repeats = 5)
nb_fit2 <- train(Chance.of.Admit ~ .,
                        data=train2,
                        mehod="naive_bayes",
                        trControl=ctrl,
                        preProcess = c("center", "scale"),
                        metric="Accuracy")


nb_fit2

nb_pred <- predict(nb_fit2, newdata = test2)
confusionMatrix(nb_pred, test2$Chance.of.Admit)

# 결과 해석 : userkernel - 커널 밀도함수 사용여부
#           : adjust - 커널 밍도함수의 bandwidth 값 조절
#           : laplace - 데이터의 수가 적을 경우 0 또는 1과 같은 극단적인 값으로 추정되는 것을 막기 위한 값

## random forrest
# 결과해석 : mtry - 각 트리에서 랜덤하게 선택되는 분할 피처 후보 개수

ctrl <- trainControl(method="repeatedcv", repeats = 5)
rf_fit2 <- train(Chance.of.Admit ~ .,
                 data=train2,
                 mehod="rf",
                 trControl=ctrl,
                 preProcess = c("center", "scale"),
                 metric="Accuracy")


rf_fit2

rf_pred <- predict(rf_fit2, newdata = test2)
confusionMatrix(rf_pred, test2$Chance.of.Admit)


# 서포트 백터 머신
ctrl <- trainControl(method = "repeatedcv", repeats = 5)
svm_linear_fit <- train(Chance.of.Admit ~ .,
                        data=train2,
                        method="svmLinear",
                        trControl = ctrl,
                        preProcess = c("center", "scale"),
                        metric="Accuracy")

svm_linear_fit

# prediction
svm_linear_pred <- predict(svm_linear_fit, newdata = test)
confusionMatrix(svm_linear_pred, test2$Chance.of.Admit)



# 커널 서포트 벡터 머신(비선형 서포트 벡터 머신)
svm_poly_fit <- train(Chance.of.Admit ~ .,
                        data=train2,
                        method="svmPoly",
                        trControl = ctrl,
                        preProcess = c("center", "scale"),
                        metric="Accuracy")

svm_poly_fit

# prediction
svm_poly_pred <- predict(svm_poly_fit, newdata = test)
confusionMatrix(svm_poly_pred, test2$Chance.of.Admit)



























