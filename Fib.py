a = 0
b = 1

def Fib(a, b):
    result = a + b
    
    return (b, result)

tpl = Fib(a, b)
n = int(input('Введіть кількість чисел, яку ви бажаєте отримати:'))

for i in range(n):
    tpl = Fib(*tpl)
    print(tpl[1])

