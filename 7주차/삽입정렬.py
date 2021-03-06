def insertion_sort(A):      # 삽입 정렬
    n = len(A)

    for i in range(1,n):    # 외부 루프 1부터 끝까지
        key = A[i]          # 키 값 설정
        j = i-1             # 이전 값
        while j >= 0 and A[j] > key:    # 이전값이 0보다 같거나크고 이전값이 키 값보다 클 때
            A[j+1] = A[j]   # 이전 값을 그 다음 값에 넣어줌
            j -= 1          # 한칸 더 뒤로
        A[j+1] = key        # 반복이 끝나면 즉, j값이 0보다 작거나 키값이 더 클 때 (정렬된 자리를 찾았다면) 그 자리에 키 값 삽입


# 삽입 정렬의 복잡도는 입력 자료의 구성에 따라서 달라진다. 입력 자료가 이미 정렬되어 있는 경우는 가장 빠르다.내부 루프가 모든 항목에서 한번 만에 빠져
# 나올 것이기 때문이다. 단, 역으로 정렬된 경우에는 시간 복잡도가 n^2으로 커진다.