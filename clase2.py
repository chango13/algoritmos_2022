

def factorial_iterativa(num):
    factorial = 1
    for n in range(2, num+1):
        factorial = factorial * n
    
    return factorial

def factorial_recursivo(num):
    if(num == 0):
        # print('se alcanzo condicion de fin')
        return 1
    else:
        # print('antes de la llamada recursiva num:', num)
        # value = num * factorial_recursivo(num-1)
        # print('despues de la llamada recursiva num:', value)
        # return value
        return num * factorial_recursivo(num-1)


def fib_iter(num):
    val1 = 0
    val2 = 1
    for n in range(2, num+1):
        resultado = val1 + val2
        val1 = val2
        val2 = resultado
    return resultado


def fib_rec(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fib_rec(num-1) + fib_rec(num-2)

# print(factorial_recursivo(5))
# print(factorial_iterativa(5))


for i in range(0, 11):
    print('fibanacci ', i, fib_rec(i))




