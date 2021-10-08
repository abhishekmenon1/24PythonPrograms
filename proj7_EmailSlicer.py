"""
The program helps get you the username and domain name from an email address.
You can even customize the application and send a message to the host with this information.
"""


email = input("\nEnter Your Office email(e.g. micheal.scott@dundermifflin.com) \n--> ")
firstName = []
lastName = []
company = []

for i in range(len(email)):
    if email[i] == "." or email[i] == "_":
        for j in range(i+1, len(email)):
            lastName.append(email[j])
            if email[j] == "@":
                break

    elif email[i] == "@":
        for k in range(i+1, len(email)):
            company.append(email[k])

            if email[k] == ".":
                break

for a in range(len(email)):
    firstName.append(email[a])
    if email[a] == "." or email[a] == "_" or email[a] == "@":
        break

firstName = firstName[:-1]
#print((firstName))

lastName = lastName[:-4]
#print("".join(lastName))

company = company[:-1]
#print("".join(company))

print("----\nHello","".join(firstName),"".join(lastName),"!\nHow is work at","".join(company),"been so far?" )