import pandas
import pandas
import matplotlib.pyplot as plt

def normalizer(x):

    normalizedX = (x - min(x)) / (max(x) - min(x))

    return normalizedX

def denormalizer(normalizedX, x):

    denormalizedX = min(x) + normalizedX * (max(x) - min(x))

    return denormalizedX

def function(x, b, m): 
    
    y = m * x + b
    return y

def summation(b, m, x_points, y_points):

    total1 = 0
    total2 = 0
    
    for i in range(1, len(x_points)):
        
        total1 -= function(x_points[i], b, m) - y_points[i]
        total2 -= (function(x_points[i], b, m) - y_points[i]) * x_points[i]

    return total1, total2

def gradientDescent(x_points, y_points, b, m, learningRate=0.1, iterations=2000):

    for i in range(iterations):
        s1, s2 = summation(b, m, x_points, y_points)
        m += learningRate * (s2 / len(x_points))
        b += learningRate * (s1 / len(x_points))

        # if(i < 500) or (i > 500 and i % 10 == 0):
        #     plt.plot(x_points, function(x_points, b, m))

    return b, m


m, b = 0, 0

df = pandas.read_csv('data.csv')
x_points = df['km'].values
y_points = df['price'].values

normalizedX = normalizer(x_points)
normalizedY = normalizer(y_points)

b, m = gradientDescent(normalizedX, normalizedY, b, m)

theta_1 = (max(y_points) - min(y_points)) * m / (max(x_points) - min(x_points))
theta_0 = min(y_points) + ((max(y_points) - min(y_points)) * b) + theta_1 * (1 - min(x_points))

print(denormalizer(b, y_points))
print(theta_0)
print(theta_1)

plt.plot(x_points, y_points, 'bo')
plt.plot(x_points, function(x_points, denormalizer(b, y_points), theta_1))
plt.plot(x_points, function(x_points, theta_0, theta_1))


plt.show()

