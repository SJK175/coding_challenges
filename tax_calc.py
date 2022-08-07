#####calculate monthly tax#########################
#deduction rule : 
#Long term savings : maximum 150000
#medical exp : max 10% of income
#child_education : max 15% of income
#establishment cost (rent/emi) : max 25% of income
#tax rule after deduction :
#upto 500000 : no tax
#500000-1000000 : 10% of income
#1000000-2000000 : 20% of income
#2000000 plus : 25% of income
###################################################

#income and deduction claimed
income = float(input("Total income : " ))
long_term_sav = float(input("Total savings in 80C : "))
medical = float(input("medical exp : "))
child_edu = float(input("child education cost : "))
rent_emi = float(input("rent/home emi given : "))

#tax slabs
slab_one = 500000
slab_one_tax = 0
slab_two = 1000000
slab_two_tax = 0.1
slab_three = 2000000
slab_three_tax = 0.2
slab_four_tax = 0.25

#deduction limits 
long_term_sav_max = 150000
medical_max = income*0.1
child_edu_max = income*0.15
rent_emi_max = income*0.25

#calculating tax deduction
long_term_sav_deduct = min(long_term_sav,long_term_sav_max)
medical_deduct = min(medical,medical_max)
child_edu_deduct = min(child_edu,child_edu_max)
rent_emi_deduct = min(rent_emi,rent_emi_max)
total_deduct = long_term_sav_deduct+medical_deduct+child_edu_deduct+rent_emi_deduct

#tax calculation
tax_income = income - total_deduct

if tax_income < 0:
  print("verify your deduction claims")
  Y_tax = 0
elif tax_income <= slab_one :
  Y_tax = tax_income * slab_one_tax
elif tax_income > slab_one and tax_income <= slab_two :
  Y_tax = tax_income * slab_two_tax
elif tax_income > slab_two and tax_income <= slab_three :
  Y_tax =  tax_income * slab_three_tax
elif tax_income > slab_three :
  Y_tax =  tax_income * slab_four_tax
else :
  print("verify your income & deductions with your HR")

print("---------------")
print("---------------")
print("your total deductions are INR: " +  str(round(total_deduct)))
print("your taxable income is INR: " +  str(round(tax_income)))
print("your yearly tax would be aproximately: " +  str(round(Y_tax)))
print("your monthly tax would be aproximately INR: " + str(round(Y_tax/12)))
print("please contact your HR in case you need any clarification.")
print("---------------")
print("---------------")







