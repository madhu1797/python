##For loop - iteration over numeric range

for i in range(1,10,2):
  print(i)


##Iteration over list
mylist = [30,21,33,42,53,64,71,86,97,10]
for i in mylist:
    print(i)

##loop with continue
for n in "abcdef":
    if n =="a" or n =="d":
       continue
    print("letter :", n)

##loop with break
for n in "abcdef":
    if n =="a" or n =="d":
       print("letter :", n)
    else:
        break

