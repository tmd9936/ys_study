## 그래프
# 산점도 : 변수간의 관계 표현

install.packages("forcats")
library(forcats)
library(ggplot2)
# 배경 레이어 생성 (첫 번째 레이어)
ggplot(data = mpg, aes(x=displ, y=hwy))

# 그래프 모양 추가(두 번째 레이어)
# geom_point은 두변수의 관계를를 점으로 표현하겠다
ggplot(data = mpg, aes(x=displ, y=hwy)) + geom_point()

# 그래프의 옵션을 추가(세번째 레이어)
#xlim(xlimit) x축의 범위를 지정
ggplot(data = mpg, aes(x=displ, y=hwy)) + geom_point() + xlim(3, 6) + ylim(10,30)

idwest <-  as.data.frame(ggplot2::midwest)

ggplot(data = midwest ,aes(x=poptotal, y =popasian)) + geom_point()

ggplot(data = midwest, aes(x = poptotal, y= popasian)) + geom_point() +xlim(0,500000) + ylim(0, 10000)

# 막대 그래프 - 집단간의 차이를 비교
library(dplyr)
# 평균표 만들기
df_mpg <- mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))

ggplot(data = df_mpg, aes(x = reorder(drv, -mean_hwy), y = mean_hwy)) + geom_col()

# 빈도 막대 그래프
# 값의 갯수(빈도)로 막대의 길이를 표현
# x축의 변수 : 범주형 변수
ggplot(data = mpg, aes(x = drv)) + geom_bar()

# x축의 변수가 : 연속변수

suv_mpg <- mpg %>% 
  filter(class=="suv") %>% 
  group_by(manufacturer) %>% 
  summarise(cty_mean = mean(cty)) %>% 
  arrange(desc(cty_mean)) %>% 
  head(5)

count_mpg <- mpg %>% 
  group_by(class) %>% 
  summarise(class_cnt = count(mpg,class))

cl_cnt = count(mpg,class)
ggplot(data=cl_cnt, aes(x=class, y=n)) + geom_bar()

?reorder 
?aes

suv_mpg

ggplot(data=suv_mpg, aes(x = reorder(manufacturer, -cty_mean), y=cty_mean)) + geom_col()

ggplot(data=mpg, aes(x=forcats::fct_infreq(class))) + geom_bar()
ggplot(data=mpg, aes(x=class)) + geom_bar()

ggplot(data=economics, aes(x=date, y=unemploy)) + geom_line()

ggplot(data=economics, aes(x=date, psavert)) + geom_line()

# boxplot(상자 그래프) : 집단의 데이터 특성들을 알아 볼 수 있는 그래프
# 박스의 크기가 작으면 그만큼 거기에 몰려있다는 의미
# 박스의 크기가 크면 다양하게 분포되어 있다는 의미
# 박스안의 선은 중앙값의 위치를 나타냄
# IQR <= 상자의 높이
# 각 1사분위수 or 3사분위수에 1.5IQR을 더한 수를 벗어난 값은 극단치로, 상자밖 점으로 표시됨
ggplot(data =mpg, aes(x=drv, y=hwy)) + geom_boxplot()
cl_mpg <- mpg %>% 
  filter(class==c("compact","subcompact","suv"))

ggplot(data=cl_mpg, aes(x=class, y=cty)) + geom_boxplot()




