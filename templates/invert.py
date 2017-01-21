gradient = ['rgba(69, 208, 255, 1)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 
        'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 
        'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)', 'rgba(69, 208, 255, 0)'];
a = []
t = len(gradient)
for x in range(t):
    print(t,x)
    a.append(gradient[t-x-1])

print(a)