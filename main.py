"""
PyCloudMail
===============

PyCloudMail is a WordCloud generator in Python.
"""

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Get data directory
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select the source txt file", filetypes= (("TXT files","*.txt"),("All files","*.*")))
filename = os.path.basename(file_path)
pre, ext = os.path.splitext(file_path)

# Read the whole text
text = open(file_path).read()

# Generate a word cloud image and saving it into a file
wordcloud = WordCloud(width=2000, height=1126, background_color=None, mode="RGBA").generate(text)
wordcloud.to_file(pre + ".png")

# Display the generated image (interpolation='bilinear' to make the displayed image appear more smoothly)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()