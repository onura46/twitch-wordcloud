from dougdoug.TwitchPlays_TTS_READER import *
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import re
import numpy as np
from scipy.ndimage import gaussian_gradient_magnitude
from config import *
from cleanup import Cleanup

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
if CLEANUP: # Flag in config that erases previous chatlog
    Cleanup.erase_save()

def make_plot_masked():
    # load image. This has been modified in gimp to be brighter and have more saturation.
    parrot_color = np.array(Image.open(os.path.join(d, INPUTFILE)))
    # subsample by factor of 3. Very lossy but for a wordcloud we don't really care.
    parrot_color = parrot_color[::3, ::3]

    # create mask  white is "masked out"
    parrot_mask = parrot_color.copy()
    parrot_mask[parrot_mask.sum(axis=2) == 0] = 255

    # some finesse: we enforce boundaries between colors so they get less washed out.
    # For that we do some edge detection in the image
    edges = np.mean(
        [
            gaussian_gradient_magnitude(parrot_color[:, :, i] / 255.0, 2)
            for i in range(3)
        ],
        axis=0,
    )
    parrot_mask[edges > 0.40] = 255

    # Process chatlog and regex out links, which break the wordcloud
    text = " ".join(i for i in open("save/chatlog.txt", "r") if re.search('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)',i) == None)
    wordcloud = WordCloud(font_path=FONT,background_color=BACKGROUND_COLOR,mask=parrot_mask,scale=SCALE,min_font_size=MIN_FONT_SIZE,max_font_size=MAX_FONT_SIZE,contour_width=2,contour_color="black",collocations=False,max_words=MAX_WORDS).generate(text)

    image_colors = ImageColorGenerator(parrot_color)
    wordcloud.recolor(color_func=image_colors)

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    wordcloud.to_file("wordcloud.png")

    plt.figure(figsize=(10, 10))
    plt.title("Original Image")
    plt.imshow(parrot_color)

    plt.figure(figsize=(10, 10))
    plt.title("Edge map")
    plt.imshow(edges)

    plt.show()
    
def make_plot():
    # Process chatlog and regex out links, which break the wordcloud
    text = " ".join(i for i in open("save/chatlog.txt", "r") if re.search('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)',i) == None)
    wordcloud = WordCloud(font_path=FONT,background_color=BACKGROUND_COLOR,scale=SCALE, min_font_size=MIN_FONT_SIZE,max_font_size=MAX_FONT_SIZE,contour_width=2,contour_color="black",collocations=False,max_words=MAX_WORDS).generate(text)

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation="bilinear")
    wordcloud.to_file("wordcloud.png")

    plt.show()
