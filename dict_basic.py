#work on an example that use python dictionary
#give an user defined comment if the key is not valid.

email_list = {
"IN123" : "avik@xyz.com",
"IN456" : "subha@xyz.com",
"IN827" : "shovik@xyz.com",
"IN098" : "suman@xyz.com",
"IN625" : "jaydeep@xyz.com"
}

print(email_list["IN123"])
print(email_list.get("IN450","not a valid key"))
