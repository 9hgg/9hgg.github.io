file=open("million.txt","w")
file.write("1")
for i in range(1000000):
    file.write("0")
file.write(".")
file.close()
