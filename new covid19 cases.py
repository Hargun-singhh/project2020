state1 = {
    "active": 881,
	"confirmed": 3497,
	"deaths": 78,
	"recovered": 2538,
	"state": "Punjab"

}
state2 = {
    "active": 51922,
	"confirmed": "116752",
	"deaths": 5651,
	"recovered": 59166,
	"state": "Maharashtra"

}
state3 = {
	"active": 21993,
	"confirmed": 50193,
	"deaths": 576,
	"recovered": 27624,
	"state": "Tamil Nadu"

}
state4 = {
	"active": 27741,
	"confirmed": 47102,
	"deaths": 1904,
	"recovered": 17457,
	"state": "Delhi"

}
state5 = {
	"active": 6149,
	"confirmed": 25148,
	"deaths": "1561",
	"recovered": 17438,
	"state": "Gujarat"

}
state6 = {
	"active": "162534",
	"confirmed": "372552",
	"deaths": "12390",
	"recovered": "197583",
	"state": "Total"


}
state7 = {
	"active": "5659",
	"confirmed": "15785",
	"deaths": "488",
	"recovered": "9638",
	"state": "Uttar Pradesh"

}
state8 = {
	"active": "2721",
	"confirmed": "13626",
	"deaths": "323",
	"recovered": "10582",
	"state": "Rajasthan"

}
state9 = {
	"active": "5216",
	"confirmed": "12735",
	"deaths": "518",
	"recovered": "7001",
	"state": "West Bengal"

}
state10 = {
	"active": "2308",
	"confirmed": "11426",
	"deaths": "486",
	"recovered": "8632",
	"state": "Madhya Pradesh"

}
state11 = {
	"active": "4710",
	"confirmed": "9743",
	"deaths": "144",
	"recovered": "4889",
	"state": "Haryana"
}
state12 = {
	"active": "2939",
	"confirmed": "8281",
	"deaths": "125",
	"recovered": "5213",
	"state": "Karnataka"
}
state13 ={
	"active": "4240",
	"confirmed": "8452",
	"deaths": "101",
	"recovered": "4111",
	"state": "Andhra Pradesh"
}
state14 ={
	"active": "2087",
	"confirmed": "7503",
	"deaths": "49",
	"recovered": "5367",
	"state": "Bihar"
}
state15 ={
	"active": "3363",
	"confirmed": "7072",
	"deaths": "203",
	"recovered": "3506",
	"state": "Telangana"
}
state16 = {
	"active": "2417",
	"confirmed": "5834",
	"deaths": "81",
	"recovered": "3336",
	"state": "Jammu and Kashmir"
}
state17 = {
	"active": "1791",
	"confirmed": "5006",
	"deaths": "9",
	"recovered": "3203",
	"state": "Assam"
}
state18 = {
	"active": "1307",
	"confirmed": "4856",
	"deaths": "15",
	"recovered": "3534",
	"state": "Odisha"
}
state19 = {
	"active": "1450",
	"confirmed": "3040",
	"deaths": "22",
	"recovered": "1566",
	"state": "Kerala"
}
state20 = {
	"active": "809",
	"confirmed": "2301",
	"deaths": "27",
	"recovered": "1450",
	"state": "Uttarakhand"
}
state21 = {
	"active": "755",
	"confirmed": "2134",
	"deaths": "11",
	"recovered": "1368",
	"state": "Chhattisgarh"
}
state22 = {
	"active": "615",
	"confirmed": "1961",
	"deaths": "11",
	"recovered": "1335",
	"state": "Jharkhand"
}
state23 = {
	"active": "531",
	"confirmed": "1189",
	"deaths": "1",
	"recovered": "657",
	"state": "Tripura"
}
state24 = {
	"active": "718",
	"confirmed": "836",
	"deaths": "1",
	"recovered": "117",
	"state": "Ladakh"
}
state25 = {
	"active": "625",
	"confirmed": "754",
	"deaths": "0",
	"recovered": "129",
	"state": "Goa"
}
state26 = {
	"active": "228",
	"confirmed": "650",
	"deaths": "7",
	"recovered": "402",
	"state": "Himachal Pradesh"
}
state27 = {
	"active": "463",
	"confirmed": "681",
	"deaths": "0",
	"recovered": "218",
	"state": "Manipur"
}
state28 = {
	"active": "68",
	"confirmed": "390",
	"deaths": "6",
	"recovered": "316",
	"state": "Chandigarh"
}
state29 = {
	"active": "121",
	"confirmed": "135",
	"deaths": "0",
	"recovered": "14",
	"state": "Arunachal Pradesh"
}
state30 = {
	"active": "200",
	"confirmed": "338",
	"deaths": "7",
	"recovered": "131",
	"state": "Puducherry"
}
india = [state2, state3, state4, state5, state1, state7, state8, state9, state10, state11, state12, state13, state14, state15, state16, state17, state18, state19, state20, state21, state22, state23, state24, state25, state26, state27, state28, state29, state30, state6]
print("Length of India is:", len(india))
print()

filter1 = input("Please Enter 1st Filter from [active | confirmed | deaths | recovered | state]: ")
filter2 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")
filter3 = input("Please Enter 2nd Filter from [active | confirmed | deaths | recovered | state]: ")

for i in range(0, len(india)):
	print("~~~~~~~~~~~~~~~~~~")
	print("{}: {}\n{}: {}\n{}: {}".format(filter1.upper(), india[i][filter1], filter2.upper(), india[i][filter2], filter3.upper(), india[i][filter3]))
	print("~~~~~~~~~~~~~~~~~~")
	print()

state = input("Enter the name of state to search: ")
for i in range(0, len(india)):

	print("Matching {} with {}".format(state, india[i]["state"]))

	# if state == india[i]["state"]:
	if state.lower() == india[i]["state"].lower():
		print("State {} Found. Details are Below:".format(state))
		print(india[i])
		break
