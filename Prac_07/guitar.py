from Prac_07.guitarClass import Guitar


guitars = []


def main():

#    name = input("Name: ")
#       year = int(input("Year: "))
#        cost = int(input("Cost: "))
#        add_guitar = Guitar(name, year, cost)
#        guitars.append(add_guitar)
#        print(add_guitar, "added")
#        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

#    guitars.sort()

    i = -1
    for guitar in guitars:
        i += 1
        word_vintage = ''
        if guitar.is_vintage():
            word_vintage = "(Vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, word_vintage))
main()