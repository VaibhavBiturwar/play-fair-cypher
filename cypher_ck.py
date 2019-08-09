# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:31:09 2019

@author: ck
"""

import string
def cypher_ck(pl):
    ans = []
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


    #pl = input("Enter Text to ENCRYPT : ")
    pl = pl.lower().split(" ")
    pl = "".join(pl)
    if len(pl)%2 !=0 :
        pl = pl+"x"
    
    for x in range(0,len(pl),2):
        i=0
        for j in range(5):
            if pl[x] == alpha[0][j]:
                break
        else: #runs only if break is not called(loop is not terminated)
            i=1
            val = ord(pl[x]) - 97
            if val > 19:
                val=19
            i= i+ (val//5)
            j= val%5
            while(pl[x]!=alpha[i][j]):#max 5 times chalega
                j=j-1
                if(j==-1):
                    j=4
                    i=i-1

        p=0        
        for q in range(5):
            if pl[x+1] == alpha[0][q]:
                break
        else:
            p=1
            val = ord(pl[x+1]) - 97
            if val > 19:
                val=19
            p= p+ (val//5)
            q= val%5
            while(pl[x+1]!=alpha[p][q]):#max 5 times chalega
                q=q-1
                if(q==-1):
                    q=4
                    p=p-1

    
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
            ans.append(alpha[i][q])
            # print(alpha[p][j] , end = "")
            ans.append(alpha[p][j])

    return "".join(ans)

print(cypher_ck("I PLAY WITH"))