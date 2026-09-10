import math
import matplotlib.pyplot as plt
while True: 
    #gets usersinput for coefficiant a and sets it to a float
    a_input = input("Enter a : ")
    if a_input == "":
        break
    a = float(a_input)

#gets usersinput for coefficiant b and sets it to a float
    b_input = input("Enter b : ")
    if b_input == "":
        break
    b = float(b_input)

#gets usersinput for coefficiant c and sets it to a float
    c_input = input("Enter c : ")
    if c_input == "":
        break
    c = float(c_input)

#determines the discriminant and uses it to determine the number of solutios
    D = b**2 - 4*a*c
    if D < 0:
       print("no real solutions")

       xOpt = -b/(2*a)
       xMin = xOpt - 3
       xMax = xOpt + 3

#determines if there is one solution and caluculates teh x value
    elif D == 0:
        x1 = -b / (2*a)
        print("one solution: {:.5f}".format(x1))

        xMin = x1 - 2
        xMax = x1 + 2


#dtermines if there are 2 soutions and calculates the x values
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("two solutions: x1={:.5f} x2={:.5f}".format(x1, x2))

        xMin = min(x1, x2) - 2
        xMax = max(x1, x2) + 2

#creates a list of x values and y values to plot the graph of the quadratic function
    step = (xMax - xMin) / 149
    xVal = []
    yVal = []
    for i in range(150):
    
        x = xMin + i * step
        xVal.append(x)
        yVal.append(a*x**2 + b*x + c) 

    #plots the graph of the quadratic function using matplotlib
    plt.plot(xVal, yVal, 'o-')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
