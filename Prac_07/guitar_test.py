from Prac_07.guitarClass import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)


def get_age(guitar1):
    age = 2017 - guitar1.year
    return age


def is_vintage(age):
    if age >= 50:
        return True


def main():
    print (is_vintage(get_age(guitar1)))


main()