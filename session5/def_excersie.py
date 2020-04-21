#1번. 
def what():
    a = int(input("숫자를 하나 입력>>"))
    if a %2 ==0:
        print(f'{a}는 짝수입니다')
    else:
        print(f'{a}는 홀수입니다')
what()


#2번 내풀이. 
def gugu():
    b = int(input('숫자를 입력하세요>>'))
    if b %2 ==0:
        print('짝수구구단')
        for i in range(2,10,2):
            for j in range(1,10):
                print(f'{i}*{j}={i*j}')
    else:
        print('홀수구구단')
        for i in range(1,10,2):
            for j in range(1,10):
                print(f'{i}*{j}={i*j}')
gugu()

#2번 원하는식의 풀이.
def gugudan_even(e):
    print('짝수구구단')
    for i in range(2,10,2):
        for j in range(1,10):
            print(f'{i}*{j}={i*j}')

def gugudan_odd(o):
    print('홀수구구단')
    for i in range(1,10,2):
        for j in range(1,10):
            print(f'{i}*{j}={i*j}')

def whatgugu():
    c = int(input('아무 숫자나 입력>>'))
    if c%2 == 0:
        return gugudan_even(c)
    else:
        return gugudan_odd(c)

whatgugu()
