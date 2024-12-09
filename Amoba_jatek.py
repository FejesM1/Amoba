"""
a kód működése:
először létre hozzuk a 10x10-es mezőt
uttánna kérjük be az inputokat addig amíg nincs 100 input vagy vki nem nyert
minden másodiknál x a többbi o
hogy nyer vki ha egy sorba vagy egy oszlopba 5 db x vgy o van akkor az nyert

"""
userx=input("[x] Kérem a nevét:")
usero=input("[o], Kérem a nevét: ")
palya=[]
for i in range(10):
    palya.append([])
    for q in range(10):
        palya[i].append("   ")

def kiir():

    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    for c in range(10):
        palya.append([])
        print(*palya[c])
        if c!=9:
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
        else:
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")

vege=True  
def szamol():
    global vege
    for q in range(10):
        akt=""
        aktf=""
        for w in range(10):
            akt+=palya[q][w]
            aktf+=palya[w][q]
        if " x  x  x  x  x"in akt:
            print(f"Vége a játéknak. Nyertes: {userx}")
            vege=False
        elif "o  o  o  o  o" in akt:
            print(f"Vége a játéknak. Nyertes: {usero}")
            vege=False
        elif " x  x  x  x  x" in aktf:
            print(f"Vége a játéknak. Nyertes: {userx}")
            vege=False
        elif "o  o  o  o  o" in aktf:
            print(f"Vége a játéknak. Nyertes: {usero}")
            vege=False
    for  i in range(6):
        fjbl=""
        fjbl1=""
        fblj=""
        fblj1=""
        for t  in range(i,10):
            fjbl+=palya[t-i][t]
            fjbl1+=palya[t][t-i]
            fblj += palya[t - i][9 - t]       # Bal felsőtől jobb alsóig átló
            fblj1 += palya[t][9 - (t - i)]   
        if " x  x  x  x  x " in fjbl1 or " x  x  x  x x "in fjbl:
            print(f"Vége a játéknak. Nyertes: {userx}")
            vege=False
        elif " o  o  o  o  o " in fjbl1 or " o  o  o  o  o "in fjbl:
            print(f"Vége a játéknak. Nyertes: {userx}")
            vege=False
        elif " x  x  x  x  x " in fblj1 or " x  x  x  x x "in fblj:
            print(f"Vége a játéknak. Nyertes: {userx}")
            vege=False
        elif " o  o  o  o  o " in fblj1 or " o  o  o  o  o "in fblj:
            print(f"Vége a játéknak. Nyertes: {userx}")
            vege=False


       
            


kiir()
xo=0

while xo<100 and vege:
    koordinatak=input()
    k=koordinatak.split(" ")
    print(k)
    qw=True
    if palya[int(k[0])-1][int(k[1])-1]==" o ":
        print("Ez a hely foglalt.")
        qw=False
    elif palya[int(k[0])-1][int(k[1])-1]==" x ":
        print("Ez a hely foglalt.")
        qw=False
    elif qw:
        xo+=1
    if xo%2==0 and qw:
        palya[int(k[0])-1][int(k[1])-1]=" o "
    elif qw:
         palya[int(k[0])-1][int(k[1])-1]=" x "

    
    kiir()
    szamol()
