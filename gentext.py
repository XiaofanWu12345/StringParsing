s=""
for x in range(500):
    s+="asdfklj, "
for x in range(300):
    s+="asdfjkl, "
for x in range(100):
    s+="asldfjlojadfklsjkl "
for x in range(100):
    s+="asjkdlf, "
with open("text.txt","w") as f:
    f.write(s)