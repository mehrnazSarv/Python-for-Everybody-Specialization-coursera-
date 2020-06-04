
fname = input("Enter file name: ")
handle = open(fname)


words = list()

for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])


counts = dict()

for word in words:
           counts[word] = counts.get(word, 0) + 1

maxval = None
maxkey = None

for key,val in counts.items() :
    if maxval is None or val > maxval:
        maxval = val
        maxkey = key

print (maxkey, maxval)
