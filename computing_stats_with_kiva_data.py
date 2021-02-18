from math import sqrt

loan_amount = [1250.0, 500.0, 1450.0, 200.0, 700.0, 100.0, 250.0, 225.0, 1200.0, 150.0, 600.0, 300.0, 700.0, 125.0,
               650.0, 175.0, 1800.0, 1525.0, 575.0, 700.0, 1450.0, 400.0, 200.0, 1000.0, 350.0]

country_name = ['Azerbaijan', 'El Salvador', 'Bolivia', 'Paraguay', 'El Salvador', 'Philippines', 'Philippines',
                'Nicaragua', 'Guatemala', 'Philippines', 'Paraguay', 'Philippines', 'Bolivia', 'Philippines',
                'Philippines', 'Madagascar', 'Georgia', 'Uganda', 'Kenya', 'Tajikistan', 'Jordan', 'Kenya',
                'Philippines', 'Ecuador', 'Kenya']

time_to_raise = [193075.0, 1157108.0, 1552939.0, 244945.0, 238797.0, 1248909.0, 773599.0, 116181.0, 2288095.0, 51668.0,
                 26717.0, 48030.0, 1839190.0, 71117.0, 580401.0, 800427.0, 1156218.0, 1166045.0, 2924705.0, 470622.0,
                 24078.0, 260044.0, 445938.0, 201408.0, 2370450.0]

num_lenders_total = [38, 18, 51, 3, 21, 1, 10, 8, 42, 1, 18, 6, 28, 5, 16, 7, 54, 1, 18, 22, 36, 12, 8, 24, 8]

# total amount of money loaned
loan_total = 0
for loan in loan_amount:
    loan_total += loan
print(loan_total)

# average amount of money loaned
number_of_loans = len(loan_amount)
print(number_of_loans)
loan_total = 0
for loan in loan_amount:
    loan_total += loan
loan_average = (loan_total / number_of_loans)
print(loan_average)

# min and max loans
min_loan = min(loan_amount)
print(min_loan)
max_loan = max(loan_amount)
print(max_loan)
min_index = loan_amount.index(min_loan)
max_index = loan_amount.index(max_loan)
max_country = country_name[max_index]
min_country = country_name[min_index]
print(min_country)
print(max_country)

# average lenders per loan
how_many_lenders = len(num_lenders_total)
print(how_many_lenders)
lenders_total = 0
for lender in num_lenders_total:
    lenders_total += lender
average_lenders = (lenders_total / how_many_lenders)
print(average_lenders)

# total loans to Philippines
philippines_count = country_name.count('Philippines')

# loans for each country
unique_countries = ['Guatemala', 'Paraguay', 'Tajikistan', 'Kenya', 'Azerbaijan', 'El Salvador', 'Bolivia', 'Ecuador',
                    'Georgia', 'Philippines', 'Uganda', 'Madagascar', 'Nicaragua', 'Jordan']

for country in unique_countries:
    print(country, country_name.count(country))

# average loan amount to Philippines
loan_total = 0
p_index = [5, 6, 9, 11, 13, 14, 22]
for index in p_index:
    loan_total += loan_amount[index]
p_average = (loan_total / len(p_index))

# longest loan to raise
max_time = max(time_to_raise)
max_index = time_to_raise.index(max_time)
longest_to_fund = country_name[max_index]

# arithmetic mean (time / dollar)
a_mean = 0
a_total = 0
for time in time_to_raise:
    temp_index = time_to_raise.index(time)
    amount = loan_amount[temp_index]
    a_total += (time / amount)
a_mean = (a_total / len(time_to_raise))

# standard deviation and variance of loan amount
number_of_loans = len(loan_amount)
loan_total = 0
loan_average = 0
for loan in loan_amount:
    loan_total += loan
loan_average = (loan_total / number_of_loans)
loan_var = 0
loan_stdev = 0
for loan in loan_amount:
    loan_var += (((loan - loan_average) ** 2) / len(loan_amount))
loan_stdev = sqrt(loan_var)

# covariance and pearson's correlation
loan_amount_num_lenders = 0
loan_amount_ttr = 0
num_lenders_ttr = 0

number_of_loans = len(loan_amount)
loan_total = 0
loan_average = 0
for loan in loan_amount:
    loan_total += loan
loan_average = (loan_total / number_of_loans)

number_of_times = len(time_to_raise)
time_total = 0
time_average = 0
for time in time_to_raise:
    time_total += time
time_average = (time_total / number_of_times)

loan_var = 0
loan_stdev = 0
for loan in loan_amount:
    loan_var += (((loan - loan_average) ** 2) / len(loan_amount))
loan_stdev = sqrt(loan_var)

time_var = 0
time_stdev = 0
for time in time_to_raise:
    time_var += (((time - time_average) ** 2) / len(loan_amount))
time_stdev = sqrt(time_var)

for index in range(len(loan_amount)):
    covar = ((loan_amount[index] - loan_average) * (time_to_raise[index] - time_average) / len(loan_amount))
loan_amount_ttr = (covar / (loan_stdev * time_stdev))
print(loan_amount_ttr)
