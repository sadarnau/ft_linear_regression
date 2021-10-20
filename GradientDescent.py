import pandas, os.path
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

    def showGraph(self):
        # create a list of frames
        frames = []
        
        fig = make_subplots(rows=1, cols=2)
        
        points = go.Scatter(x=self.normalizedX, y=self.normalizedY, mode='markers',showlegend=False)

        for i in range(len(self.theta0History)):

            line = go.Scatter(x=self.normalizedX, y=self.estimatePrice(self.normalizedX, self.theta0History[i], self.theta1History[i]), showlegend=False)

            button = { "type": "buttons", "buttons": [{ "label": "Play", "method": "animate", "args": [None, {"frame": {"duration": 1}}]}]}

            layout = go.Layout(updatemenus=[button], title_text=f"Gradient Descent Step {i}")

            frame = go.Frame(data=[points, line], layout=go.Layout(title_text=f"Gradient Descent Step {i}",
                                xaxis=dict(range=[0, 1]), yaxis=dict(range=[0, 1])))

            frames.append(frame)
        
        # combine everything together
        fig = go.Figure(data=[points, line], frames=frames, layout = layout)
        fig.set_subplots(rows=2, cols=2, specs=[[{}, {}],[{"colspan": 2, "secondary_y": True}, None]],
            subplot_titles=("iterations", "Linear regression applyed to the dataset", 'Values of thetas and cost function over iterations'),
            horizontal_spacing=0.1, vertical_spacing=0.1)


        fig.add_trace(go.Scatter(x=self.x, y=self.y, mode='markers',showlegend=False), row=1, col=2)
        fig.add_trace(go.Scatter(x=self.x, y=self.estimatePrice(self.x, self.theta0, self.theta1),showlegend=False), row=1, col=2)
        fig.update_xaxes(title_text="Mileage (km)", row=1, col=2)
        fig.update_yaxes(title_text="Price ($)", row=1, col=2)


        fig.add_trace(go.Scatter(name="Cost function", y=self.costHistory), row=2, col=1, secondary_y=False)
        fig.add_trace(go.Scatter(name="Theta0",y=self.theta0History), row=2, col=1, secondary_y=True)
        fig.add_trace(go.Scatter(name="Theta1",y=self.theta1History), row=2, col=1, secondary_y=True)
        fig.update_xaxes(range=[-10, 2050], row=2, col=1,title_text="Iterations")
        fig.update_yaxes(title_text="Cost", secondary_y=False, row=2, col=1)
        fig.update_yaxes(title_text="Theta value", secondary_y=True)

        fig.update_layout(legend=dict( y=0.25, x=0.75))
        fig.show()

if __name__ == "__main__":

    learn = GradientDescent('files/data.csv')
    learn.doGradientDescent()
    learn.showGraph()

    print(f'\ntheta0 = {learn.theta0} and theta1 = {learn.theta1}\n')
