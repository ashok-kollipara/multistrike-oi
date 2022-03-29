import tkinter as tk
from tkinter import ttk
#import matplotlib.animation as animate
import tkplot
import json_handler

def list_expiries(index, expiry_box, mainframe):
    
    json_handler.get_OC_json(index)

    lbl=ttk.Label(
            mainframe,
            text='Downloading Data from NSE....',
            anchor='center',
            foreground='green',
            )
    lbl.grid(
            column=2,
            row =1,
            sticky='WE',
            padx=5,
            pady=5,
            columnspan=2
            )

    mainframe.after(5000, lambda: lbl.configure(text='Data Downloaded, Choose Expiry Date'))

    expiry_list = json_handler.get_expiries()
    expiry_box['values'] = expiry_list

    mainframe.after(5000, lambda: lbl.destroy())

    return

def populate_strikes(expiry_chosen, strike1_box, strike2_box):
    
    strikes_list = json_handler.get_strikes(expiry_chosen.get())
    strike1_box['values'] = strikes_list
    strike2_box['values'] = strikes_list

    return

def plot(root_window, index_chosen, expiry_chosen, strike1, strike2):

    plotframe = ttk.Frame(root_window)
    plotframe['padding'] = (3,3,3,3)
    plotframe.grid(column=0, row=1, sticky=('N', 'W', 'E', 'S') )

    tkplot.main(
            plotframe, 
            index_chosen.get(),
            expiry_chosen.get(),
            strike1.get(),
            strike2.get()
            )

    '''
    figure, figure_canvas = tkplot.main(
            plotframe, 
            index_chosen.get(),
            expiry_chosen.get(),
            strike1.get(),
            strike2.get()
            )


    #place subplot on plotframe
    wid = figure_canvas.get_tk_widget()
    wid.pack(side='top', fill='both',expand=True)

    #animation for live plotting
    ani = animate.FuncAnimation(
            figure,
            lambda : tkplot.draw_plot(
                index_chosen.get(),
                expiry_chosen.get(),
                strike1.get(),
                strike2.get()
                ),
            interval=300000
            )

    figure.show()

    return ani
    '''

def ui_workspace():

    root_window = tk.Tk() 


    # Standardized spawn location and configurable items for window geometry

    screen_width=root_window.winfo_screenwidth()
    screen_height=root_window.winfo_screenheight()
    win_width=900
    win_height=200
    x_spawn=int((screen_width-win_width)/2)
    y_spawn=int((screen_height-win_height)/2)

    # Do the placement
    placement_location=f'{win_width}x{win_height}+{x_spawn}-{y_spawn}'
    #root_window.geometry(placement_location)



    # Update title
    root_window.title("Multi-strike Open Interest Analysis")

    # Create the main element frame
    mainframe= ttk.Frame(root_window)
    mainframe['padding'] = (3,3,3,3)
    #mainframe['width'] = win_width

    mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S') )
    root_window.rowconfigure(0, weight=1)
    root_window.rowconfigure(1, weight=1)
    root_window.columnconfigure(0, weight=1)
    root_window.columnconfigure(1, weight=1)
    root_window.columnconfigure(2, weight=1)
    root_window.columnconfigure(3, weight=1)
    root_window.columnconfigure(4, weight=1)
    root_window.columnconfigure(5, weight=1)
    
    # Add widgets

    # Add label for radio boxes
    ttk.Label(mainframe, text='Choose an Expiry Date').grid(column=2, row=0, sticky=('W','E'))

    # Make a combobox
    expiry_chosen = tk.StringVar()
    expiry_box = ttk.Combobox(mainframe, textvariable=expiry_chosen, state='readonly')
    expiry_box.grid(column=3, row=0, sticky=('W','E'))
    #expiry_box.bind('<<ComboboxSelected>>', lambda: populate_strikes(strike1_box, strike2_box))

    # Add label for radio boxes
    ttk.Label(mainframe, text='Choose an Index').grid(column=0, row=0, sticky=('W','E'))

    index_chosen = tk.StringVar()

    #Add Radio Boxes for Index Selection
    nifty = ttk.Radiobutton(
            mainframe, 
            text='NIFTY', 
            variable=index_chosen, 
            value='NIFTY',
            command= lambda : list_expiries(index_chosen.get(), expiry_box, mainframe)
            )

    banknifty = ttk.Radiobutton(
            mainframe, 
            text='BANKNIFTY', 
            variable=index_chosen, 
            value='BANKNIFTY',
            command= lambda : list_expiries(index_chosen.get(), expiry_box, mainframe)
            )

    nifty.grid(column=1, row=0, sticky=('W','E'))
    banknifty.grid(column=1, row =1, sticky=('W','E'))

    # Add label for strike selection combo boxes
    ttk.Label(mainframe, text='Strikes to Compare').grid(column=4, row=0, sticky=('W','E'))

    # Make a combobox for strike 1
    strike1 = tk.StringVar()
    strike1_box = ttk.Combobox(mainframe, textvariable=strike1, state='readonly')
    strike1_box.grid(column=5, row=0, sticky=('W','E'))

    # Make a combobox for strike 2
    strike2 = tk.StringVar()
    strike2_box = ttk.Combobox(mainframe, textvariable=strike2, state='readonly')
    strike2_box.grid(column=5, row=1, sticky=('W','E'))

    # Bind selection of expiry date to populate the strike combo boxes
    expiry_box.bind(
            '<<ComboboxSelected>>',
            lambda _ : populate_strikes(expiry_chosen, strike1_box, strike2_box)
            )


    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
        child.grid_configure(ipadx=3, ipady=3)


    button = ttk.Button(
            mainframe,
            text = 'Plot', 
            command = lambda : plot(
                root_window,
                index_chosen,
                expiry_chosen,
                strike1,
                strike2
                )
            )

    button.grid(column=6, row=0, sticky='WE')


    root_window.mainloop()


if __name__=='__main__':

    ui_workspace()
