#Script to create a movie out of the output images produced by Image Capture.py

# import imageio
# images = []

# filenames = 
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.imsave('movie.gif', images)

import os
import imageio.v2 as imageio

png_dir = r"C:\Users\vaigogia\OneDrive - Advanced Micro Devices Inc\Documents\GitHub\Python Automation\New folder\ChipScrubber\Images"
images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.jpg'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))

# Make it pause at the end so that the viewers can ponder
for _ in range(10):
    images.append(imageio.imread(file_path))

imageio.mimsave(r"C:\Users\vaigogia\OneDrive - Advanced Micro Devices Inc\Documents\GitHub\Python Automation\New folder\ChipScrubber\Images\Movie.gif", images)