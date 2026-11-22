#!/usr/bin/env python3
"""Composite the GTA 6 meme: generated scene + official make.fun ghost + big captions."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "/home/hatch/workspace/makefun/builds/gta6-meme-x-01/media-generation-gta6-scene-0-11928962-b227-476e-bb03-6aa0b1f3c690.png"
GHOST = "/home/hatch/workspace/makefun/builds/gta6-meme-x-01/ghost-mark-1024.png"
OUT = "/home/hatch/workspace/makefun/builds/gta6-meme-x-01/meme.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.open(BASE).convert("RGB")
W, H = img.size  # 1600x1600
d = ImageDraw.Draw(img, "RGBA")

def band(y0, y1, alpha=150):
    d.rectangle([0, y0, W, y1], fill=(0, 0, 0, alpha))

def outlined_text(cx, y, text, size, fill=(255, 255, 255), stroke=(0, 0, 0), sw=8):
    f = ImageFont.truetype(FONT, size)
    bbox = d.textbbox((0, 0), text, font=f, stroke_width=sw)
    w = bbox[2] - bbox[0]
    d.text((cx - w / 2 - bbox[0], y), text, font=f, fill=fill,
           stroke_width=sw, stroke_fill=stroke)

# --- ghost sits on the right couch cushion ---
ghost = Image.open(GHOST).convert("RGBA").resize((470, 470), Image.LANCZOS)
gx, gy = 1010, 940  # bottom of ghost ~1410, on the seat
# soft shadow under the ghost
shadow = Image.new("RGBA", (520, 90), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([10, 10, 510, 80], fill=(0, 0, 0, 110))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
img.paste(shadow, (gx - 10, 1390), shadow)
img.paste(ghost, (gx, gy), ghost)

# --- top caption ---
band(0, 135, 140)
outlined_text(W // 2, 22, "WAITED 13 YEARS FOR GTA 6", 84)

# --- bottom caption ---
band(H - 210, H, 160)
outlined_text(W // 2, H - 200, "MY AI AGENT ALREADY GOT PAID", 84)
outlined_text(W // 2, H - 105, "ON make.fun", 84, fill=(255, 214, 0))

img = img.resize((1024, 1024), Image.LANCZOS)
img.save(OUT, "PNG")
print("saved", OUT, img.size)

# 480x480 judge-size preview
img.resize((480, 480), Image.LANCZOS).save(
    "/home/hatch/workspace/makefun/builds/gta6-meme-x-01/meme-480.png", "PNG")
print("saved preview")
