from GradientDescent import GradientDescent
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=2, horizontal_spacing=0.05, vertical_spacing=0.1, subplot_titles=("Learning rate of 0.1", "Iterations : 1000", "Learning rate of 0.01", "Iterations : 3000", "Learning rate of 0.001", "Iterations : 6000",),
                                    specs=[[{"secondary_y": False}, {"secondary_y": True}],
                                            [{"secondary_y":False}, {"secondary_y": True}],
                                            [{"secondary_y":False}, {"secondary_y": True}]])

learn = GradientDescent('files/data.csv', iterations=1000, learningRate=0.1)
learn.doGradientDescent()

fig.add_trace(go.Scatter(x=learn.normalizedX, y=learn.normalizedY, mode='markers'), row=1, col=1)
for i in range(len(learn.theta0History)):
    if(i <= 500 or (i > 500 and i % 50 == 0)):
        fig.add_trace(go.Scatter(x=learn.normalizedX, y=learn.estimatePrice(learn.normalizedX, learn.theta0History[i], learn.theta1History[i])), row=1, col=1)

fig.add_trace(go.Scatter(y=learn.costHistory), row=1, col=2, secondary_y=False)
fig.add_trace(go.Scatter(y=learn.theta0History), row=1, col=2, secondary_y=True)
fig.add_trace(go.Scatter(y=learn.theta1History), row=1, col=2, secondary_y=True)

del learn

learn = GradientDescent('files/data.csv', iterations=3000, learningRate=0.01)
learn.doGradientDescent()

fig.add_trace(go.Scatter(x=learn.normalizedX, y=learn.normalizedY, mode='markers'), row=2, col=1)
for i in range(len(learn.theta0History)):
    if(i <= 500 or (i > 500 and i % 10 == 0)):
        fig.add_trace(go.Scatter(x=learn.normalizedX, y=learn.estimatePrice(learn.normalizedX, learn.theta0History[i], learn.theta1History[i])), row=2, col=1)

fig.add_trace(go.Scatter(y=learn.costHistory), row=2, col=2, secondary_y=False)
fig.add_trace(go.Scatter(y=learn.theta0History), row=2, col=2, secondary_y=True)
fig.add_trace(go.Scatter(y=learn.theta1History), row=2, col=2, secondary_y=True)

del learn

learn = GradientDescent('files/data.csv', iterations=6000, learningRate=0.001)
learn.doGradientDescent()

fig.add_trace(go.Scatter(x=learn.normalizedX, y=learn.normalizedY, mode='markers'), row=3, col=1)
for i in range(len(learn.theta0History)):
    if(i <= 500 or (i > 500 and i % 10 == 0)):
        fig.add_trace(go.Scatter(x=learn.normalizedX, y=learn.estimatePrice(learn.normalizedX, learn.theta0History[i], learn.theta1History[i])), row=3, col=1)

fig.add_trace(go.Scatter(y=learn.costHistory), row=3, col=2, secondary_y=False)
fig.add_trace(go.Scatter(y=learn.theta0History), row=3, col=2, secondary_y=True)
fig.add_trace(go.Scatter(y=learn.theta1History), row=3, col=2, secondary_y=True)

fig.update_layout(showlegend=False)

fig.show()
