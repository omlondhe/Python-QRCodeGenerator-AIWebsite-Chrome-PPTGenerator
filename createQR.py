import pyqrcode
import png
import sys
from pyqrcode import QRCode

link = sys.argv[1]
url = pyqrcode.create(link)
url.png(sys.argv[2] + ".png", scale=6)
