#basic building block of WHILE loop :
#create email IDs for the list of names with domain : xyz.com
name_list = ["subhajit", "arijit", "barry", "jaydeep", "suman"]
i = 0
while i <= len(name_list)-1 :
  print(name_list[i] + "@xyz.com")
  i += 1
