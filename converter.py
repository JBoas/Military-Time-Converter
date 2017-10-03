usertime = input("Enter Time")

if("AM")in(usertime):
	amtime3 = usertime.split(":")
	print(amtime3)
	amtime2 = amtime3[1].split("A")
	print(amtime2)
	amtime = ("0") + (amtime3[0]) + (amtime2[0])
	print(amtime)


if("AM")in(usertime):
        amtime3 = usertime.split(":")
        print(amtime3)
        amtime2 = amtime3[1].split("A")
        print(amtime2)
        amtime = ("0") + (amtime3[0]) + (amtime2[0])
        print(amtime)



if("am")in(usertime):
        amtime3 = usertime.split(":")
        print(amtime3)
        amtime2 = amtime3[1].split("a")
        print(amtime2)
        amtime = ("0") + (amtime3[0]) + (amtime2[0])
        print(amtime)



if("PM")in(usertime): 
	pmtime3 = usertime.split(":")
	pmtime2 = pmtime3[1].split("P")
	pmtime = (pmtime3[0]) + (pmtime2[0])
	mpmtime = int(1200) + int(pmtime)
	print(mpmtime)



if("pm")in(usertime):
        pmtime3 = usertime.split(":")
        pmtime2 = pmtime3[1].split("p")
        pmtime = (pmtime3[0]) + (pmtime2[0])
        mpmtime = int(1200) + int(pmtime)
        print(mpmtime)

