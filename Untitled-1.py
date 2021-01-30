filepath = "./hole.txt"
with open(filepath) as fp:
    lines = fp.read().splitlines()
with open(filepath, "w") as fp:
    for line in lines:
        print('"'+ line + '"', file=fp)