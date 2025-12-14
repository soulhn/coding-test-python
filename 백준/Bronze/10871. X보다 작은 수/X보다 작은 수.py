N, X = map(int, input().split())
A = list(map(int, input().split()))

result = []
for v in A:
    if v < X:
        result.append(str(v))

print(" ".join(result))