# @ 의사결정 트리
# 패키지 설치
# 기본트리 확인
# cross-validation
# 가지치기
# 예측



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

# Decision Tree 학습
install.packages("tree")
library(tree)

treeRaw <- tree(Class~.,
                data=train)

plot(treeRaw)
text(treeRaw)

# 가장 적합한 사이즈 찾기(Tree Size)
# prune.misclass : 오분류율이 많은 값을 기준으로 가지치기를 함
cv_tree <- cv.tree(treeRaw, FUN = prune.misclass)
plot(cv_tree)

# 가지치기(가지가 너무 많으면 성능상의 문제)
# best값은 cv에서 측정된 값을 적용
prune_tree <- prune.misclass(treeRaw,best = 4)

plot(prune_tree)
text(prune_tree, pretty = 0)

pred <- predict(prune_tree, test, type='class')
confusionMatrix(pred, test$Class)

# 학습된 데이터로 테스트를 하면 정확도가 높은데
# 테스트데이터인 경우 정확도가 낮음
# -> 오버핏이 다른 학습알고리즘 보다 더 크게 발생함

# Random Forest 학습
ctrl <- trainControl(method="repeatedcv", repeats = 5)
rfFit <- train(Class ~.,
               data=train,
               method="rf",
               trControl = ctrl,
               preProcess = c("center", "scale"),
               metric="Accuracy")
rfFit

plot(rfFit)

# 정확도 테스트
pred_test <- predict(rfFit, newdata = test)
confusionMatrix(pred_test,test$Class)

# 변수의 중요도
importance_rf <- varImp(rfFit, scale=F)
plot(importance_rf)














