import os.path

def getThetas():
    if os.path.isfile('files/thetas.txt'):
        with open('files/thetas.txt', 'r') as f:
            theta0 = f.read()
        print("\ntheta0 is", theta0)
    else:
        print("\nThetas file was not found so the default value of 0 will be taken\n")
        theta0 = 0
        theta1 = 0

    # if os.path.isfile('theta/theta1.txt'):
    #     with open('theta/theta1.txt', 'r') as f:
    #         theta1 = f.read()
    #     print("\ntheta1 is", theta1, '\n')
    # else:
    #     print("\ntheta1 was not found so it will take a value of 0\n")
    #     theta1 = 0

    return theta0, theta1


def estimatePrice(mileage):

    estPrice = theta0 + (theta1 * mileage)

    return estPrice

theta0, theta1 = getThetas()

miles = input("Enter mileage : ")   # TO DO : PROTECT ONLY INT
estPrice = estimatePrice(int(miles))
print("\nThe estimated price is :", estPrice, '\n')
