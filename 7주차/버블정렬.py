def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        bchanged = False

        for j in range(i):
            if (A[j] > A[j+1]):
                A[j],A[j+1] = A[j+1],A[j]
                bchanged = True
        if not bchanged: break
