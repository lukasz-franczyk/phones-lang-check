import qrcode
from PIL import Image
data = """
en - English
de - German
pl - Polish
fr - French
"""

image = qrcode.make(data)
image.save('qr.png')