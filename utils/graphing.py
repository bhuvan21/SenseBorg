import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ConfigurableGraph:

    def __init__(self, var, yrange=None):
        self.var = var
        self.x_len = 200
        if yrange == None:
            self.y_range = [0, 1]
        else:
            self.y_range = yrange

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.xs = list(range(0, self.x_len))
        self.ys = [0] * self.x_len
        self.ax.set_ylim(self.y_range)

        self.line, = self.ax.plot(self.xs, self.ys)

        plt.title("Variable")
        plt.xlabel('Samples')
        plt.ylabel('V')

        plt.show()

    def animate(self, i, ys): 
        self.ys.append(self.var())
        self.ys = self.ys[-self.x_len:]
        self.line.set_ydata(self.ys)

        return self.line,
