salary = [12,16,24,33]
name = ["mat","joe","sam","bob"]
name.append("rainer")
name.extend(salary)
name.insert(2,"subhajit")
name.remove("sam")
salary.sort()
#name.clear() will clear the list
name2 = name.copy()

print(name)
print(name.index("subhajit"))
print(name.count("subhajit"))
print(salary)
print(name2)
#print(name_salary)

