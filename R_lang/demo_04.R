# 데이터 프레임 만들기
# 역사 점수 생성
history <- c(50,10,60,90)
history

math <- c(50, 60, 100, 20)
math

# 변수를 합쳐서 데이터프레임 만들기
df_midterm <- data.frame(history, math)
df_midterm

# 변수 추가하기
class <- c(1,1,2,2)
class

df_midterm <- data.frame(history, math, class)
df_midterm

# 역사 평균점수
mean(df_midterm$history)

# 수학 평균점수
mean(df_midterm$math)


install.packages("readxl")
library(readxl)


df_finalexam <- read_excel("finalexam.xlsx", sheet=1, col_names = T)
df_finalexam

mean(df_finalexam$math)
mean(df_finalexam$history)
mean(df_finalexam$english)

df_finalexam <- read_excel("finalexam.xlsx", sheet=1, col_names = F)
df_finalexam

write.csv(df_finalexam, file = "output_newdata.csv")



