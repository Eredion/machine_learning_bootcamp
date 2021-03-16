import numpy as np
from matplotlib import pyplot as plt


def cost_(y, y_hat):
    if type(y_hat) != np.ndarray or type(y) != np.ndarray or y.ndim != 1\
            or y_hat.ndim != 1 or len(y_hat) != len(y):
        return None
    else:
        return(np.dot((1 / (len(y)))*(y_hat - y), (y_hat - y)))


def add_intercept(x):
    if type(x) == np.ndarray and x.size > 0 and x.ndim == 1:
        y = np.ones(x.size,)
        return(np.array([y, x]).transpose())
    else:
        return (None)


def simple_predict(x, theta):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2:
        return None
    else:
        x = add_intercept(x)
        return (x @ theta)


def plot_with_cost(x,  y, theta):
    if type(theta) != np.ndarray or type(x) != np.ndarray or x.ndim != 1\
            or theta.ndim != 1 or len(theta) != 2 or type(y) != np.ndarray\
            or y.ndim != 1 or len(y) != len(x):
        return None
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x, y, 'o')
        y_hat = simple_predict(x, theta)
        for i in range(0, len(y)):
            ax.plot([x[i], x[i]], [y[i], y_hat[i]],
                    linestyle='--', color='red')
            ax.plot(x, theta[1] * x + theta[0])
            ax.set_title(cost_(y, y_hat))
            plt.show()

if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([11.52434424, 10.62589482, 13.14755699,
                  18.60682298, 14.14329568])
    theta1 = np.array([18, -1])
    plot_with_cost(x, y, theta1)

    theta2 = np.array([14, 0])
    plot_with_cost(x, y, theta2)

    theta3 = np.array([12, 0.8])
    plot_with_cost(x, y, theta3)
