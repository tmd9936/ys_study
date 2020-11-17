# 관객수 기준 역재 박스오피스
# http:www.kobis.or.kr

library(readxl)
movies <- read_excel("movies.xlsx")
movies

## 데이터 파악하기기

head(movies)
tail(movies)
names(movies)
dim(movies)
summary(movies)

max(movies$매출액)
max(movies$관객수)
max(movies$상영횟수)

# 행의 번호
which.max(movies$관객수)
movies[64, ]

which.min(movies$스크린수)
movies[60, ]


# histogram

movies$관객수

hist(movies$관객수)

library(ggplot2)

ggplot(data = movies, aes(x = 관객수)) + geom_histogram()

## 관객수 상영 횟수
gp <- ggplot(data = movies, aes(x = 관객수, y=상영횟수, col=대표국적)) + geom_point()

install.packages("plotly")
library(plotly)
ggplotly(gp)


# 상영횟수당 관객수가 가장 많은 영화 찾기
movies2 <- movies %>% 
  mutate(상영대비관객 = 관객수/상영횟수)

which.max(movies$상영횟수)
movies[126,]

which.max(movies$관객수/movies$상영횟수)
movies[21,]

movies2 %>% 
  arrange(desc(상영대비관객)) %>% 
  head(10)

sort(movies$관객수 / movies$상영횟수, decreasing = T) # decreasing 기본값 f

movies %>% 
  mutate(상영대비관객 = 관객수/상영횟수) %>% 
  arrange(desc(상영대비관객)) %>% 
  head(10)




















