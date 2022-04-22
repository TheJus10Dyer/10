#Justin Dyer
#proj1.py
#J00655685



import math
import numpy as np
import matplotlib.pyplot as plt

#define the function of dv_over_dt
def dv_over_dt(g, c, m, v):
    dfdt = g - c/m *v
    return dfdt

#define the function of v_exact
def v_exact_func(g, c, m, t):
    v = g*m/c*(1.0 - math.exp(-1.0*c/m*t))
    return v

#define the error analysis function
def truePerRelError(t_values, num_values, exact_values, ErrorCompareAtTime):
    for i in range (0, len(t_values)):
        if t_values[i] < ErrorCompareAtTime and t_values[i+1] >= ErrorCompareAtTime:
            num_val_compare = num_values[i+1]
            exact_val_compare = exact_values[i+1]
            if exact_val_compare != 0.0:
                truePercentRelativeError = (exact_val_compare - num_val_compare)/exact_val_compare
            else:
                truePercentRelativeError = math.nan

    return truePercentRelativeError, num_val_compare, exact_val_compare

#define the function to display key results on screen
def display_values(t, v_euler, v_exact, truePercentRelativeError, percentRelativeError):
    print('Display the results...')
    length = len(t)
    print('____i____ ____t_____ __v_euler__ __v_exact__ ')
    for i in range(0, length):
        print('{:10d}'.format(i), '{:10.6f}'.format(t[i]), '{10.6f}'.format(v_euler[i]), '{:10.6f}'.format(v_exact[i]) )

    print('truePercentRelativeError = ', truePercentRelativeError)
    print('percentRelativeError = ', percentRelativeError)
    return 1

#define the function to plot and display/save the figure
def plotSaveResultsInOneFigure(t, v_euler, v_exact, dt, truePercentRelativeError, v_euler_compare, v_exact_compare, at_t):
    plt.plot(t, v_euler, 'o-', t, v_exact, '-x') #plot two curves for v_euler and v_exact
    plt.legend(('v_Explicit Euler Method', 'v_Exact Solution'), loc = 0)
    plottitle = 'Parachutist velocity vs time (dt = ' + str(dt) + 's)'
    plt.title(plottitle)
    textshown = '@t = ' + str(at_t) + 's' + '\n True Percent Relative Error = ' + str(truePercentRelativeError*100) + '%' \
                + '\n v_Euler = ' + str(v_euler_compare) + ' m/s' \
                + '\n v_Exact = ' + str(v_exact_compare) + ' m/s'

    plt.text(10.0, 10.0, textshown)
    plt.xlabel('t (s)') #label of x-axis
    plt.ylabel('Velocity (m/s)')#label of y-axis
    plt.grid(True) #add grid
    plotFileName = 'plot_dt' + str(dt) + '.jpg'
    plt.savefig(plotFileName, format = 'jpg') # save plot in a jpg format file
    plt.show() #show the plot on screen
    return 1

#initial conditions and constants
g = 9.8
c = 12.5
m = 68.1

#create a dt input
dt = float(input('Input the time step. dt = '))
print('dt = ', dt, 'seconds')
num_of_points = int((100 - 100%dt)/dt) + 1
print('Number of data points = ', num_of_points)
t = [0.0]
v_euler = [0.0]
v_exact = [0.0]
ErrorCompareTime = 20.0

#create data for the plot
i = 0
while i < int(num_of_points - 1):
    t.append(float(t[i]+dt))
    v_euler.append(float(v_euler[i] + dv_over_dt(g, c, m, v_euler[i])*dt))
    v_exact.append(float(v_exact_func(g, c, m, t[i+1])))
    i = i+1

#define the comparison
truePercentRelativeError, v_euler_compare, v_exact_compare = truePerRelError(t, v_euler, v_exact, ErrorCompareTime)

#plot ad save results
plotSaveResultsInOneFigure(t, v_euler, v_exact, dt, truePercentRelativeError, v_euler_compare, v_exact_compare, ErrorCompareTime)

input('\nPress Return to exit')