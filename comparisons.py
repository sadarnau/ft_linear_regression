import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from GradientDescent import GradientDescent

fig = figure(figsize=(20, 15), dpi=80)
fig.add_subplot(321)

learn = GradientDescent('files/data.csv', iterations=1000, learningRate=0.1)
learn.doGradientDescent()

print(f'\ntheta0 = {learn.theta0} and theta1 = {learn.theta1}\n')

plt.title('Learning rate of 0.1')
plt.plot(learn.normalizedX, learn.normalizedY, 'bo')

fig.add_subplot(322)
plt.title('Iteration : 1000')
plt.plot(learn.costHistory)

del learn

fig.add_subplot(323)
learn = GradientDescent('files/data.csv', iterations=3000, learningRate=0.01)
learn.doGradientDescent()

plt.title('Learning rate of 0.01')
plt.plot(learn.normalizedX, learn.normalizedY, 'bo')

fig.add_subplot(324)
plt.title('Iteration : 3000')
plt.plot(learn.costHistory)

del learn

fig.add_subplot(325)
learn = GradientDescent('files/data.csv', iterations=6000, learningRate=0.001)
learn.doGradientDescent()

plt.title('Learning rate of 0.001')
plt.plot(learn.normalizedX, learn.normalizedY, 'bo')

fig.add_subplot(326)
plt.title('Iteration : 6000')
plt.plot(learn.costHistory)


plt.show()