# Parse through the portions of an email address and print the username and domain name.
#Name: Ziling He
#Date: Sep. 18, 2026

#Method 1 : Using split
email_address = input("Enter an email address: ")
parts = email_address.split("@")
username = parts[0]
domain_name = parts[1]

print("parts of the email address:", parts)
print("Username:", username)
print("Domain name:", domain_name)


#Method 2 : Using index and slicing
at_sign_index = email_address.index("@")
username2 = email_address[:at_sign_index]
domain_name2 = email_address[at_sign_index + 1:]

print("Username (method2):", username2)
print("Domain name (method2):", domain_name2)
