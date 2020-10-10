L0 = []
L1 = []
L2 = list('abc')
L3 = list('def')
L4 = list('ghi')
L5 = list('jkl')
L6 = list('mno')
L7 = list('pqrs')
L8 = list('tuv')
L9 = list('wxyz')
sum = [L0,L1,L2,L3,L4,L5,L6,L7,L8,L9]
print('请输入0到99的整数')
input=input()
if 0<=eval(input)<10:
    for _ in sum[eval(input)]:
        print(_,end=' ')
elif 10 <= eval(input)<100:
    for i in sum[eval(input[0])]:
        for j in sum[eval(input[1])]:
            print(i+j,end=' ')
else:
    print('error')



