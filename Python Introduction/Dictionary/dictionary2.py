student_id = {
    101: "Tony Stark",
    102: "Thor Odin son",
    103: "Captain Steve Rogers",
    104: "Bruce Banner",
    105: "Natasha Romanof",
    106: "Carol Danvers",
    107: "Scott Lang",
    108: "Peter Parker",
    109: "Dr. Stephen Strange",
    110: "Nick Fury",
}

n = int(input("Enter your id => "))

print(student_id.get(n, "Invalid Id !!!"))

# ? if user input is not in the dictionary then it will print "Invalid Id !!!"
