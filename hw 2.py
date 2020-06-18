one_plus_day_1_sales = 150
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profits_to_amazon_from_one_plus = 200.27

discounts_from_sbi_to_one_plus = 3000.12

home_appl_day1_sales = 120
home_appl_day2_sales = 220
home_appl_day3_sales = 180

profits_to_amazon_from_home_appl = 50

discounts_from_sbi_to_home_appl = 3000.12

total_one_plus_sales = one_plus_day_1_sales + one_plus_day_2_sales + one_plus_day_3_sales
total_home_appl_sales = home_appl_day1_sales + home_appl_day2_sales + home_appl_day3_sales

net_one_plus_profits = total_one_plus_sales * profits_to_amazon_from_one_plus
net_home_appl_profits = total_home_appl_sales * profits_to_amazon_from_home_appl

print("One Plus Sale Profits Made by Amazon", net_one_plus_profits)
print("Home Appl Sale Profits Made by Amazon", net_home_appl_profits)


if net_one_plus_profits > net_home_appl_profits:
    print("Amazon Made more Profits on One Plus by", (net_one_plus_profits - net_home_appl_profits))
else:
    print("Amazon Made more Profits on Home Appl by", (net_home_appl_profits - net_one_plus_profits))