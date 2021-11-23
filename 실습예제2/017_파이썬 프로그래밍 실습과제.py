
# a = input('정수1 : ')
# b = input('정수2 : ')
# c = int(a)+int(b)
# print(f'합은 : {c} 입니다.')

# a = input('first number: ')
# b = input('second number: ')
# c = int(a)+int(b)
# print(f'add: {c}')
# d = int(a)-int(b)
# print(f'sub: {d}')
# e = int(a)*int(b)
# print(f'mul: {e}')
# f = int(a)/int(b)
# print(f'div: {f}')

def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])  # 튜플로 리턴

if __name__ == '__main__':
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)