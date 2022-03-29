import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
import matplotlib.animation as animate
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk
        )

import db_actions as db
import os


matplotlib.use('TkAgg')

ax = None
#expiry_date, contract1, contract2, index = None, None, None, None

'''
def init_plot(index, expiry_date, contract1, contract2):

    db.populate_db(index, expiry_date, contract1, contract2)

    time_stamp, strike1_oi, strike2_oi = db.fetch_data()

    ax.plot(time_stamp, strike1_oi, label=f'{contract1}', color='orange')
    ax.plot(time_stamp, strike2_oi, label=f'{contract2}', color='purple')
    ax.scatter([time_stamp[-1]], [strike1_oi[-1]], marker='o', color='orange')
    ax.scatter([time_stamp[-1]], [strike2_oi[-1]], marker='o', color='purple')
    ax.legend()

    return
'''

def draw_plot(index, expiry_date, contract1, contract2):

    db.populate_db(index, expiry_date, contract1, contract2)

    time_stamp, strike1_oi, strike2_oi= db.fetch_data()

    ax.cla()

    #ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

    ax.tick_params(axis='x', rotation=70)

    ax.plot(time_stamp, strike1_oi, label=f'{contract1}', color='orange')
    ax.plot(time_stamp, strike2_oi, label=f'{contract2}', color='purple')
    ax.scatter([time_stamp[-1]], [strike1_oi[-1]], marker='o', color='orange')
    ax.scatter([time_stamp[-1]], [strike2_oi[-1]], marker='o', color='purple')

    ax.legend()

    return


def main(plotframe, index_chosen, expiry_chosen, strike1, strike2):

    '''
    global ax
    global contract1
    global contract2
    global expiry_date
    global index

    contract1 = strike_contract1
    contract2 = strike_contract2
    expiry_date = expiry
    index = index_chosen

    # figure size = 5 inches x 5 inches with dpi of 100
    # this makes size 900 x 500 pixels
    #figure = Figure(figsize=(9,5), dpi=100)
    figure = Figure(dpi=100)

    # connect figure to Tkinter Canvas
    figure_canvas = FigureCanvasTkAgg(figure, plotframe)
    figure_canvas.draw()

    ax = figure.add_subplot(1,1,1)

    #Place navigation tool bar on figure_canvas
    #Toggle placement with pack_toolbar argument
    toolbar = NavigationToolbar2Tk(figure_canvas, plotframe, pack_toolbar=False)
    toolbar.update()

    #place subplot on plotframe
    wid = figure_canvas.get_tk_widget()
    wid.pack(side='top', fill='both',expand=True)

    file_path= os.getcwd() +'\\'+ 'multistrike_oi.db'

    #os.system('cls')
    '''

    global ax

    #get the axes of the subplot on figure for manipulation
    ax = plt.subplot(1,1,1)


    #animation for live plotting
    ani = animate.FuncAnimation(
            plt.gcf(),
            lambda _ : draw_plot(
                index_chosen,
                expiry_chosen,
                strike1,
                strike2
                ),
            interval=300000
            )


    plt.show()
    #return figure, figure_canvas



if __name__ == '__main__':

    main(plotframe, expiry, strike_contract1, strike_contract2)
