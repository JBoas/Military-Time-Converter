
usertime = input("Enter Time: ")

regularam = list(usertime)
regularpm = list(usertime)
militarypm = list(usertime)
militaryam = list(usertime)


if("AM")in(usertime):
	amtime3 = usertime.split(":")
	amtime2 = amtime3[1].split("A")
	amtime = ("0") + (amtime3[0]) + (amtime2[0])
	print(amtime)


elif("A.M.")in(usertime):
        amtime3 = usertime.split(":")
        amtime2 = amtime3[1].split("A")
        amtime = ("0") + (amtime3[0]) + (amtime2[0])
        print(amtime)


elif("a.m.")in(usertime):
        amtime3 = usertime.split(":")
        amtime2 = amtime3[1].split("a")
        amtime = ("0") + (amtime3[0]) + (amtime2[0])
        print(amtime)


elif("am")in(usertime):
        amtime3 = usertime.split(":")
        amtime2 = amtime3[1].split("a")
        amtime = ("0") + (amtime3[0]) + (amtime2[0])
        print(amtime)


elif("PM")in(usertime):
	pmtime3 = usertime.split(":")
	pmtime2 = pmtime3[1].split("P")
	pmtime = (pmtime3[0]) + (pmtime2[0])
	mpmtime = int(1200) + int(pmtime)
	print(mpmtime)


elif("P.M.")in(usertime):
        amtime3 = usertime.split(":")
        amtime2 = amtime3[1].split("P")
        amtime = ("0") + (amtime3[0]) + (amtime2[0])
        print(amtime)


elif("p.m.")in(usertime):
        pmtime3 = usertime.split(":")
        pmtime2 = pmtime3[1].split("p")
        pmtime = (pmtime3[0]) + (pmtime2[0])
        mpmtime = int(1200) + int(pmtime)
        print(mpmtime)


elif("pm")in(usertime):
        pmtime3 = usertime.split(":")
        pmtime2 = pmtime3[1].split("p")
        pmtime = (pmtime3[0]) + (pmtime2[0])
        mpmtime = int(1200) + int(pmtime)
        print(mpmtime)


if not ":"  in (usertime) or not "am"  in (usertime) or not "a.m." in (usertime) or not "A.M." in (usertime) or not "AM" in (usertime) or not "pm" in (usertime) or not "PM" in (usertime) or not "P.M." in (usertime) or not "p.m." in (usertime):
	if len(usertime) == 4 and (usertime.isnumeric()):

		if int(usertime) <= int(959):
			mtime3 = list(str(usertime))
			mtime2 = (mtime3[1]) + (":") + (mtime3[2]) + (mtime3[3]) + (" A.M.")
			print(mtime2)


		if int(usertime)>= int(1000):
			if int(usertime)<= int(1259):
				mtime6 = list(str(usertime))
				mtime5 = (mtime6[0]) + (mtime6[1]) + (":") + (mtime6[2]) + (mtime6[3]) + (" A.M.")
				print(mtime5)


		if int(usertime)>= int(1300):
			if int(usertime)<= int(2159):
				emtime4 = int(usertime) - int(1200)
				emtime3 = list(str(emtime4))
				emtime2 = (emtime3[0]) + (":") + (emtime3[1]) + (emtime3[2]) + (" P.M.")
				print(emtime2)


		if int(usertime) >= int(2200):
			if int(usertime) <= int(2459):
				emtime7 = int(usertime) - int(1200)
				emtime6 = list(str(emtime7))
				emtime5 = (emtime6[0]) + (emtime6[1]) + (":") + (emtime6[2]) + (emtime6[3]) + (" P.M.")
				print(emtime5)


else:
	print("Invalid")
