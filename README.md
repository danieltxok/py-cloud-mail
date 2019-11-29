# PyCloudMail

PyCloudMail is a WordCloud generator in Python based on [this tutorial](https://www.datacamp.com/community/tutorials/wordcloud-python). Currently it only reads from a static TXT file but ideally it should read from the Gmail API to fetch customized text. This is WorkInProgress and my personal project to learn a bit of Python.

## Getting Started

Easily install all the dependencies by running `pip install -r requirements.txt` in your development environment. The script needs wordcloud, numpy, pillow and matplotlib to work.
To run the script, simply type `python main.py` and the file selection dialog will pop-up. Select the TXT file and wait for the output PNG file.

## Acknowledgments

* Huge thanks to [amueller](https://github.com/amueller) for the [word cloud generator](https://github.com/amueller/word_cloud)
* Also thanks to Duong Vu for [this tutorial](https://www.datacamp.com/community/tutorials/wordcloud-python)