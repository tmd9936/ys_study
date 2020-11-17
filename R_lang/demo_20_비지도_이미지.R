install.packages("jpeg")
library(jpeg)

dog <- readJPEG('dog.jpg')

# array : 3차원
# 픽셀 : RGB값을 각각 갖고 있고 그게 가로x세로
class(dog)
str(dog)
head(dog)
dim(dog)

r <- dog[,,1]
g <- dog[,,2]
b <- dog[,,3]


# r,g,b각각 차원축소를 하고 합치기
dog.r.pca <- prcomp(r, center = F,)
dog.g.pca <- prcomp(g, center = F,)
dog.b.pca <- prcomp(b, center = F,)

rgb.pca <- list(dog.r.pca, dog.g.pca, dog.b.pca)

# 축소할 차원 수
pc <- c(2, 10, 50, 100, 300)


for(i in pc) {
  pca.img <- sapply(rgb.pca, function(j) {
    compressed.img <- j$x[,1:i] %*% t(j$rotation[,1:i])
  }, simplify = 'array')
  writeJPEG(pca.img, paste('dog_pca_',i,'.jpg', sep = ''))
}

# t는 transpose
# t()함수는 수학적으로 전치를 의미함, 행렬의 행과 열을 전치 ( 행->열, 열->행)
# sapply()함수는 rgb.pca 리스트 각각의 값에 funcion() 함수를 적용한뒤 array로 만들라는 의미

# %*%는 행렬곱(내적)을 의미하는 연산자




























