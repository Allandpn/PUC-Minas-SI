

v0 = [4]
v1 = [2,3]
v2 = [1]
v3 = [1,4,6]
v4 = [0,3]
v5 = [6,8]
v6 = [3,5,7,14]
v7 = [6]
v8 = [5,9,11]
v9 = [8,10]
v10 = [9,11,15]
v11 = [8,10,12]
v12 = [11]
v13 = [15]
v14 = [6]
v15 = [10,13]



vetores = {   
    0:v0,
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
}


class Vetor:
    def __init__(self, v, adj=0):
        self.v = v
        self.adj = adj
        self.td = 0
        self.tt = 0
        self.pai = None  

ListaBP = []
Saida = []

arestaarvore = []
arestaretorno = []


def dfs(v, t):
    t += 1
    v.td = t
    for w_ in v.adj:
        w = ListaBP[w_]
        if w.td == 0:
            w.pai = v.v
            arestaarvore.append(f"{v.v}:{w.v}")            
            dfs(w, t)
        elif w.tt == 0 and v.pai != w:
            arestaretorno.append(f"{v.v}:{w.v}")  
    t += 1 
    v.tt = t
    
    
def rota(v):
    Saida.append(v.v)
    if v.pai is not None:
        rota(ListaBP[v.pai])
        


class Main:
    def __init__(self):
        for key, value in vetores.items():
            v = Vetor(key, value)
            ListaBP.append(v)
        
        t = 0
        raiz = ListaBP[0]        
        
        dfs(raiz, t)
        
        # print(arestaarvore)
        # print(arestaretorno)
        
        
        # for v in ListaBP:
        #     print(f"v:{v.v}, td:{v.td}, tt:{v.tt}, pai:{v.pai}")
       
        rota(ListaBP[13])
        print(Saida[::-1])
        

main_instance = Main()
        
        
   