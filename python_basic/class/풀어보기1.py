class Book():
    def __init__(self, code, title, author, publisher):
        self.code = code
        self.title = title
        self.author = author
        self.publisher = publisher

    def info(self):
        print('code : {} title: {} author: {} publisher: {}'.
            format(self.code, self.title, self.author, self.publisher))
    


def set_info():
    code = input('도서 코드 : ')
    title = input('도서명 : ')
    author = input('저자 : ')
    publisher = input('출판사 : ')
    print()
    # print(code, title, author, publisher)
    return Book(code, title, author, publisher)

    

def print_book_info(book_list):
    for book in book_list:
        book.info()

def menu_display():
    print('-------------------')
    print('1. 도서 정보 입력')
    print('2. 도서 출력')
    print('3. 도서 삭제')
    print('4. 종료')
    print('-------------------')

    return int(input())

def delete_menu_display():
    print('-------------------')
    print('1. 도서 인덱스로 삭제')
    print('2. 도서명으로 삭제')
    print('-------------------')
    
    return int(input())

def delete_by_index(book_list):
    book_num = int(input('도서 번호 : '))
    if book_num >= 0 and book_num < len(book_list):
        del book_list[book_num]
        print('삭제됐습니다')
    else:
        print('잘못된 번호')

    return book_list

def repo_book(book_list):
    with open('./book_db.txt', 'w', encoding='utf8') as f:
        for book in book_list:
            f.write(book.code + '\n')
            f.write(book.title + '\n')
            f.write(book.author + '\n')
            f.write(book.publisher + '\n')

def load_book(book_list):
    with open('./book_db.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        num = int(len(lines)/4)

        for i in range(num):
            code = lines[4*i].strip()
            title = lines[4*i+1].strip()
            author = lines[4*i+2].strip()
            publisher = lines[4*i+3].strip()
            book = Book(code, title, author, publisher)
            book_list.append(book)

def delete_by_title(book_list):
    title = input('도서 제목 : ')

    for i, book in enumerate(book_list):
        if book.title == title:
            del book_list[i]
    
    return book_list

def run():
    book_list = []
    load_book(book_list)

    while True:
        menu_num = menu_display()

        if menu_num == 1:
            book_list.append(set_info())
        elif menu_num == 2:
            print_book_info(book_list)
        elif menu_num == 3:
            d_menu_num = delete_menu_display()          
            if d_menu_num == 1:
                delete_by_index(book_list)
            elif d_menu_num == 2:
                delete_by_title(book_list)
            else:
                print('잘못된 번호')
        elif menu_num == 4:
            repo_book(book_list)
            print('종료합니다.')
            break
        else:
            print('없는 메뉴')


if __name__ == '__main__':
    run()
