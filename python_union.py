size = int(input())
arr = list(map(int, input().split()))
size2 = int(input())
arr1 = list(map(int, input().split()))

arr = set(arr)
arr1 = set(arr1)

ans = arr.difference(arr1).union(arr1.difference(arr))
for _ in (sorted(ans)):
    print(_)
