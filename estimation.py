import os.path

def getThetas():
    if os.path.isfile('files/thetas.txt'):
        with open('files/thetas.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) == 2:
                theta0 = float(lines[0])
                theta1 = float(lines[1])
            else: print("Thetas file is corrupted")
        print("\ntheta0 =", theta0)
        print("\ntheta1 =", theta1, '\n')
    else:
        print("\nThetas file was not found so the default value of 0 will be taken\n")
        theta0 = 0
        theta1 = 0

    return theta0, theta1


def estimatePrice(mileage):

    estPrice = theta0 + (theta1 * mileage)

    return estPrice

theta0, theta1 = getThetas()

miles = input("Enter mileage : ")

try:
    estPrice = estimatePrice(int(miles))
except:
    print("\nOnly numbers plzz\n")
    exit(1)

if estPrice < 0:
    print('\nSorry, your car is worth nothing...\n')
else:
    print("\nThe estimated price is :", estPrice, '\n')
