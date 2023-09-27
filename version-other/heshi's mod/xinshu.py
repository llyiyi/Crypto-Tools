
#输入1时可以计算任意算式与任意算式的余数
#输入2时计算pow(a1,b1)模b1*b2的余数
choice=input('input choice\n')
if choice=='1':
    a = input('input a\n')
    ea = eval(a)
    print(ea)
    b = input('input b\n')
    eb = eval(b)
    print(eb)
    output = "a chu b=" + str(ea // eb) + '...' + str(ea % eb)
    print(output)
    input('hahaha')
else:
    if choice== '2':
        a1 = int(input('input a1\n'))
        a2 = int(input('input a2\n'))
        a = pow(a1, a2)
        print(a)
        b1 = int(input('input b1\n'))
        b2 = int(input('input b2\n'))
        b = b1 * b2
        print(b)
        output = "a chu b=" + str(a // b) + '...' + str(a % b)
        print(output)
        input('hahaha')
    else:
        print('wrong choice')



