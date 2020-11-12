## classification(분류)으로 합격 여부 예측하기

# target 값 --> 명목형(범주형) --> 분류(classification)
# target 값 --> 연속형 숫자 --> 회귀(Regression)

# 합격여부 판단을 위한 기준점 
library(caret)

rawdata2 <- read.csv("university.csv", header = T)

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
logit_pf <- train(Chance.of.Admit ~ .,
                  data=train2,
                  method="knn",
                  trControl=ctrl,
                  preProcess = c("center", "scale"),
                  tuneGrid = customGrid,
                  metric="Accuracy")

logit_pf

plot(logit_pf)

# 예측
pred_test <- predict(logit_pf, newdata = test2)
confusionMatrix(pred_test, test2$Chance.of.Admit)

importance_nb <- varImp(nbFit, scale=F)
plot(importance_nb)


















