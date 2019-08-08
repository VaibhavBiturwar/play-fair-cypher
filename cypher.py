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


pl = input("Enter Text to ENCRYPT : ")
pl = pl.split(" ")
pl = "".join(pl)
if len(pl)%2 !=0 :
    pl = pl+"x"
pl = pl.replace("j","i")
#print(pl)

for x in range(0,len(pl),2):
    for i in range(5):
        for j in range(5):
            if pl[x] == alpha[i][j]:
                for p in range(5):
                    for q in range(5):
                        if pl[x+1] == alpha[p][q]:
                            if i == p:
                                _ = j+1
                                if _ == 5:
                                    _=0
                                print(alpha[i][_] , end = "")
                                _ = q+1
                                if _ == 5:
                                    _=0
                                print(alpha[i][_] , end = "")
                           
                            elif j == q:
                                _ = i+1
                                if _ == 5:
                                    _=0
                                print(alpha[_][j] , end = "")
                                _ = p+1
                                if _ == 5:
                                    _=0
                                print(alpha[_][j] , end = "")
                            
                            else:
                                print(alpha[i][q] , end = "")
                                print(alpha[p][j] , end = "")
                                










