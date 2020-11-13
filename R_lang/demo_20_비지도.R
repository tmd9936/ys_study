# 데이터 파악하기
# sepal 꽃받침
# petal 꽃잎
# Species 품좀
iris

head(iris)
str(iris)

# 각컬럼의 합계
colSums(is.na(iris))

summary(iris)

boxplot(iris)

## 주성분 분석하기
# prcomp 함수 적용하기(평균:0, 분산:1)
iris.pca <- prcomp(iris[1:4], center = T, scale=T)
iris.pca


# stadard deciation 표준편차 주성분이 갖는 값
# proportion of variance (eigenvalue) 분산비율 (모든 값 다 더하면 1)
# Cumulative Proportion 분산의 누적 비율

# 분석, 결과치 확인 및 해석
# Standard deviation (표준 편차)의 제곱 = 분산 = eigenvalue
# Proportion of Variance : 각 주성분이 차지하는 분산 비율
# Cumulative Proportion : 분산의 누적 비율
summary(iris.pca)


# eigenvector(고유벡터)
# 어떤 변수들이 중요한지를 eigenvetor를 통해서 알 수 있음
# -> 값은 각 피처가 벡터를 만든 가중치
iris.pca$rotation

# 차원 축소를 했을때 각 변수가 갖는 값
# 새로운 축에서 그 데이터들이 갖는 값 (각 주성분들의 값)
head(iris.pca$x, 10)

# scrre plot 확인(주성분의 개수를 선택하기 위해 scree plot을 그린다.)
# 주성분 개수를 선택하는 기준
# 1. 시각화를 위해서는 주성분 개수가 2, 3개 선택
# 2. eigenvalue > 1을 선택
# 3. elbow포인트 선택

plot(iris.pca, type='l', main = 'Scree plot')

# 2개의 차원으로 축소
head(iris.pca$x[,1:2], 10)

# 2차원 시각화
install.packages("ggfortify")
library(ggfortify)
autoplot(iris.pca, data=iris, colour='Species')

#######

rawdata1 <- read.csv("financial_marketing.csv", header = T)

# unknown -> NA
rawdata1[rawdata1 =="unknown"] <- NA

# na로 바꾸기
sum(is.na(rawdata1))

# na omit -> na 데이터 지우기
rawdata1 <- na.omit(rawdata1)
rawdata1 <- data.frame(rawdata1)

rawdata$age <- scale(rawdata$age)
rawdata$duration <- scale(rawdata$duration)
rawdata$campaign <- scale(rawdata$campaign)
rawdata$previous <- scale(rawdata$previous)
rawdata$emp.var.rate <- scale(rawdata$emp.var.rate)
rawdata$cons.price.idx <- scale(rawdata$cons.price.idx)
rawdata$cons.conf.idx <- scale(rawdata$cons.conf.idx)
rawdata$euribor3m <- scale(rawdata$euribor3m)
rawdata$nr.employed <- scale(rawdata$nr.employed)

num_feature <- c("age", "duration", "campaign", "previous", "emp.var.rate", "cons.price.idx","cons.conf.idx", "euribor3m", "nr.employed")

num_data <- rawdata1[, num_feature]
pca_num <- prcomp(num_data)
plot(pca_num, type="l", main="Principle Component Analysis")

summary(pca_num)

pca_matrix <- pca_num$rotation

pca_data <- as.matrix(num_data) %*% pca_matrix
dim(pca_data)

# pca_matrix
# as.matrix(num_data)

library(ggfortify)
autoplot(pca_num, data=rawdata1, colour='target')

#####################
tar <- rawdata1[ , "target"]
reduced_data <- data.frame(cbind(pca_num$x[,1:3], tar))
reduced_data$tar <- as.factor(reduced_data$tar)
str(reduced_data)

library(ggplot2)
ggplot(data = reduced_data, aes(x=PC1, y =PC2)) + geom_point(aes(color=tar, shape=tar)) + xlab("PC1") + ylab("PC2")+ggtitle("PCA DATA")



























