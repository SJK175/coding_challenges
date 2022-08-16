#basic building block of FOR loop :
#create email IDs for the list of names with domain : xyz.com
name_list = ["subhajit", "arijit", "barry", "jaydeep", "suman"]

j = 0
for i in name_list :
  print(name_list[j] + "@xyz.com")
  j += 1

print ("--") 
print ("here's the list of all email IDS")  
