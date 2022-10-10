
def foo(P):
    P = sorted(P)
    Stack = []
    for i in P:
        print(not Stack)
        while(Stack and Stack[0][1] <= i[1]):
            Stack.pop()
        Stack.append(i)

    return Stack
print(foo([(2,1), (4,1), (6,1), (2,2), (3,2), (2,3), (1,4), (5,4), (3,5), (2,7)]))
