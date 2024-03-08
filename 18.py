with open("18.in") as f: 
    arr = list(map(lambda line: list(map(int, line.split())), f.read().split("\n")))

print(*arr,sep="\n")