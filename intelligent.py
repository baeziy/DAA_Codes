
def foo(P):
    P = sorted(P)
    Stack = []
    for i in P:
        while(Stack and Stack[-1][1] <= i[1]):
            Stack.pop()
        Stack.append(i)

    return Stack
print(foo([(2,5), (3,13), (4,11), (5,1), (7,7), (9,10), (10,5), (12,12), (13,3), (14,10), (15,7)]))
