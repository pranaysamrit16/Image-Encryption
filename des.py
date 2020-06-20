

Mg = ""

PC1=[57 ,  49,    41,   33,    25 ,   17 ,   9,
               1  , 58 ,   50 ,  42 ,   34 ,   26 ,  18,
              10  ,  2  ,  59  , 51 ,   43 ,   35 ,  27,
              19   ,11   ,  3,   60 ,   52 ,   44  , 36,
              63  , 55    ,47,   39 ,   31 ,   23  , 15,
               7 ,  62,    54,   46 ,   38 ,   30  , 22,
              14,    6 ,   61,   53 ,   45 ,   37  , 29,
              21 ,  13  ,   5 ,  28 ,   20 ,   12  ,  4]

PC2=[14,    17 ,  11,    24 ,    1,    5,
                  3,    28 ,  15  ,   6,    21 ,  10,
                 23 ,   19 ,  12  ,   4,    26  ,  8,
                 16 ,    7 ,  27   , 20,    13,    2,
                 41 ,   52,   31,    37,    47 ,  55,
                 30 ,   40,   51 ,   45  ,  33,   48,
                 44 ,   49 ,  39  ,  56 ,   34,   53,
                 46  ,  42,   50   , 36,    29 ,  32]

IP1=[            58,    50,   42,    34,    26 ,  18,    10   , 2,
            60,    52 ,  44,    36 ,   28,   20,    12,    4,
            62 ,   54 ,  46 ,   38,    30,   22,    14,    6,
            64  ,  56,   48,    40,    32,   24,    16,    8,
            57 ,   49 ,  41,    33 ,   25,   17,     9 ,   1,
            59 ,   51,   43,    35,    27,   19,    11,    3,
            61 ,   53 ,  45,    37 ,   29,   21,    13,    5,
            63 ,   55,   47,    39,    31,   23,    15,    7 ]

IP2=[40,     8,   48,    16 ,   56 ,  24 ,   64,   32,
            39 ,    7,   47 ,   15 ,   55,   23,    63,   31,
            38 ,    6,   46 ,   14 ,   54,   22,    62,   30,
            37 ,    5,   45,    13 ,   53,   21,    61,   29,
            36 ,    4,   44,    12 ,   52,   20,    60,   28,
            35 ,    3,   43,    11 ,   51,   19,    59,   27,
            34 ,    2,   42,    10 ,   50,   18,    58,   26,
            33,     1,   41,     9 ,   49,   17,    57,   25]

E=[ 32,     1 ,   2,     3,     4,    5,
                  4,     5   , 6,     7,     8,    9,
                  8,     9 ,  10,    11,    12,   13,
                 12,    13,   14,    15,    16 ,  17,
                 16,    17   ,18,    19,    20,   21,
                 20,    21  , 22,    23,    24,   25,
                 24 ,   25 ,  26,    27,    28,   29,
                 28  ,  29,   30,    31 ,   32,    1]

P=[16 ,  7,  20 , 21,
                         29,  12,  28,  17,
                          1,  15,  23,  26,
                          5 , 18,  31,  10,
                          2 ,  8,  24,  14,
                         32 , 27,   3,   9,
                         19 , 13,  30,   6,
                         22 , 11,   4,  25]

S1=[14 , 4,  13,  1,   2,   15,  11,  8,   3, 10,   6, 12,   5,  9,   0,  7,
      0, 15,   7,  4,  14,  2,  13,  1,  10,  6,  12, 11,   9,  5,   3,  8,
      4,  1,  14,  8,  13,  6 ,  2, 11,  15, 12,   9,  7,   3, 10,   5,  0,
     15, 12,   8,  2 ,  4,  9,   1,  7,   5, 11,   3, 14,  10,  0,   6, 13]

S2=[ 15,  1,   8, 14,   6, 11,   3,  4,   9,  7,   2, 13,  12,  0,   5, 10,
      3, 13,   4,  7,  15,  2,   8, 14,  12,  0,   1, 10,   6,  9,  11,  5,
      0, 14,   7, 11,  10,  4,  13,  1,   5,  8,  12,  6,   9,  3,   2, 15,
     13,  8,  10,  1,   3, 15,   4,  2,  11,  6,   7, 12,   0,  5,  14,  9]

S3=[ 10,  0,   9, 14,   6,  3,  15 , 5,   1, 13,  12,  7,  11,  4,   2,  8,
     13,  7,   0,  9,   3,  4,   6, 10,   2 , 8,   5, 14,  12, 11,  15,  1,
     13,  6,   4,  9,   8, 15,   3,  0,  11,  1,   2, 12,   5, 10,  14,  7,
      1, 10,  13,  0,   6,  9,   8,  7,   4, 15,  14,  3,  11,  5,   2, 12]

S4=[ 7, 13  ,14 , 3  , 0 , 6  , 9, 10   ,1  ,2   ,8 , 5  ,11 ,12 ,  4, 15,
     13 , 8 , 11 , 5 ,  6, 15  , 0 , 3 ,  4 , 7 ,  2, 12,   1, 10,  14,  9,
     10  ,6 ,  9 , 0 , 12, 11  , 7 ,13  ,15 , 1 ,  3, 14,   5 , 2,   8,  4,
      3 ,15 ,  0 , 6 , 10 , 1  ,13 , 8  , 9 , 4 ,  5, 11,  12,  7,   2, 14]

S5=[  2, 12,   4,  1,   7, 10,  11,  6,   8,  5,   3, 15,  13,  0,  14  ,9,
     14 ,11,   2, 12 ,  4,  7 , 13,  1,   5,  0,  15, 10,   3,  9 ,  8 , 6,
      4,  2,   1, 11 , 10, 13,   7,  8,  15,  9,  12,  5,   6,  3 ,  0 ,14,
     11,  8,  12,  7 ,  1, 14,   2, 13,   6, 15,   0,  9,  10,  4  , 5,  3]

S6=[ 12 , 1,  10, 15 ,  9,  2 ,  6 , 8,   0, 13,   3,  4 , 14,  7  , 5, 11,
     10, 15 ,  4 , 2 ,  7, 12 ,  9,  5,   6,  1,  13, 14,   0, 11  , 3 , 8,
      9, 14 , 15,  5,   2 , 8,  12,  3,   7,  0,   4, 10,   1, 13 , 11  ,6,
      4 , 3,   2 ,12,   9 , 5 , 15, 10,  11, 14,   1,  7,   6 , 0,   8 ,13]

S7=[4, 11 ,  2, 14  ,15,  0,   8, 13  , 3,    12 ,  9,  7,   5, 10,   6,  1,
     13,  0,  11,  7 ,  4,  9 ,  1, 10 , 14  ,3  , 5 ,12,   2 ,15 ,  8 , 6,
      1,  4,  11, 13 , 12 , 3 ,  7, 14 , 10 ,15 ,  6 , 8,   0 , 5 ,  9 , 2,
      6 ,11,  13,  8,   1 , 4,  10 , 7,   9 , 5,   0 ,15,  14 , 2,   3 ,12]

S8= [13 , 2 ,  8,  4  , 6, 15 , 11,  1,  10,  9 ,  3, 14,   5,  0,  12,  7,
      1 ,15 , 13,  8  ,10,  3 ,  7,  4,  12,  5,   6, 11,   0, 14,   9,  2,
      7 ,11 ,  4,  1 ,  9, 12 , 14,  2,   0,  6,  10, 13,  15,  3,   5,  8,
      2 , 1,  14 , 7,   4, 10,   8, 13,  15 ,12,   9,  0,   3,  5,   6, 11]

def lshift(s,n):
    l=len(s)
    t=""
    for i in range(0,l):
        t+=s[(i+n)%l]
    return t

def createK(C,D):
    K=""
    for i in range(0,48):
        j=PC2[i]-1
        if(j<28):
            K+=C[j]
        else:
            K+=D[j%28]
    return K

def XOR(L,R):
    l=len(L)
    s=""
    for i in range(0,l):
        if(L[i] == R[i]):
            s+='0'
        else:
            s+='1'
    return s

def sb2(f,S):
    r=f[0]+f[5]
    c=f[1:5]
    r=int(r,2)
    c=int(c,2)
    rc=S[16*r+c]
    s=""
    s+="{0:b}".format(rc).zfill(4)
    return s

def sb(f):
    s=""
    s+=sb2(f[0:6],S1)
    s+=sb2(f[6:12],S2)
    s+=sb2(f[12:18],S3)
    s+=sb2(f[18:24],S4)
    s+=sb2(f[24:30],S5)
    s+=sb2(f[30:36],S6)
    s+=sb2(f[36:42],S7)
    s+=sb2(f[42:48],S8)
    
    temp=""
    for i in range(0,32):
        temp+=s[P[i]-1]

    return temp
    

def Etable(R,K):
    temp=""
    for i in range(0,48):
        temp+=R[E[i]-1]
    return XOR(temp,K)
    
def func(R,K):
    f0=Etable(R,K)
    f=sb(f0)
    return f
    

def encrypt(M,K):
    M=bin(int(M, 16))[2:].zfill(64)
    K=bin(int(K,16))[2:].zfill(64)
    L=M[0:32]
    R=M[32:64]

    temp=""
    for i in range(0,56):
        temp+=K[PC1[i]-1]

    K=temp
    C0=K[0:28]
    D0=K[28:56]
    C1=lshift(C0,1)
    D1=lshift(D0,1)
    C2=lshift(C1,1)
    D2=lshift(D1,1)
    C3=lshift(C2,2)
    D3=lshift(D2,2)
    C4=lshift(C3,2)
    D4=lshift(D3,2)
    C5=lshift(C4,2)
    D5=lshift(D4,2)
    C6=lshift(C5,2)
    D6=lshift(D5,2)
    C7=lshift(C6,2)
    D7=lshift(D6,2)
    C8=lshift(C7,2)
    D8=lshift(D7,2)
    C9=lshift(C8,1)
    D9=lshift(D8,1)
    C10=lshift(C9,2)
    D10=lshift(D9,2)
    C11=lshift(C10,2)
    D11=lshift(D10,2)
    C12=lshift(C11,2)
    D12=lshift(D11,2)
    C13=lshift(C12,2)
    D13=lshift(D12,2)
    C14=lshift(C13,2)
    D14=lshift(D13,2)
    C15=lshift(C14,2)
    D15=lshift(D14,2)
    C16=lshift(C15,1)
    D16=lshift(D15,1)

    K1=createK(C1,D1)
    K2=createK(C2,D2)
    K3=createK(C3,D3)
    K4=createK(C4,D4)
    K5=createK(C5,D5)
    K6=createK(C6,D6)
    K7=createK(C7,D7)
    K8=createK(C8,D8)
    K9=createK(C9,D9)
    K10=createK(C10,D10)
    K11=createK(C11,D11)
    K12=createK(C12,D12)
    K13=createK(C13,D13)
    K14=createK(C14,D14)
    K15=createK(C15,D15)
    K16=createK(C16,D16)

    IP=""
    for i in range(0,64):
        IP+=M[IP1[i]-1]
    
    L0=IP[0:32]
    R0=IP[32:64]

    L1=R0
    R1=XOR(L0,func(R0,K1) )

    L2=R1
    R2=XOR(L1,func(R1,K2) )
    L3=R2
    R3=XOR(L2,func(R2,K3) )
    L4=R3
    R4=XOR(L3,func(R3,K4) )
    L5=R4
    R5=XOR(L4,func(R4,K5) )
    L6=R5
    R6=XOR(L5,func(R5,K6) )
    L7=R6
    R7=XOR(L6,func(R6,K7) )
    L8=R7
    R8=XOR(L7,func(R7,K8) )
    L9=R8
    R9=XOR(L8,func(R8,K9) )
    L10=R9
    R10=XOR(L9,func(R9,K10) )
    L11=R10
    R11=XOR(L10,func(R10,K11) )
    L12=R11
    R12=XOR(L11,func(R11,K12) )
    L13=R12
    R13=XOR(L12,func(R12,K13) )
    L14=R13
    R14=XOR(L13,func(R13,K14) )
    L15=R14
    R15=XOR(L14,func(R14,K15) )
    L16=R15
    R16=XOR(L15,func(R15,K16) )

    LR=R16+L16
    temp=""
    for i in range(0,64):
        temp+=LR[IP2[i]-1]
        RL=temp

    #C="{0:0>4X}".format(int(RL, 2))
    C = '%0*X' % ((len(RL) + 3) // 4, int(RL, 2))
    return C

def decrypt(C,K):
    K=bin(int(K,16))[2:].zfill(64)

    temp=""
    for i in range(0,56):
        temp+=K[PC1[i]-1]

    K=temp
    C0=K[0:28]
    D0=K[28:56]
    C1=lshift(C0,1)
    D1=lshift(D0,1)
    C2=lshift(C1,1)
    D2=lshift(D1,1)
    C3=lshift(C2,2)
    D3=lshift(D2,2)
    C4=lshift(C3,2)
    D4=lshift(D3,2)
    C5=lshift(C4,2)
    D5=lshift(D4,2)
    C6=lshift(C5,2)
    D6=lshift(D5,2)
    C7=lshift(C6,2)
    D7=lshift(D6,2)
    C8=lshift(C7,2)
    D8=lshift(D7,2)
    C9=lshift(C8,1)
    D9=lshift(D8,1)
    C10=lshift(C9,2)
    D10=lshift(D9,2)
    C11=lshift(C10,2)
    D11=lshift(D10,2)
    C12=lshift(C11,2)
    D12=lshift(D11,2)
    C13=lshift(C12,2)
    D13=lshift(D12,2)
    C14=lshift(C13,2)
    D14=lshift(D13,2)
    C15=lshift(C14,2)
    D15=lshift(D14,2)
    C16=lshift(C15,1)
    D16=lshift(D15,1)

    K1=createK(C1,D1)
    K2=createK(C2,D2)
    K3=createK(C3,D3)
    K4=createK(C4,D4)
    K5=createK(C5,D5)
    K6=createK(C6,D6)
    K7=createK(C7,D7)
    K8=createK(C8,D8)
    K9=createK(C9,D9)
    K10=createK(C10,D10)
    K11=createK(C11,D11)
    K12=createK(C12,D12)
    K13=createK(C13,D13)
    K14=createK(C14,D14)
    K15=createK(C15,D15)
    K16=createK(C16,D16)
    
    RL=bin(int(C,16))[2:].zfill(64)
    temp=""
    for i in range(0,64):
        temp+=RL[IP1[i]-1]
        LR=temp
    
    R16=LR[0:32]
    L16=LR[32:64]
    
    L15=XOR(R16,func(L16,K16))
    R15=L16
    L14=XOR(R15,func(L15,K15))
    R14=L15
    L13=XOR(R14,func(L14,K14))
    R13=L14
    L12=XOR(R13,func(L13,K13))
    R12=L13
    L11=XOR(R12,func(L12,K12))
    R11=L12
    L10=XOR(R11,func(L11,K11))
    R10=L11
    L9=XOR(R10,func(L10,K10))
    R9=L10
    L8=XOR(R9,func(L9,K9))
    R8=L9
    L7=XOR(R8,func(L8,K8))
    R7=L8
    L6=XOR(R7,func(L7,K7))
    R6=L7
    L5=XOR(R6,func(L6,K6))
    R5=L6
    L4=XOR(R5,func(L5,K5))
    R4=L5
    L3=XOR(R4,func(L4,K4))
    R3=L4
    L2=XOR(R3,func(L3,K3))
    R2=L3
    L1=XOR(R2,func(L2,K2))
    R1=L2
    L0=XOR(R1,func(L1,K1))
    R0=L1
    
    IP=L0+R0
    
    temp=""
    for i in range(0,64):
        temp+=IP[IP2[i]-1]
    M=temp
    #C="{0:0>4X}".format(int(M, 2))
    C = '%0*X' % ((len(M) + 3) // 4, int(M, 2))
    return C
 