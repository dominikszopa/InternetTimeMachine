from displayhatmini import DisplayHATMini

try:
    from PIL import Image
except ImportError:
    print("""This example requires PIL/Pillow, try:
sudo apt install python3-pil
""")

width = DisplayHATMini.WIDTH
height = DisplayHATMini.HEIGHT

buffer = Image.new("RGB", (width, height))
displayhatmini = DisplayHATMini(buffer, backlight_pwm=True)

displayhatmini.set_backlight(0)
