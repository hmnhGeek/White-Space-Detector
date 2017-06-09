from PIL import Image
import numpy as np
import scipy.misc

def padding(image, padding_value):
    old_image = Image.open(image)
    old_size = old_image.size

    old_width = old_size[0]
    old_height = old_size[1]

    new_width = old_width + padding_value
    new_height = old_height + padding_value

    new_image = Image.new("RGB", (new_width, new_height), "white")
    new_image.paste(old_image,  (padding_value/2,padding_value/2))

    new_image.save(image)

def autoCrop(in_image, out_image, padding_value = 100):

    im = Image.open(in_image)
    pix = np.asarray(im)

    pix = pix[:,:,0:3] # Drop the alpha channel
    idx = np.where(pix-255)[0:2] # Drop the color when finding edges
    box = map(min,idx)[::-1] + map(max,idx)[::-1]

    region = im.crop(box)
    region_pix = np.asarray(region)

    scipy.misc.imsave(out_image, region_pix)

    padding(out_image, padding_value)

    
