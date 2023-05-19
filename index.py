from datetime import date, timedelta


class user():
    name = ""
    bookings = []

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
        print(self.bookings)


def bookunit():
    c = int(input("Enter the choice:\n1 for hours\n2 for days\n3 for weeks\n"))
    n = int(input("Enter the amount:"))
    if (c == 1):
        return (n*5)
    elif (c == 2):
        return (n*20)
    elif (c == 3):
        return (60*n)
    else:
        print("Invalid Choice")


def booking(ob):
    n = int(input("How many bikes do you want to book?:"))
    time = str(date.today())
    lst = [time]
    for i in range(0, n):
        print("For bike:", (i+1))
        lst.append(bookunit())
    total = 0
    for i in lst[1:]:
        total += int(i)
    if (n > 3):
        choice = input("Do you want to get the Family discount:")
        if (choice == "yes" or choice == "Yes" or choice == "Y"):
            total = 0.3*total
    lst.append(total)
    ob.bookings.append(lst)


def bill(ob):
    f = open("Bill.txt", "w")
    lst = ob.bookings
    nam = ob.name
    L = (str(nam)+"\n"+str(lst[0])+"\n"+str(lst[1:-1])+"\n"+str(lst[-1]))
    f.writelines(L)


u1 = user("Swaraj")
booking(u1)
bill(u1)
