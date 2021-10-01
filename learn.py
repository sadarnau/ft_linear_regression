import pandas

class GradientDescent:

    def __init__(self, iterations=2000, learningRate=0.1):
        self.theta0 = 0
        self.theta1 = 0
        self.nomalizedTheta0 = 0
        self.nomalizedTheta1 = 0
        self.x
        self.y
        self.normalizedX
        self.normalizedy
        self.lenData = 0
        self.data = self.getData()
        self.iterations = iterations
        self.learningRate = learningRate

    def normalizer(values):

        normalizedValues = (values - min(values)) / (max(values) - min(values))

        return normalizedValues

    def processData():
        # TO DO : to protect
        self.data = pandas.read_csv('data.csv')
        self.x = self.data['km'].values
        self.y = self.data['price'].values
        self.normalizedX = self.normalizer(self.x)
        self.normalizedy = self.normalizer(self.y)

    def estimatePrice(x, theta0, theta1):

        y = theta0 + theta1 * x

        return y

    def doGradientDescent():

        for i in range(self.iterations):
            total1 = 0
            total2 = 0

            for i in range(self.lenData):
                
                # TO DO : take of useless bracket
                total1 -= self.estimatePrice(self.normalizedX[i], self.nomalizedTheta0, self.nomalizedTheta1) \
                    - self.normalizedy[i]
                total2 -= (self.estimatePrice(self.normalizedX[i], self.nomalizedTheta0, self.nomalizedTheta1) \
                    - self.normalizedy[i]) * self.normalizedX[i]

            m += learningRate * (s2 / len(x_points))
            b += learningRate * (s1 / len(x_points))

            # if(i < 500) or (i > 500 and i % 10 == 0):
            #     plt.plot(x_points, function(x_points, b, m))


        return b, m