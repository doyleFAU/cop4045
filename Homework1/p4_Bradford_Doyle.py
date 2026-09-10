import math
import matplotlib.pyplot as plt
#plots a functions given by the user
def plot_function(fun_str, domain, ns):
    xmin = domain[0]
    xmax = domain[1]

    x_val = []
    y_val = []

##makes the space between the x value
    step = (xmax - xmin) / (ns - 1)
    i = 0
#makes the lists of the x and y values
    while i < ns:
        x =xmin + i * step
        x_val.append(x)
        y = eval(fun_str)
        y_val.append(y)
        i = i + 1

#makes top of table
    print("x, y")
    print("----------------------------------------------------")
    k = 0
    while k < len(x_val):
        line = "{:.4f}, {:+.4f}".format(x_val[k], y_val[k])
        print(line)
        k = k + 1

#makes the graph
    plt.plot(x_val, y_val, 'o-')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("function graph")
    plt.show()

#gets input from the user
fun_str = input("enter function with variable x: ")
ns = int(input("enter number of samples: "))
xmin = float(input("enter xmin:"))
xmax = float(input("enter xmax:"))
plot_function(fun_str, (xmin, xmax), ns)

