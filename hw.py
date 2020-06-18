"""
			Day1			Profits					SBI
OnePlus		150 units		200.27 per phone		3000.12 per phone
			Day2			Profits					SBI
OnePlus		250 units		200.27					3000.12
			Day3			Profits					SBI
OnePlus		100 units		200.27					3000.12


			Day1			Profits					SBI
HomeAppl 	120 units		50	per appl			100 per appl
			Day2			Profits					SBI
HomeAppl 	220 units		50	per appl			100 per appl
			Day3			Profits					SBI
HomeAppl 	180 units		50	per appl			100 per appl

"""

one_plus_day_1_sales = 150
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profit_to_amazon_from_one_plus = 200.27

discount_from_sbi_to_home_appl = 3000.27

home_appl_day1_sales = 120
home_appl_day2_sales = 220
home_appl_day3_sales = 180

profits_to_amazon_from_home_appl = 50

discounts_from_sbi_to_home_appl = 3000.12

total_one_plus_sales = one_plus_day_1_sales + one_plus_day_2_sales + one_plus_day_3_sales
total_home_appl_sales =  home_appl_day1_sales + home_appl_day2_sales + home_appl_day3_sales

if total_one_plus_sales > total_home_appl_sales:
    print("Amazon will invest in one plus for more customers", (total_one_plus-sales - total_home_appl_sales))
else:
    print("Amazon will invest in home appl for more customers", (total_home_appl_sales - total_one_plus_sales))


