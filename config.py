CHANNEL_TO_LISTEN_TO = 'channel_name'

# Wordcloud settings
SCALE = 12 # Scales size of the entire chart; increase if output image is too small, decrease if too large
MIN_FONT_SIZE = 3 # Smallest possible words on chart
MAX_FONT_SIZE = 50 # Largest possible words on chart - size of the most used words
MAX_WORDS = 500 # Limit to this number of words
MARGIN = 2
FONT = "Reduction.ttf"
BACKGROUND_COLOR = "white" # Accepts colors by word from https://drafts.csswg.org/css-color-4/#named-colors
COLORMAP = "plasma" # Accepts colormap names from https://matplotlib.org/stable/users/explain/colors/colormaps.html

# Erases previous chat log before initialization
CLEANUP = True

# Set whether or not to mask the wordcloud, and set the destination of the file to use as a mask.
MASKED = True
INPUTFILE = "tree.jpg"