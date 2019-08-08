import string

alpha = []
alpha_m = []
kw = [ _ for _ in "dimat"]
alpha.append(kw)

z = 0 
for x in string.ascii_lowercase:
    if x not in kw:
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