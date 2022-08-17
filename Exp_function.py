# create an exponent function using loop

for i in range(6) :
  print(i)

def exp_fun(base, pow) :
  result = 1
  for i in range(pow) :
    result = result * base
  return result


test = exp_fun(3,100)  
print(test)
