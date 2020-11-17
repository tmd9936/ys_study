df <- read.csv("customers_data.csv", stringsAsFactors = F, header = T)

library(dplyr)

# 도매시작에 고객들이 연간 물건을 얼마나 구매했는지를 정리한 데이터 
head(df)

# channel : 유통채널, fresh:신선식품, milk : 유제품, Frozen : 냉동식품
# Grocery: 채소류, Region : 지역, Detergents_paper : 세제, 제지

dim(df)
str(df)

# 범주형 확인
unique(df$Channel)
unique(df$Region)

df$Channel <- as.factor(df$Channel)
df$Region <- as.factor(df$Region)

# 결측치 확인
colSums(is.na(df))
table(is.na(df))

# 기술 통계량 확인
summary(df)

# scipen에 아무 양수를 넣으면 정수표현식으로 바뀜
## 양수 : 정수표현, 음수 : 과학적 표기법
options(scipen = 999)
# ncol() 컴럼의 갯수
boxplot(df[,3:ncol(df)])

# 이상치 제거
tmp <- NULL
for(i in 3:ncol(df)) {
  tmp <- rbind(tmp, df[order(df[,i], decreasing=T),] %>% slice(1:5))
}

# 복원추출을 통한 추출로 중복 발생
tmp %>% arrange(Fresh) %>% head()
boxplot(tmp)

# 중복제거
tmp <-distinct(tmp)

# anti.join(df,tmp)은 df에서 tmp를 제거
# 같은 것들을 찾아서 제거해주는 함수
rm_outlier_df <- anti_join(df, tmp)

# 이상치 제거 후 박스플롯 확인해보기
par(mfrow = c(1,2))
boxplot(df[,3:ncol(df)])
boxplot(rm_outlier_df[,3:ncol(df)])

dev.off()

# 클러스터의 개수(k 개수 선택)
# 군집 분석시 사용되는 패키지 factoextra
# install.packages('factoextra')
library(factoextra)

# Elobow Method
set.seed(2020)
fviz_nbclust(rm_outlier_df[,3:ncol(rm_outlier_df)], kmeans, method="wss", k.max = 15) +
  theme_classic() + ggtitle("Elbow Chart")

# silhouette Mehod
fviz_nbclust(rm_outlier_df[,3:ncol(rm_outlier_df)], kmeans, method="silhouette", k.max = 15) +
  theme_minimal() + ggtitle("silhouette Chart")

# 클러스터를 5개로 나누기 

# kmean() : kmean모델 생성
df_kmeans <- kmeans(rm_outlier_df[,3:ncol(rm_outlier_df)], center = 5
                    , iter.max = 10000)

# 결과 해석
df_kmeans
#############
# 각 클러스트의 사이즈
## K-means clustering with 3 clusters of sizes 100, 80, 241

# Cluster means:
# Fresh      Milk   Grocery   Frozen Detergents_Paper Delicassen
## 각 클러스터의 변수 별 평균값

# Clustering vector:
## 각 데이터(벡터)들이 몇번째 군집에 할당됐는지를 표시

#############
# centers는 각 그룹별 해당 컬럼의 평균값
df_kmeans$centers

df_kmeans$cluster

# 시각화
barplot(t(df_kmeans$centers), beside=T, col=1:6, )
legend("topright", colnames(df[3:8]), fill=1:6, cex = 0.6)

fviz_cluster(df_kmeans, data=rm_outlier_df[,3:ncol(rm_outlier_df)])

df_clustered <- data.frame(rm_outlier_df, cluster=factor(df_kmeans$cluster))
library(ggplot2)
ggplot(df_clustered, aes(x=Fresh, y= Grocery, color=cluster)) + geom_point()

head(rm_outlier_df)



























