from Prac_08.taxi import Taxi


def main():
    prius = Taxi('Prius', 100)
    prius.drive(40)
    print(prius)
    print("The current fair is ${}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print("The current fair is ${}".format(prius.get_fare()))


main()
