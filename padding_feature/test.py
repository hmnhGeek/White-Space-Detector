import os
import pixel

app = os.path.dirname(os.path.abspath(__file__))

os.chdir(app+'/images/')

files = [f for f in os.listdir(".")]

for f in files:
    print
    print "White space in", f, pixel.iswhite(f)
    if pixel.iswhite(f):
        pixel.run(f, app+'/out/'+f)
        print "File cropped"
    print

os.chdir(app)
    
