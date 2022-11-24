import tkinter as tk

import random
import numpy as np
import itertools as it
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = tk.Tk()
root.geometry("250x100")

n_centroids_var = tk.StringVar()
w_h_var = tk.StringVar()

def voronoi():

    n_centroids = int(n_centroids_var.get())
    h = int(w_h_var.get())
    w = int(w_h_var.get())
    x = int(w_h_var.get())
    y = int(w_h_var.get())
    img = np.zeros((x,y,3))

    centroids = [(random.randint(0, h), random.randint(0, w)) for _ in range(n_centroids)]
    colors = np.array([np.random.choice(range(256), size=3) for _ in range(n_centroids)]) / 255

    for x, y in it.product(range(h), range(w)):
        distances = np.sqrt([(x - c[0])**2 + (y - c[1])**2 for c in centroids])
        centroid_i = np.argmin(distances)
        img[x,y] = colors[centroid_i]

    fig = plt.figure(figsize = (0.75, 0.75))

    plt.imshow(img, cmap='gray')

    plt.xticks([])
    plt.yticks([])

    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()
  
    canvas.get_tk_widget().grid(row=0,column=3, rowspan = 3, pady=2)
     
    n_centroids_var.set("")
    w_h_var.set("")

    close_fig_state = False

    if close_fig_state == False:
        plt.close('all')

def r_voronoi():

    n_centroids = random.randint(1, 30)
    h = random.randint(1, 30)
    w = h
    x = h
    y = x
    img = np.zeros((x,y,3))

    centroids = [(random.randint(0, h), random.randint(0, w)) for _ in range(n_centroids)]
    colors = np.array([np.random.choice(range(256), size=3) for _ in range(n_centroids)]) / 255

    for x, y in it.product(range(h), range(w)):
        distances = np.sqrt([(x - c[0])**2 + (y - c[1])**2 for c in centroids])
        centroid_i = np.argmin(distances)
        img[x,y] = colors[centroid_i]

    fig = plt.figure(figsize = (0.75, 0.75))

    plt.imshow(img, cmap='gray')

    plt.xticks([])
    plt.yticks([])

    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()

    canvas.get_tk_widget().grid(row = 0, column = 3, rowspan = 3, pady = 2)
     
    n_centroids_var.set("")
    w_h_var.set("")

    close_fig_state = False

    if close_fig_state == False:
        plt.close('all')

centroid_label = tk.Label(root, text = 'n centroids', font=('calibre', 10, 'bold'))
centroid_entry = tk.Entry(root, textvariable = n_centroids_var, font=('calibre', 10, 'normal'), width = 10)

wh_label = tk.Label(root, text = 'w and h', font = ('calibre', 10, 'bold'))
wh_entry = tk.Entry(root, textvariable = w_h_var, font = ('calibre', 10, 'normal'), width = 10)

sub_btn = tk.Button(root,text = 'Submit', command = voronoi)

ran_btn = tk.Button(root,text = 'Random', command = r_voronoi)

centroid_label.grid(row = 0, column = 0, pady = 2)
centroid_entry.grid(row = 0, column = 1, pady = 2)
wh_label.grid(row = 1, column = 0, pady = 2)
wh_entry.grid(row = 1, column = 1, pady = 2)
sub_btn.grid(row = 2, column = 1, pady = 2)
ran_btn.grid(row = 2, column = 0, pady = 2)
  
root.mainloop()