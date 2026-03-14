from PIL import Image, ImageDraw, ImageFont

# Create blank image
width, height = 600, 400
image = Image.new("RGB", (width, height), color=(255, 228, 225))

draw = ImageDraw.Draw(image)

# Load font
try:
    font_big = ImageFont.truetype("arial.ttf", 80)
    font_small = ImageFont.truetype("arial.ttf", 30)
except:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Main text
text = "SORRY 😔"

# NEW METHOD (instead of textsize)
bbox = draw.textbbox((0, 0), text, font=font_big)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

draw.text(
    ((width - text_width) / 2, (height - text_height) / 2 - 30),
    text,
    fill="red",
    font=font_big
)

# Sub text
sub_text = "Please forgive me ❤️"

bbox2 = draw.textbbox((0, 0), sub_text, font=font_small)
sub_width = bbox2[2] - bbox2[0]
sub_height = bbox2[3] - bbox2[1]

draw.text(
    ((width - sub_width) / 2, (height - sub_height) / 2 + 50),
    sub_text,
    fill="black",
    font=font_small
)

image.save("sorry_image.png")

print("Sorry image created successfully!")