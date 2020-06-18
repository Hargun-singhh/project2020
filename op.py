state1 = {
    "active": 881,
	"confirmed": 3497,
	"deaths": 78,
	"deltaconfirmed": "0",
	"deltadeaths": "0",
	"deltarecovered": "0",
	"lastupdatedtime": "17/06/2020 19:35:50",
	"recovered": 2538,
	"state": "Punjab",
	"statecode": "Punjab  --"
}

state2 = {
    "active": 51922,
	"confirmed": "116752",
	"deaths": 5651,
	"deltaconfirmed": "0",
	"deltadeaths": "0",
	"deltarecovered": "0",
	"lastupdatedtime": "17/06/2020 23:34:48",
	"migratedother": "13",
	"recovered": 59166,
	"state": "Maharashtra",
	"statecode": "Maharashtra  --"
}

state3 = {
	"active": 21993,
	"confirmed": 50193,
	"deaths": 576,
	"deltaconfirmed": "0",
	"deltadeaths": "0",
	"deltarecovered": "0",
	"lastupdatedtime": "17/06/2020 18:45:48",
	"migratedother": "0",
	"recovered": 27624,
	"state": "Tamil Nadu",
	"statecode": "Tamil Nadu  --"
}

state4 = {
	"active": 27741,
	"confirmed": 47102,
	"deaths": 1904,
	"deltaconfirmed": "0",
	"deltadeaths": "0",
	"deltarecovered": "0",
	"lastupdatedtime": "17/06/2020 23:26:52",
	"migratedother": "0",
	"recovered": 17457,
	"state": "Delhi",
	"statecode": "Delhi  --"
}


state5 = {
	"active": 6149,
	"confirmed": 25148,
	"deaths": "1561",
	"deltaconfirmed": "0",
	"deltadeaths": "0",
	"deltarecovered": "0",
	"lastupdatedtime": "17/06/2020 21:05:49",
	"migratedother": "0",
	"recovered": 17438,
	"state": "Gujarat",
	"statecode": "Gujarat  --"
}
state6 = {
	"active": "162534",
	"confirmed": "372552",
	"deaths": "12390",
	"deltaconfirmed": "5288",
	"deltadeaths": "75",
	"deltarecovered": "3042",
	"lastupdatedtime": "18/06/2020 20:44:10",
	"migratedother": "45",
	"recovered": "197583",
	"state": "Total",
	"statecode": "Country  --"

}
state7 = {
	"active": "5659",
	"confirmed": "15785",
	"deaths": "488",
	"deltaconfirmed": "604",
	"deltadeaths": "23",
	"deltarecovered": "399",
	"lastupdatedtime": "18/06/2020 18:45:48",
	"migratedother": "0",
	"recovered": "9638",
	"state": "Uttar Pradesh",
	"statecode": "Uattar Pradesh  --",
	"statenotes": ""
}
state8 = {
	"active": "2721",
	"confirmed": "13626",
	"deaths": "323",
	"deltaconfirmed": "84",
	"deltadeaths": "10",
	"deltarecovered": "115",
	"lastupdatedtime": "18/06/2020 11:11:47",
	"migratedother": "0",
	"recovered": "10582",
	"state": "Rajasthan",
	"statecode": "Rajasthan  --",
	"statenotes": ""
}
state9 = {
	"active": "5216",
	"confirmed": "12735",
	"deaths": "518",
	"deltaconfirmed": "435",
	"deltadeaths": "12",
	"deltarecovered": "468",
	"lastupdatedtime": "18/06/2020 20:44:15",
	"migratedother": "0",
	"recovered": "7001",
	"state": "West Bengal",
	"statecode": "West Bengal  --",
	"statenotes": ""
}
state10 = {
	"active": "2308",
	"confirmed": "11426",
	"deaths": "486",
	"deltaconfirmed": "182",
	"deltadeaths": "4",
	"deltarecovered": "244",
	"lastupdatedtime": "18/06/2020 19:25:49",
	"migratedother": "0",
	"recovered": "8632",
	"state": "Madhya Pradesh",
	"statecode": "Madhya Pradesh  --",
	"statenotes": ""
}
cases = [state2, state3, state4, state5, state1, state7, state8, state9, state10, state6]
print("cases: ")


for i in range(0, 10):
    print("Cases of",cases[i]['statecode'], "\t", "Confirmed Cases-",cases[i]['confirmed'], "\t", "Active Cases-",cases[i]['active'],"\t", "Deaths-",cases[i]['deaths'],)
    print("~~~~~~~~~~~~~~~~~~~~~")
print()


