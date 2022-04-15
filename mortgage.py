# List of yearly interest rates, or a single float if fixed forever.
# As it is it will set 1.65% for 5 years, 2.5% for 10 years,
# 3% for 10 years and 3.5% for the remaining time.
# Make sure there's info for enough years wrt the mortage duration.
interest_rate = [1.65]*5+[2.5]*10+[3.0]*5+[3.5]*30

# Amount of down payment
upfront_pay = 50000

# Real estate price
total = 400000

# Fee you want to pay every month, debt+interest
monthly = 1700

# If you want to split the mortgage in two and apply different interest
# rates to the two chunks. Same format as interest_rate.
split_with_variable = False
variable_rate = [1.11]*1+[1.4]*1+[2.4]*30

# Some init
loan = total - upfront_pay
left_to_pay = loan
year = 1
cumulated_interest = 0

print('Interest rate {}, loan amount {}, monthly fee {}, upfront pay {}'.format(interest_rate, loan, monthly,  upfront_pay))

# In Sweden mortgages go on until entirely paid back!
while left_to_pay > 0:
	if type(interest_rate) == float:
		interest_fee = round(left_to_pay/100*interest_rate/12)
	else:
		actual_rate = interest_rate[year-1]
		if split_with_variable: # if mortgage is split, pick average interest rate
			actual_rate = (interest_rate[year-1]+variable_rate[year-1])/2
			
		interest_fee = round(left_to_pay/100*actual_rate/12)
	
	amortering = round(monthly - interest_fee)
	amortering_percentage = round(amortering*12/left_to_pay, 3)

	if left_to_pay < amortering*12: #less than a year left until mortgage is paid back
		amortering = round(left_to_pay/(left_to_pay/monthly)-interest_fee)
		print('year {}, interest {}, amortering {} for {} months'.format(year, interest_fee, amortering, round(left_to_pay/monthly)))
	else:
		print('year {}, interest {} ({}%), amortering {} ({}%), left to pay {}'.format(year, interest_fee, round(actual_rate, 2), amortering, amortering_percentage, left_to_pay))

	left_to_pay -= amortering*12
	year += 1
	cumulated_interest += interest_fee*12

print('Total spent in interest: {}'.format(cumulated_interest))
