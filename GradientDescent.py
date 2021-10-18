import pandas, os.path
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
import plotly.graph_objects as go
import plotly.express as px

class GradientDescent:

    def __init__(self, pathData, iterations=2000, learningRate=0.05):
        self.theta0 = 0
        self.theta1 = 0
        self.normalizedTheta0 = 0
        self.normalizedTheta1 = 0
        self.x = 0
        self.y = 0
        self.normalizedX = 0
        self.normalizedY = 0
        self.lenData = 0
        self.data = self.processData(pathData)
        self.iterations = iterations
        self.learningRate = learningRate
        self.costHistory = []
        self.theta0History = []
        self.theta1History = []
    
    def processData(self, pathData):
        if not os.path.isfile(pathData):
            print("Wrong path for the data file")
            exit(1)

        self.data = pandas.read_csv(pathData)
        self.x = self.data['km'].values
        self.y = self.data['price'].values
        if (len(self.x) != len(self.y)) or len(self.x) == 0:
            print("Data file is no gooood")
            exit(1)

        self.normalizedX = self.normalizer(self.x)
        self.normalizedY = self.normalizer(self.y)        
        self.lenData = len(self.x)

    def normalizer(self, values):

        normalizedValues = (values - min(values)) / (max(values) - min(values))

        return normalizedValues

    def denormalizer(self):
        self.theta1 = (max(self.y) - min(self.y)) * self.normalizedTheta1 / (max(self.x) - min(self.x))
        self.theta0 = min(self.y) + ((max(self.y) - min(self.y)) * self.normalizedTheta0) + self.theta1 * (1 - min(self.x))

    def estimatePrice(self, x, theta0, theta1):

        y = theta0 + theta1 * x

        return y

    def addCostHistory(self):        

        tot = 0
        for i in range(self.lenData):
            tot += (self.estimatePrice(self.normalizedX[i], self.normalizedTheta0, self.normalizedTheta1) - self.normalizedY[i])**2

        cost = tot / (2 * self.lenData)
        self.costHistory.append(cost)

    def saveThetas(self):
        with open('files/thetas.txt', 'w') as f:
            f.write(str(self.theta0))
            f.write('\n')
            f.write(str(self.theta1))

    def doGradientDescent(self):

        for i in range(self.iterations):
            total1 = 0
            total2 = 0

            for j in range(self.lenData):
                total1 -= self.estimatePrice(self.normalizedX[j], self.normalizedTheta0, self.normalizedTheta1) \
                    - self.normalizedY[j]
                total2 -= (self.estimatePrice(self.normalizedX[j], self.normalizedTheta0, self.normalizedTheta1) \
                    - self.normalizedY[j]) * self.normalizedX[j]

            self.normalizedTheta0 += self.learningRate * (total1 / self.lenData)
            self.normalizedTheta1 += self.learningRate * (total2 / self.lenData)
            self.theta0History.append(self.normalizedTheta0)
            self.theta1History.append(self.normalizedTheta1)
            self.addCostHistory()

        self.denormalizer()
        self.saveThetas()

if __name__ == "__main__":

    learn = GradientDescent('files/data.csv')
    learn.doGradientDescent()
    
    # fig = px.scatter(x=learn.x, y=learn.y)

    # create a list of frames
    frames = []
    points = go.Scatter(x=learn.normalizedX, y=learn.normalizedY, mode='markers')

    for i in range(len(learn.theta0History)):

        line = go.Scatter(x=learn.normalizedX, y=learn.estimatePrice(learn.normalizedX, learn.theta0History[i], learn.theta1History[i]))    # create the button

        button = { "type": "buttons", "buttons": [{ "label": "Play", "method": "animate", "args": [None, {"frame": {"duration": 1}}]}]}

        layout = go.Layout(updatemenus=[button], title_text=f"Gradient Descent Step {i}")    # create a frame object

        frame = go.Frame(data=[points, line], layout=go.Layout(title_text=f"Gradient Descent Step {i}",
                            xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1])))

        frames.append(frame)
    
    # combine everything together
    fig = go.Figure(data=[points, line],
                    frames=frames,
                    layout = layout)
                                    
    fig.show()

    print(f'\ntheta0 = {learn.theta0} and theta1 = {learn.theta1}\n')
    
    # plt.title('Iterations of the gradient descent algorithm')
    # plt.plot(learn.normalizedX, learn.normalizedY, 'bo')
    # plt.ylabel('Normalized price')
    # plt.xlabel('Normalized mileage')

    # fig.add_subplot(222)
    # plt.title('The linear regression found')
    # plt.plot(learn.x, learn.y, 'bo')
    # plt.plot(learn.x, learn.estimatePrice(learn.x, learn.theta0, learn.theta1))
    # plt.ylabel('Price')
    # plt.xlabel('Mileage (Km)')

    # fig.add_subplot(212)
    # color='tab:blue'
    # plt.plot(learn.theta0History, label='$\\theta_{0}$', linestyle='-', color=color)
    # plt.plot(learn.theta1History, label='$\\theta_{1}$', linestyle='--', color=color)
    # plt.xlabel('Iterations'); plt.ylabel('$\\theta$', color=color)
    # plt.tick_params(axis='y', labelcolor=color)
 
    # color='tab:red'
    # ax2 = plt.twinx()
    # ax2.plot(learn.costHistory, label='Cost function', color=color)
    # ax2.set_title('Values of $\\theta$ and cost function over iterations')
    # ax2.set_ylabel('Cost', color=color)
    # fig.legend(bbox_to_anchor=(0.9, 0.4))

    # plt.show()
