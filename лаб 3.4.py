if __name__ == '__main__':
    value = 1
    addition = 2
    value = value + addition
    print(value)
    value = 1
    addition = 2
    value += addition
    print(value)

    value = '1'
    addition = '2'
    value = value + addition
    print(value)
    value = '1'
    addition = '2'
    value += addition
    print(value)


    class A(object):
        def __init__(self, v):
            self.v = v

        def __add__(self, a):
            self.v += a.v
            return self

        def __iadd__(self, a):
            self.v -= a.v
            return self

        def __str__(self):
            return str(self.v)


    value = A(1)
    addition = A(2)
    value = value + addition
    print(value)
    value = A(1)
    addition = A(2)
    value += addition
    print(value)