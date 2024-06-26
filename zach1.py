#years_13 = set(range(1978, 3000, 13))
years_17 = set(range(1978, 2051, 17))

common_years = years_13 & years_17

sorted_years = sorted(common_years)
print(sorted_years)
