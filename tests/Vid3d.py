import sys
sys.path.insert(0, '..')

import VidLib
import Image3d
import PIL

VidLib.create(size=300)
for x in range(360):
    Image3d.start_3d()
    d = 0.03*x;
    Image3d.make_voxels([d,d,d])
    Image3d.draw_line((d,d,d),(10,10,10))
    Image3d.ax.view_init(30, x)
    p = Image3d.to_pil()
    p = p.crop((100, 100, 400, 400))
  #  p = p.resize((300,300))
    VidLib.img.paste(p, (0,0,300,300))
    VidLib.text("3D Test", color=(70, 234, 189) )
    VidLib.next()
    print(x)
VidLib.done()
