install.packages("rjava")
install.packages("memoise")
install.packages("KoNLP")

install.packages("vctrs")

install.packages("rlang")

koinstall = c('rJava', 'stringr','hash','tau','Sejong', 'RSOLite', ' devtools', 'vctrs')
install.packages(koinstall)
install.packages("remotes")

remotes::install_github('haven-jeon/KoNLP', upgrade="never", INSTALL_opts = c("--no-multiarch"))



library(rJava)
library(stringr)

library(KoNLP)


useSejongDic()

extractNoun("롯데마트 판매하")

txt <- readLines("hiphop.txt")
txt <- str_replace_all(txt,"\\W", " ")

nouns <- extractNoun(txt)
nouns

wordCount <- table(unlist(nouns))

wordCount

df_word <- as.data.frame(wordCount, stringsAsFactors = F)
df_word

library(dplyr)

df_word <- rename(df_word, word = Var1, freq = Freq)
df_word <- filter(df_word, nchar(word) >= 2)

top_20 <- df_word %>% arrange(desc(freq)) %>% head(20)
top_20

install.packages("wordcloud")
library(wordcloud)

library(RColorBrewer)
set.seed(100)

pal <- brewer.pal(9, "Set1")

word <- c("인천광역시", "서울시", "대구시")
word
freq <- c(700, 80, 30)
wordcloud(word, freq, colors = pal, rot.per = .1)
wordcloud(c)

##########################3
library(KoNLP)
library(RColorBrewer)
library(wordcloud)
library(dplyr)

useSejongDic()

pal <- brewer.pal(8, "Dark2")

text <- readLines(file.choose(), encoding="UTF-8")
text

# 각 행별로 명사를 추출
# sapply() : 결과를 벡터나 행렬로 리턴됨.
# USE.NAMES 행을 보이게 할건지 지정하는 옵션
noun <- sapply(text, extractNoun, USE.NAMES = T)

noun

noun2 <- unlist(noun)
noun2

word_count <- table(noun2)
word_count

df <- as.data.frame(word_count, stringsAsFactors = F)

df <- rename(df, word = noun2, freq = Freq)

df <- filter(df, nchar(word) > 1)

top_20 <- df %>% 
  arrange(desc(freq)) %>% 
  head(20)

top_20

wordcloud(word = df$word, 
          freq = df$freq, 
          min.freq = 2,
          max.words = 200,
          random.order = F,
          colors = pal, 
          rot.per = .5,
          scale = c(10, 1))


library(ggplot2)
order <- arrange(top_20, freq)$word
order

ggplot(data=top_20,
  aes(x = word, y= freq)) +
  ylim(0, 50) +
  geom_col() +
  scale_x_discrete(limit = order) +
  geom_text(aes(label = freq), hjust = -0.3) +
  coord_flip()

ggplot(data=top_20,
  aes(x = word, y= freq)) +
  ylim(0, 50) +
  geom_col() +
  scale_x_discrete(limit = order) +
  geom_text(aes(label = freq), vjust = -1)
        

########################################
# 단계 구분도(지역별 통계치)

install.packages("mapproj")
install.packages("ggiraphExtra")
library(ggiraphExtra)

data() # USArrests : 주별 강력 범죄율 정보

str(USArrests) # UrbanPop(도시 인구)
head(USArrests)
library(dplyr)

library(tibble)

# 행의 이름을 state 변수로 바꿔서 새로운 데이터 프레임을 만듦
crime <- rownames_to_column(USArrests, var="state")
# state의 모든 문자를 소문자로 변경
crime$state <- tolower(crime$state)
crime
str(crime)

# 미국의 위/경도 정보가 있는 지도 데이터터
install.packages("maps")
library(ggplot2)
states_map <- map_data("state")
str(states_map)

ggChoropleth(data = crime, 
             aes(fill = Rape, map_id = state), 
             map = states_map,
             interactive = T)
