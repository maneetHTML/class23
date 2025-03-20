w=(1,0,1,0,1,0,1,0,1,0,0,1)
sunny=0
rain=0
for i in range(len(w)):
    if (w[i]==0):
        rain+=1
    else:
        sunny+=1

if(sunny>rain):
    print("good weather")
else:
    print("bad weather")