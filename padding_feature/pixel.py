from PIL import Image
import cropper

def get_dim(image):
    return image.size

def iswhite(addr, padding = 100, thr = 220):
    img = Image.open(addr) #Can be many different formats.
    im = img.copy()

    width, height = get_dim(im)   # Get dimensions

    new_width = width - padding
    new_height = height - padding

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    
    im = im.crop((left, top, right, bottom))
    
    pix = im.load()
    area = im.size[0] * im.size[1]

    white_from_left_to_right = []
    ltr = True
    white_from_right_to_left = []
    rtl = True
    white_from_top_to_bottom = []
    ttb = True
    white_from_bottom_to_top = []
    btt = True


    x_percent = int(round(im.size[0]*0.7142857142857143*100**(-1)))
    y_percent = int(round(im.size[1]*0.7142857142857143*100**(-1)))

    # from left to right
    
    for x in range(0,x_percent):
        for y in range(0,im.size[1]):
            rgb = pix[x, y]
            if rgb[0] < thr and rgb[1] < thr and rgb[2] < thr:
                white_from_left_to_right.append(rgb)
            if y == im.size[1] - 1:
            
                if white_from_left_to_right == []:
                    
                    ltr = True
                else:
                    ltr = False

    # from right to left
    
    for x in range(im.size[0]-1, im.size[0]-1-x_percent, -1):
        for y in range(0,im.size[1]):
            rgb = pix[x, y]
            if rgb[0] < thr and rgb[1] < thr and rgb[2] < thr:
                white_from_right_to_left.append(rgb)
            if y == im.size[1] - 1:
            
                if white_from_right_to_left == []:
                    
                    rtl = True
                else:
                    rtl = False

    # from top to bottom
    
    for y in range(0, y_percent):
        for x in range(0,im.size[0]):
            rgb = pix[x, y]
            if rgb[0] < thr and rgb[1] < thr and rgb[2] < thr:
                white_from_top_to_bottom.append(rgb)
            if x == im.size[0] - 1:
            
                if white_from_top_to_bottom == []:
                    
                    ttb = True
                else:
                    ttb = False

    # from bottom to top
    
    for y in range(im.size[1]-1, im.size[1]-1-y_percent, -1):
        for x in range(0,im.size[0]):
            rgb = pix[x, y]
            if rgb[0] < thr and rgb[1] < thr and rgb[2] < thr:
                white_from_bottom_to_top.append(rgb)
            if x == im.size[0] - 1:
            
                if white_from_bottom_to_top == []:
                    
                    btt = True
                else:
                    btt = False

    if [ltr, rtl, ttb, btt] == 4*[False,]:
        return False
    else:
        return True



def run(addr, out):
    if iswhite(addr):
        cropper.autoCrop(addr, out)
    else:
        print "Not required!!"


