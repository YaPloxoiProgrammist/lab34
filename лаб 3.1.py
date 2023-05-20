if __name__ == '__main__':

    A = int(input('Введите значение стороны A '))
    B = int(input('Введите значение стороны B '))
    C = int(input('Введите значение стороны C '))

    def triangle(A, B, C):
        if A + B > C and A + C > B and C + B > A:
            print('Можно')
        else:
            print('Нельзя')

triangle(A, B, C)