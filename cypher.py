import string

alpha = []
alpha_m = []
z = 0 
for x in string.ascii_lowercase:
    if z < 5:
        if x != 'j':
            alpha_m.append(x)
            z+=1
    else:
        z=1
        alpha.append(alpha_m)
        alpha_m=[]
        alpha_m.append(x)
alpha.append(alpha_m)

print(alpha)