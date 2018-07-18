from PIL import Image, ImageDraw, ImageFont

im = Image.open("Blank_canvas.png")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype( "times.ttf", 29 )
draw.text( (5, 0), text = 'H', font = font, fill=(0, 0, 0) )
del draw
im.save("Home.png")

im = Image.open("Blank_canvas.png")
draw = ImageDraw.Draw(im)
draw.polygon( (8, 6, 22, 15, 8, 24), fill = (0, 0, 0), outline = None )
del draw
im.save("Right.png")

im = Image.open("Blank_canvas.png")
draw = ImageDraw.Draw(im)
draw.polygon( (2, 6, 16, 15, 2, 24), fill = (0, 0, 0), outline = None )
draw.polygon( (15, 6, 29, 15, 15, 24), fill = (0, 0, 0), outline = None )
del draw
im.save("Right_ultra.png")

im = Image.open("Right.png")
im.rotate(90).save("Up.png")

im = Image.open("Right_ultra.png")
im.rotate(90).save("Up_ultra.png")

im = Image.open("Right.png")
im.rotate(180).save("Left.png")

im = Image.open("Right_ultra.png")
im.rotate(180).save("Left_ultra.png")

im = Image.open("Right.png")
im.rotate(270).save("Down.png")

im = Image.open("Right_ultra.png")
im.rotate(270).save("Down_ultra.png")
