HMMT={
    'BEGIN':{'Y':0.2,'N':0.8},
    'Y':{'Y':0.7,'N':0.2,'END':0.1},
    'N':{'Y':0.1,'N':0.8,'END':0.1},
    'END':{}
}

HMMG={
    'BEGIN':{},
    'Y':{'A':0.1,'C':0.4,'G':0.4,'T':0.1},
    'N':{'A':0.25,'C':0.25,'G':0.25,'T':0.25},
    'END':{'$':1}
}

seq='ATGCG$'

def viterbi(HMMT,HMMG,seq):
    l=len(seq)
    V={key:[[0,'?'] for i in range(l+1)] for key in HMMT.keys()}
    V['BEGIN'][0]=[1,'$']
    
    for c in range(l):
        for row in V.keys():
            for state in HMMT.keys():
                P=V[state][c][0]*HMMT[state].get(row,0)*HMMG[row].get(seq[c],0)
                if P>V[row][c+1][0]:
                    V[row][c+1]=[P,state]
    
    S=[]
    Pi=[]
    i=l
    state=V['END'][l][1]
    
    while state!='BEGIN':
        S.append(seq[i-2])
        Pi.append(state)
        i-=1
        state=V[state][i][1]
    S.reverse()
    Pi.reverse()

    print("The Viterbi matrix that contains both the probabilities and the states is:")
    for key in V:
        result=[]
        for elem in V[key]:
            result.append(elem)
        print("{}:{}".format(key,result))
    print("The sequence and the related states are:")
    print(S)
    print(Pi)
    print("P(S,Pi*)={}".format(V['END'][l][0]))

    return V, V['END'][l][0]

viterbi(HMMT,HMMG,seq)
