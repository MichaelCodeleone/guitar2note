def guitar(strin, adder):
	#strin is the string of the guitar
	#adder is the fret number
	#returns note
	n = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
	adj = n.index(strin)
	temp1 = adder % 12
	temp2 = n[(adj+temp1) % 12]
	if (((adj+temp1) % 12) == 0):
		temp2 = n[0]
	return(temp2)

#Each entry in notes is string + fret number
notes = ["G4","B7","B7","B0","G4","B7","B5","B3","B2","B0","D4","G2","D2","G1"]
notelist = []

for i in notes:
    notelist.append(guitar(i[0],int(i[1:])))

print(notelist)
