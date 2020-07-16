import sys
sys.path.insert(0, '..')

import VidLib
import Image3d
import PIL

VidLib.create(size=400)
for x in range(360):
    Image3d.start_3d()
    d = 0.03*x;
    Image3d.make_voxels([d,d,d])
    Image3d.draw_line((d,d,d),(10,10,10))
    Image3d.ax.view_init(30, x)
    p = Image3d.to_pil()
    p = p.resize((400,400))
    px = p.load()
    for i in range(400):
        for j in range(400):
            VidLib.pixels[i,j] = px[i,j]
    VidLib.text("3D Test")
    VidLib.next()
    print(x)
VidLib.done()
