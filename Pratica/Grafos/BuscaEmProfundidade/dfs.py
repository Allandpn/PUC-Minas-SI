


v1 = [2,3]
v2 = [1,6]
v3 = [1,4,5]
v4 = [3]
v5 = [3,6,8]
v6 = [2,5]
v7 = [8,10]
v8 = [5,7,9,16]
v9 = [8]
v10 = [7,11,13]
v11 = [10,12]
v12 = [11,13,17]
v13 = [10,12,14]
v14 = [13]
v15 = [17]
v16= [8]
v17 = [12,15]



vetores = {   
    1:v1,
    2:v2,
    3:v3,
    4:v4,
    5:v5,
    6:v6,
    7:v7,
    8:v8,
    9:v9,
    10:v10,
    11:v11,
    12:v12,
    13:v13,
    14:v14,
    15:v15,
    16:v16,
    17:v17
}


class Vetor:
    def __init__(self, v, adj=0):
        self.v = v
        self.adj = adj
        self.td = 0
        self.tt = 0
        self.pai = None  

ListaBP = []

arestaarvore = []
arestaretorno = []


def dfs(v, t):
    t += 1
    v.td = t
    for w_ in v.adj:
        w = ListaBP[w_-1]
        if w.td == 0:
            w.pai = v.v
            arestaarvore.append(f"{v.v}:{w.v}")            
            dfs(w, t)
        elif w.tt == 0 and v.pai != w:
            arestaretorno.append(f"{v.v}:{w.v}")  
    t += 1 
    v.tt = t
    


class Main:
    def __init__(self):
        for key, value in vetores.items():
            v = Vetor(key, value)
            ListaBP.append(v)
        
        t = 0
        raiz = ListaBP[0]        
        
        dfs(raiz, t)
        
        print(arestaarvore)
        print(arestaretorno)
        

main_instance = Main()
        
        
   