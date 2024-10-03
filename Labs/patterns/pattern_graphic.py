#README===========================================================
#1. Open Google Colab site
#2. Create new note
#3. Paste code from this file to note
#4. Upload "data.txt" file to site store(in temporary)
#5. Run script and have plot or errors
#6. You need to click on plot and copy it, because save image will be empty(idk why)
#7. If you need many plots on one picture, copy block of processing and paste it many times
# changing names of file and symbols in plt.plot for beauty
#=================================================================

import matplotlib.pyplot as plt     #include libs  <DONT CHANGE>
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
from IPython.display import display, Math, Latex
import numpy as np
from math import *

file_name = "data.txt"

plt.rcParams["font.family"] = "monospace"

def mapping(x, k, b):                #Function of approximating give to curve_fit <TO CHANGE!!!>
    return b + k*x

save_pic = "./graphic.png"

#========================================================================================
_, ax = plt.subplots(figsize=(10, 10))
ax.set_xlabel("Подпись оси $X$", fontweight="bold") #You can write Latex formulas
ax.set_ylabel("Подпись оси $Y$", fontweight="bold")
ax.set_title("График $x(y)$", fontweight="bold")

ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
ax.xaxis.set_minor_locator(ticker.MaxNLocator(10))
ax.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax.yaxis.set_minor_locator(ticker.MaxNLocator(10))

plt.grid(color="blue", visible=True, which='major',axis='both',alpha=1, linestyle = ":")
plt.grid(color="blue", visible=True, which='minor',axis='both',alpha=1, linestyle = ":")
#========================================================================================
#========================================================================================

#Processing
#========================================================================================
x = []
y = []

file = open(file_name, 'r')                 #open file with data
while (line := file.readline()):              # every line have x, y, y1 ...
  s = line.split()
  if (len(s) != 0):
    x.append(float(s[0].replace(',','.')))    #collect in x[] y1[] y2[] with change "," -> "." (if excel)
    y.append(float(s[1].replace(',','.')))

k = 0                                        #create coeffs all in function
b = 0

coeffs,_ = curve_fit(mapping, x, y)          #give func and our measurements
k = coeffs[0]                                   #it returns array of aproximating coeffs <CHANGE DEPEND OF FUNC>
b = coeffs[1]
y_fit = []
for i in range(len(x)):
  y_fit.append(b + k * x[i])                    #with coeffs make array of Approximating data
#                 ^
#                 |
#                 function need to write <TO CHANGE>
#                 """"""""""""""""""""""

#Change symbols colors and e.t.c check docs for plot
plt.plot(x, y, 'r^', label='')    #triangles with measurements
plt.plot(x, y_fit, color = 'y', label = f"Прямая с аппроксимацией: " r'$y = b + k \cdot x$' f", k = {k:.3f}, b = {b:.3f}")
#==========================================================================================
#End Processing

#==========================================================================================
#==========================================================================================
plt.legend()
plt.savefig(save_pic)
plt.show()