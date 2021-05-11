infile = open("./ino.txt")
while True:
    line = infile.readline()
    if not line:
        break
    raw = line.split(',')
    print(raw)
    print(line.strip().rstrip("*").lstrip("#"))
    # strip은 양쪽 없앰 r,l은 각각의 위치에서 없앰!
