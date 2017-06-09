# White-Space-Detector

## Introduction
Although a GUI has already been implemented by me on the same project, but this one is a script and has some new feature. This script can even tell you whether there is a whitespace or not in the image. It also has a run() function for separately checking all the images for whitespaces. If detected these images are auto-cropped (same as done by the GUI).

## How to run?
  1. Type "python pixel.py".
  2. To detect if an image has whitespace, type ">>> print iswhite(image)". Will return True if it has whitespace, else False.
  3. To detect whitespace and autocrop, type ">>> run(image, saving_location)". Will crop the image automatically if it hase whitespace and will save the cropped image at saving_location. Otherwise, nothing will happen.
  4. Also has a test.py script to test the script. Store all your original images in "image" folder (please after cloning rename Image folder as image on your local machine to avoid errors). Type, "python test.py". All the processed images will be stored in "out" folder.

## Examples

### Input1
![screenshot](https://github.com/hmnhGeek/White-Space-Detector/blob/master/Images/k.png)
### Output1
![screenshot](https://github.com/hmnhGeek/White-Space-Detector/blob/master/out/k.png)

### Input2
![screenshot](https://github.com/hmnhGeek/White-Space-Detector/blob/master/Images/my.png)
### Output2
![screenshot](https://github.com/hmnhGeek/White-Space-Detector/blob/master/out/my.png)
