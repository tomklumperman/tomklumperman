from PIL import Image, ImageDraw

SRC = "images/projects-banner-github.jpeg"
DST = "images/banner-rounded.jpeg"
RADIUS_PERCENT = 3  # afronding als percentage van de breedte

img = Image.open(SRC).convert("RGBA")
radius = int(img.width * RADIUS_PERCENT / 100)

mask = Image.new("L", img.size, 0)
ImageDraw.Draw(mask).rounded_rectangle([(0, 0), img.size], radius=radius, fill=255)

img.putalpha(mask)
img.save(DST)
