def colorGradient(c1, c2, steps):
    jump = [(c2[x]-c1[x])/(steps-1) for x in range(len(c1))]
    print(jump)
    a = []
    for x in range(steps):
        a.append([int(c1[y]+jump[y]*x) for y in range(len(c1))])
    return a
def invert(gradient):
    a = []
    t = len(gradient)
    for x in range(t):
        print(t,x)
        a.append(gradient[t-x-1])
    return a
def process(g):
    t = []
    for x in g:
        print(x)
        t.append( (int(x[0]), int(x[1]), int(x[2]), x[3]) )
    return t
r = colorGradient((255, 255, 0, 1), (255,0, 0, 1), 14)
print(len(r))
print(process(invert(r)))
g = ['rgba('+str(r[x])[1:-1]+')' for x in range(len(r))]
print(g)