infile = open("d:\\input.txt","r", encoding="utf-8")
line = infile.readline()
while line != "":
    print(line)
    line = infile.readline()



word_list = []

infile = open('word_list.txt', "r",encoding="utf-8")

for line in infile:
    line = line.rstrip()
    word_list = line.split(',')
    for word in word_list:
        print(word)