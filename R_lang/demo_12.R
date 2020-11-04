## 가설 검정 연습하기

rawN <- read.csv(file="data/htest01.csv", header = T)

# group이 A인 데이터, 1~2열 가져옴
groupA <- rawN[rawN$group == 'A',1:2]
groupA
groupB <- rawN[rawN$group == 'B', 1:2]

# 두 번째 행의 평균
mean(groupA[,2])
mean(groupB[,2])

## 가설설정
# 귀무가설 : 그룹A와 그룹B간의 평균키 차이는 없다.
# 대립가설 : 그룹A보다 그룹B의 평균키가 크다.

## T-test 과정
# 데이터 정규성 검정

# 샘플사이즈 < 30 => t검정 30개 넘으면 z검정
# 각집단의 샘플 사이즈 = 3(정규성 검정 : A집단)
# shapiro.test() 함수를 이용해서 검정한다.
# p-value가 0.05보다 크면 정규성을 따르고 아니면 안 따름
# 0.05는 평균적으로 쓰는 기각역(기준값)
shapiro.test(groupA[,2])
qqnorm(groupA[,2])
qqline(groupA[,2])


shapiro.test(groupB[,2])
qqnorm(groupB[,2])
qqline(groupB[,2])

# 분산의 동질성 검정
# 귀무가설 : 두 집단간 분산차이가 없다.
# 대립가설 : 두 집단간 분산차이가 있다.

var.test(groupA[,2], groupB[,2])
# 위의 결과 p-value = 0.5385이므로 귀무가설을 채택한다
# p-value가 0.05를 안넘으면 분산이 같은거로 생각


## T-test
# alternavtive 대립가설, less 왼쪽이 오른쪽 보다 작다
# var.equal 분산이 동일한가?
t.test(groupA[,2], groupB[,2], alternative = "less", var.equal = T)


## 결론 
# p-value = 0.1154이므로 귀무가설 채택
# 귀무가설 채택 : 그룹A와 그룹B간 평균 키차이가 없다.

##############################################################################
#htest02.csv 데이터를 이용하여 그룹간 평균
#키차이를 비교하는 t검정을 하여 결론을 내시오

da = read.csv(file = "data/htest02.csv", header = T)
da
dataA <- da[da$group == 'A', 1:2]
mean(dataA$height)
dataB <- da[da$group == 'B', 1:2]
mean(dataB$height)


# 1.가설설정
# 귀무가설 : A와 B의 평균키는같다
# 대립가설 : B의 평균키가 A보다 크다

# 샘플사이즈가 30미만이기 때문에 t테스트 검정

# 2. 데이터 정규성 검정
# 귀무가설 : A와 B가 정규데이터 분포를 따른다
# 대립가설 : A와 B가 정규데이터 분포를 따르지 않는다.
shapiro.test(dataA$height)
qqnorm(dataA$height)
qqline(dataA$height)

shapiro.test(dataB$height)
qqnorm(dataB$height)
qqline(dataB$height)

# 결과 : 둘다 p-value가 기각역0.05를 넘기 때문에 따른다고 봄

# 3. 분산 동질성 검정
# 귀무가설 : 두 집단간 분산차이가 없다.
# 대립가설 : 두 집단간 분산차이가 있다.

var.test(dataA$height, dataB$height)
# p-value가 기각역0.05를 못 넘었기 때문에 대립가설을 채택함

# 4. T-test
t.test(dataB$height, dataA$height, alternative = "greater", var.equal = F)

# 5. 결론
# p-value : 0.01912 귀무가설 기각, 대립가설 채택
# 대립가설 : B집단의 평균이 A집단보다 크다


#6. htest01.csv를 이용한 결과와 비교해보세요


######################################
dat = read.csv("data/htest03.csv")
dat

datA = dat[dat$group == 'A', 1:2]

datB = dat[dat$group == 'B', 1:2]

mean(datA$height)
mean(datB$height)


shapiro.test(datA$height)
shapiro.test(datB$height)


var.test(datA$height, datB$height)

t.test(datA$height, datB$height, alternative = "less", var.equal = T)





























