def mergeSort(alist):
    print("Splitting: ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[0:mid]
        righthalf = alist[mid:len(alist)]
        print("\n\n************************")
        print("LEFT HALF: ", lefthalf)
        print("RIGH HALF:, ", righthalf)
        print("************************\n\n")

        print("SIGUE LEFT")
        mergeSort(lefthalf)
        print("SIGUE RIGHT")
        mergeSort(righthalf)
        print("FIN CALL")


        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            #print("\n Len half: ", len(lefthalf))
            #print("\n Len right: ", len(righthalf))

            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
                print("case 1")
                print("i: ", i)
            else:
                alist[k] = righthalf[j]
                j = j + 1
                print("case 2")
                print("j: ", j)
            k = k + 1
            print("k: ", k)
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
            print("case 3")
            print("i: ", i)
            print("k: ", k)

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
            print("case 4")
            print("j: ", j)
            print("k: ", k)

    print("Merging: ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
