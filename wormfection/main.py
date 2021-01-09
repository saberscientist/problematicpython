import functools
_input = open("input.txt", "r")
input = _input.read().split("\n")

N = int(input[0])
C = int(input[1])

answer = [None for _i in range(C)]
clusters = [[i] for i in range(N)]

def find(x):
    root = x
    pointer_to_root = -1

    while isinstance(root, int):
        pointer_to_root = root
        root = clusters[root]
    
    while isinstance(clusters[x], int):
        next_gen = clusters[x]
        clusters[x] = pointer_to_root
        x = next_gen

    return pointer_to_root

def merge(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    else:
        if len(clusters[b]) > len(clusters[a]):
            a,b = b,a

    clusters[a].extend(clusters[b])
    clusters[b] = a
   

for i in range(len(input) - 1, 2, -1):

    edge = list(map(int, input[i].split()))
    a = edge[0]
    b = edge[1]
   
    merge(a, b)
    answer[i - 3] = str(functools.reduce(lambda x, y: x+ y, map(lambda arr: len(arr) ** 2, filter(lambda cluster: isinstance(cluster, list), clusters))))

answer[C - 1] = str(N)
print(" ".join(answer))