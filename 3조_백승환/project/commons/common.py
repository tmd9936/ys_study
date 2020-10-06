import random
from string import digits, ascii_lowercase, ascii_uppercase
from .constant import ALLOWED_EXTENSIONS


# 파일이 유효한지 체크하는 함수
def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1] in ALLOWED_EXTENSIONS

# 파일명을 random하게 생성해주는 함수
def rand_generator(length=8):
    char = ascii_lowercase + ascii_uppercase + digits
    return "".join(random.sample(char, length))