import os.path

def getThetas():
    if os.path.isfile('theta/theta0.txt'):
        with open('theta/theta0.txt', 'r') as fTheta0:
            theta0 = fTheta0.read()
    else: theta0 = 0
    
    if os.path.isfile('theta/theta1.txt'):
        with open('theta/theta1.txt', 'r') as fTheta1:
            theta1 = fTheta1.read()
    else: theta1 = 0

    return theta0, theta1


def estimatePrice(mileage):

    theta0 = 0
    theta1 = 0
    estPrice = theta0 + (theta1 * mileage)
    return estPrice

theta0, theta1 = getThetas()

print(theta0, theta1)

# miles = input("Enter mileage : ")
# estPrice = estimatePrice(int(miles))
# print("The estimated price is :", estPrice)
