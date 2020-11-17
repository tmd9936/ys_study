# 주석처리

# 패키지 설치
install.packages("dplyr")
install.packages("ggplot2")

# 패키지 로드
library(dplyr)
library(ggplot2)

# 데이터 파악(앞부분 일부 출력해보기)
head(mpg)

# 뒷부분 출력
tail(mpg)

#데이터의 크기
dim(mpg)

# 어떤 열(변수, 속성, 필드(db))들이 있는지 확인
str(mpg)

# 통계 수치를 요약해서 출력하기기
summary(mpg)

# Raw(원본) 데이터를 살펴보고자 할 때
View(mpg) # 많이 사용되지는 않는다.

# 위의 데이터를 파악함으로써 통계 분석을 할 수 있음
# 통계적 테이터분석

# 1.회사별 평균 연비(정렬)
mpg %>%
  group_by(manufacturer) %>%
  summarise(mean.hwy=mean(hwy)) %>%
  arrange(desc(mean.hwy))

# 2. 포드사의 연비 확인
mpg %>%
  filter(manufacturer=="ford") %>%
  group_by(model) %>%
  arrange(desc(hwy))

# 3. 배기량이 연비에 미치는 영향(회귀분석)
lm.mpg <- lm(data=mpg, hwy~displ)

# 회귀분석
summary(lm.mpg)

# 시각화
qplot(data=mpg, x= displ, y = hwy)

# 선을 그리고 그 선을 통해 들어올 데이터의 값을 예측(회귀분석)
# 데이터가 많을 수록 오차율이 적을 수록 정확한 예측분석이 가능하다.




