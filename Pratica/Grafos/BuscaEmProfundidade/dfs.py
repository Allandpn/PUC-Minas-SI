

vetores = {   
    0:[4],
    1:[2,3],
    2:[1],
    3:[1,4,6],
    4:[0,3],
    5:[6,8],
    6:[3,5,7,14],
    7:[6],
    8:[5,9,11],
    9:[8,10],
    10:[9,11,15],
    11:[8,10,12],
    12:[11],
    13:[15],
    14:[6],
    15:[10,13],
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
        
        
   