import string

def cypher_old(pl):

    ans =[]
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

    pl = pl.lower().split(" ")
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
                                    # print(alpha[i][_] , end = "")
                                    ans.append(alpha[i][_])
                                    _ = q+1
                                    if _ == 5:
                                        _=0
                                    # print(alpha[i][_] , end = "")
                                    ans.append(alpha[i][_])

                                elif j == q:
                                    _ = i+1
                                    if _ == 5:
                                        _=0
                                    # print(alpha[_][j] , end = "")
                                    ans.append(alpha[_][j])
                                    _ = p+1
                                    if _ == 5:
                                        _=0
                                    # print(alpha[_][j] , end = "")
                                    ans.append(alpha[_][j])
                                
                                else:
                                    # print(alpha[i][q] , end = "")
                                    ans.append(alpha[i][q] )
                                    # print(alpha[p][j] , end = "")
                                    ans.append(alpha[p][j] )
                                break           
    return "".join(ans)
                        
#print(cypher_old("ADHVVRGTJV FJGDFBJ RIGHRI H RITHER RENGFHN TKHJRTKHEJROG WORT OEW vakfhsf drewbr uewr ewgruewdgaudgfuas bweurw eurewbtuqerbqeur wbewurwegfw uegruf ewbrewurbfwe urb32truqe bqewruwe br qeurewruqer qeur qev ruqevr qruq"))









