print("Full Name: Daylle Munsayac") 
print("Student ID: 12345678") 
print("Date and time: ", datetime.datetime.now ())

issue = input("Describe a networking issue: ") 

with open("networking_issue.txt","w") as file: file.write(issue + "\n")

