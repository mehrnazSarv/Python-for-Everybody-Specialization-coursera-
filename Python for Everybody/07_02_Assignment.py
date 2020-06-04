fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
answer = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    number = float (line[21:])
    total = number + total
answer = total / count
print ("Average spam confidence: ",answer)
