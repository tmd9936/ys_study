## 함수

aa <- c(1,2,3,4)

mean(aa)
max(aa)
min(aa)

bb <- c("a","a","b","c")
bb
qplot(bb) # 빈도 그래프 만들기기

# 문자 처리함수
cc <- c("Hello", "World", "good", "nice")
paste(cc, collapse = " ") # 빈칸 구분자로 문자를 붙이기
cc_paste <- paste(cc, collapse = " ")
cc_paste

cc2_paste <- paste(cc, collapse = ",")
cc2_paste

## 패키지(packages) = 함수 + 데어터 꾸러미
# 함수를 사용하려면 반드시!!
# 패키지를 설치(install) & 로드(library)
# Rstudio 실행할 때마다 한 번 설치된 패키지는 로드를 해줘야 한다.
# 단, 내장한수는 설치&로드가 필요없음음(min, max, mean...)
# 필요한 기능에 맞게 어플을 설치하듯이 패키지를 설치하면된다.
# 패키지들은 수시로 업데이트 된다.
# e.g) ggplot2 : 시각화 패키지(qplot, geom_line, ... 포함)

# 이러한 패키지들은 CRAN에 등록되어 있음.
# 15000여개의 패키지들이 있고, 누구나 만들어 등록할 수 있다.

qplot(bb)
head(mpg)

# 함수 파라미터(parameter) 지정하기 
qplot(data = mpg, x = hwy)
qplot(data = mpg, x = cty)
qplot(data = mpg, y = hwy, x=drv, geom = "point")
qplot(data = mpg, y = hwy, x=drv, geom = "boxplot", colour=drv)

# help에 있는 메뉴얼 참조하기기
?qplot

qplot(mpg, wt, data = mtcars)
qplot(mpg, wt, data = mtcars, colour = cyl)
qplot(mpg, wt, data = mtcars, size = cyl)
qplot(mpg, wt, data = mtcars, facets = vs ~ am)


rnorm(10)

qplot(1:10, rnorm(10), colour = runif(10))



