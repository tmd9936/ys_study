### 대응 표본 T 검정
# 데이터는 마케팅 전후의 판매액이라고 가정하자.
raw_d <- read.csv(file = "data/htest02d.csv", header = T)
head(raw_d)
dim(raw_d)

groupA_d <- raw_d[,1]
groupB_d <- raw_d[,2]


mean(groupA_d)
mean(groupB_d)

#### 가설 설정
# 귀무가설 : 마케팅을 통해서 판매액의 변화(차이)가 없다.
# 대립가설 : 마케팅을 통해서 판매액이 증가했다.

#### 데이터 정규성 검정
d = groupA_d - groupB_d

shapiro.test(d)
# -> p-value가 0.1621 > 0.05이기때문에 정규분포를 따름
qqnorm(d)
qqline(d)

#### 집단 1개만가지고 태스트하는 것이라서 분산동질성 검정은 하지 않음

#### 대응표본 t검정
# paired = T는 대응표본
t.test(groupA_d, groupB_d, alternative = "less", paired = T)

# p-value가 0.006745 < 0.05이므로 대립가설을 채택함
# 결론 : 마케팅을 통해서 판매액이 증가했다.

##################################################################
#### z검정

rawN30 = read.csv("data/htest03.csv", header = T)
head(rawN30)
tail(rawN30)
dim(rawN30)
names(rawN30)
groupA3 <- rawN30[rawN30$group == 'A', 1:2]
groupA3

groupB3 <- rawN30[rawN30$group == 'B', 1:2]
groupB3

mean(groupA3$height)
mean(groupB3$height)

## 귀무가설 : 그룹 A와 B의 평균키는 같다.
## 대립가설 : 그룹 B의 평균키가 그룹A의 평균키보다 크다.

z.test <- function(x1,x2){
  n_x1 = length(x1)
  n_x2 = length(x2)
  mean_x1 = mean(x1)
  mean_x2 = mean(x2)
  
  cat("\n")
  cat("\tTwo Sample z-test\n")
  cat("\n")
  cat("mean of x1:", mean_x1, "\n")
  cat("mean of x2:", mean_x2, "\n")
  var_x1 = var(x1)
  var_x2 = var(x2)
  z = (mean_x1 - mean_x2)/sqrt((var_x1/n_x1)+(var_x2/n_x2))
  abs_z = abs(z)
  cat("z =", abs_z, "\n")
  p_value = 1-pnorm(abs_z)
  cat("p-value =", p_value)
}

z.test(groupA3$height, groupB3$height)

# p-value = 0.04866272 이므로 귀무가설을 기각

## 결론 : 그룹B의 평균키가 그룹A의 평균키보다 크다.

# 위의 데이터를 t-test 했을 경우 (잘못된 분석석)
# 분산 동질성 검정정
var.test(groupA3$height, groupB3$height)

# conf.level : 신뢰구간(confidence interval)
t.test(groupA3$height, groupB3$height, alternative = "less", var.equal = T, conf.level = 0.95)
#결론 : p-value = 0.05136이르로 귀무가설 채택됨(차이가 없다.)


#####################################################
# ANOVA 분석 : 여러 집단의 평균차이 검정
# ANOVA 분석을 위해서는 lawstat 패키지가 핑요함
install.packages("lawstat")
library(lawstat)

raw_anova <- read.csv(file= "data/htest04.csv", header = T)
head(raw_anova)
tail(raw_anova)

groupA4 <- raw_anova[raw_anova$group=='A', 1:2]
groupB4 <- raw_anova[raw_anova$group=='B', 1:2]
groupC4 <- raw_anova[raw_anova$group=='C', 1:2]

mean(groupA4[,2])
mean(groupB4[,2])
mean(groupC4[,2])

## 가설 설정
# 귀무가설 : 세 집단간의 평균 차이가 없다.
# 대립가설 : 세 집단간의 평균 차이가 있다. (단측검정)
# 여러집단이기 때문에 단측검정을 하기가 어려움

# 정규성 검정
shapiro.test(groupA4[,2])
qqnorm(groupA4[,2])
qqline(groupA4[,2])

shapiro.test(groupB4[,2])
qqnorm(groupB4[,2])
qqline(groupB4[,2])

shapiro.test(groupC4[,2])
qqnorm(groupC4[,2])
qqline(groupC4[,2])


# 분산 동질성 검정
# ANOVA 검정에서는 var함수 대신에 levene, bartlett 함수를 이용한다.

levene.test(raw_anova$height, raw_anova$group)
# p-value = 0.3298이므로 분산이 동일하다.

bartlett.test(height~group, data=raw_anova)
# p-value = 0.3435이므로 세집단간의 분산이 동일하다.
rawAnova <- aov(height ~ group, data= raw_anova)
summary(rawAnova)

# Pr(>F) 가 1.14e-05(0.000014)이므로 대립가설 채택
# 658.4 -> 집단간 오차
# 36.2 -> 집단내 오차

# 결론 : 세 집단간 평균차이가 있다.


###########################################
# 분할표를 이용한 연관성 분석
raw_chisq <- read.csv(file="data/htest05.csv", header = T)
raw_Table <- table(raw_chisq)
raw_Table

head(raw_chisq)
tail(raw_chisq)

#### 가설설정
# 귀무가설 : 흡연 여부와 폐암유무는 연관성이 없다.
# 대립가설 : 흡연 여부와 폐암유무는 연관성이 있다.

# 카이제곱 테스트
# 셀기대도수 > 5인 경우 : correct = FALSE
# 셀기대도수 < 5인 경우 : correct = TRUE
# 일반적으로 기대도수가 5이상이라고 생각하고 검정을 한다.
chisq.test(raw_Table, correct = FALSE)


# 결론 : p-value = 0.02686이므로 대립가설 채택









































