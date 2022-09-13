def func(A, B):
    for i in range(len(A)):
        if A[i] == B[i]:
            print("P", end='')
        elif A[i] != B[i]:
            if A.count(B[i]) == B.count(B[i]) or A.count(B[i], 0, i) - B.count(B[i], 0, i) >= 1:
                print("S", end='')
            else:
                print("I", end='')
    print()


func('CLOUD', 'CUPID')
func('ALICE', 'ELIBO')
func('ABCBCYA', 'ZBBACAA')
func('CAAC', 'CACA')

print()

def main(a, b):
    res = ''
    n = len(b)
    for i in range(n):
        if b[i] == a[i]:
            res += 'P'

        elif b[i] != a[i]:
            if b[i] in a:
                res += 'S'
            else:
                res += 'I'
    return res


print(main('CLOUD', 'CUPID'))
print(main('ALICE', 'ELIBO'))
print(main('ABCBCYA', 'ZBBACAA'))
print(main('CAAC', 'CACA'))


def main(a, b):
    res = ['?'] * len(b) # массив с нужным размером
    ad = {}  # для подсчета количества букв
    bd = {}  # для подсчета количества букв
    for i in range(len(b)):
        if (b[i] == a[i]):
            res[i] = 'P'
        else: # считаем буквы в обоих словах
            bd[a[i]] = ( bd[a[i]] if a[i] in bd else 0 ) + 1
            ad[b[i]] = ( ad[b[i]] if b[i] in ad else 0 ) + 1

    for i in range(len(b)):
        if (res[i] == '?'):
            set_I_or_S(b[i], bd, i, res)
            set_I_or_S(b[i], ad, i, res)

    return ''.join(res)

def set_I_or_S(letter, dictionary, i, res):
    if (letter in dictionary and dictionary[letter] != 0):
        dictionary[letter] -= 1 # вычитаем букву из словаря
        # S если буква была в предыдущем словаре иначе I
        res[i] =  'I' if res[i] == '?' else 'S'

def test(a, b, c):
    res = main(a, b)
    compare = res == c
    print(res, compare)

test('CLOUD', 'CUPID', 'PSIIP')
test('ALICE', 'ELIBO', 'SPPII')
test('ABCBCYA', 'ZBBACAA', 'IPSSPIP')
test( 'CAAC','CACA','PPSS')