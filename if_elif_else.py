##############
#define user roles based on certain set of conditions :
##############
#(user role) is given to all LINDE GAS users.
#(special user role) is given to all LINDE REGION CONFIG MANAGERS.
#(admin role) is given to only Global CMS team members
#(special admin role) is given to only Global CMS team manager
#all/any roles needs to be revoked as soon as someone leave the company.__doc__

member_status = "active"
member_dpt = "LG"
member_team = "CMDB"
is_global = False
is_manager = True

if member_status == "active" :
  
  if member_dpt == "LG" and member_team == "CMDB" and is_global :
    if is_manager :
      print("special admin role")
    else :
      print("admin role") 
  elif member_dpt == "LG" and member_team == "CMDB" and not(is_global) :
    if is_manager :
      print("special user role")
    else :
      print("user role")
  elif member_dpt == "LG" :
    print("user role")
  else :
    print("currently no role is allocated to "+ member_dpt + " users" )

else:
  print("user is not active")





