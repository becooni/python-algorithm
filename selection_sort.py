import time

A = list(map(int, input().split()))

start_time = time.time()

for i in range(len(A)):

    min_idx = i

    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

for i in A:
    print(i),

end_time = time.time()
print("time:", end_time - start_time)