library(jpeg)

image <- readJPEG('dog.jpg')
class(image)

dim(image)
img_dim <- as.vector(dim(image))
head(img_dim)

# rep()
# 1~3 까지 3번 반복
rep(1:3, times=3)
# 1을 3번 2를3번 3을 3번
rep(1:3, each=3)
# 1을 3번 2를3번 3을 3번 한거를 3번 반복
rep(1:3, each=3, time=3)

rep(1:img_dim[2], each = img_dim[1])
rep(img_dim[1]:1, each = img_dim[2])

# 3차원 데이터를 2차원으로 펼침
# img_dim = 431 540   3
# x는 1~540번까지 각각 431번 반복
# y는 431~1번까지 각각 540번 반복

# img_RGB <- data.frame(R=as.vector(image[,,1]), G=as.vector(image[,,2]), B=as.vector(image[,,3]))

img_RGB <- data.frame(
  x = rep(1:img_dim[2], each = img_dim[1]),
  y = rep(img_dim[1]:1, each = img_dim[2]),
  R = as.vector(image[,,1]),
  G = as.vector(image[,,2]),
  B = as.vector(image[,,3])
  
)

img_RGB
tail(img_RGB)

# 컬러축소하기 위한 클러스터 개수 설정
k_cluster <- c(3, 5, 10, 15, 30, 50)

set.seed(2020)


# 2차원 데이터인 img_RGB에서 RGB데이터로 kmenas 함수를 이용하여 모델을 생성
# img_result는 각 클러스터에 해당하는 평균값
# img_array는 원래의 dimension값으로 넣어 만든 array
for(i in k_cluster) {
  img_kmeans <- kmeans(img_RGB[,c("R","G","B")], centers = i)
  img_result <- img_kmeans$centers[img_kmeans$cluster,]
  img_array <- array(img_result, dim(image))
  writeJPEG(img_array, paste('km_', i, 'clusters.jpg', sep = ''))
}

img_kmeans$cluster
img_kmeans$centers
img_kmeans$centers[1,]
img_result

dim(img_array)











