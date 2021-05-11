import re

def main():
    address_book = {}

    try:
        with open("./friendData.txt","r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                raw = line.split(',')
                print('raw', raw)
                info = [raw[1], re.sub("\n","",raw[2])]
                address_book[raw[0]] = info

    except FileNotFoundError as e:
            print("파일이 존재하지 않습니다...", e)

    while True:
        user = display_menu()
        if user == 1:
            name, number, add, email = get_contact()
            info = [number, add, email]
            address_book[name] = info

        elif user == 2:
            name = input("삭제할 이름 입력 : ")
            address_book.pop(name)

        elif user == 3:
            key = input("검색할 이름 입력 : ")
            if address_book.get(key) is None:
                print("저장되지 않은 이름입니다.")
            else:
                info = address_book.get(key)
                print(key, "의 전화번호 : ",info[0])
                print(key, "의 주소 : ", info[1])
                print(key, "의 이메일 : ", info[2])

        elif user == 4:
            for key in sorted(address_book):
                info = address_book.get(key)
                print(key, "의 전화번호 : ", info[0],key, "의 주소 : ", info[1],key, "의 이메일 : ", info[2],)

        else:
            with open("./friendData.txt", "w") as f:
                for key in address_book:
                    f.write(key + ',')
                    f.write(address_book[key][0] + ',')
                    f.write(address_book[key][1] + ',')
                    f.write(address_book[key][2] + ',')
                    f.close()
                print("파일을 저장하고 종료합니다.")
                break

def get_contact():
    name = input("이름 : ")
    number = input("전화번호 :")
    add = input("주소 : ")
    email = input("이메일 : ")
    return (name, number, add, email)

def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

if __name__ == '__main__':
    main()