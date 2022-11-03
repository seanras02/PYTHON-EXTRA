from tkinter import font
from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact.ttf", 40)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "Coding in python\nIs heel shite"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(139,0,0))

achtergrond.show()
achtergrond.save("meme_met_tekst.jpg")