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

india = [state2, state3, state4, state5, state1, state7, state8, state9, state10, state11, state12, state6]
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
