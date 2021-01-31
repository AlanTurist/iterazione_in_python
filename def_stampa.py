def stampa(n):

    if n > 0:
        print("\nIl programma calcola la somma seguente: ")
        print("\n7",end="")
        for j in range(1,n,1):
            print(end=" + 7"+"1"*j)