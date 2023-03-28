from datetime import datetime
from dateutil.relativedelta import relativedelta
from displayhatmini import DisplayHATMini
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("""This example requires PIL/Pillow, try:

sudo apt install python3-pil

""")


class DisplayDateMiniHat:
    def __init__(self):
        self.width = DisplayHATMini.WIDTH
        self.height = DisplayHATMini.HEIGHT
        self.buffer = Image.new("RGB", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.buffer)
        self.font = ImageFont.truetype("LCD14.otf", 80)
        self.displayhatmini = DisplayHATMini(self.buffer, backlight_pwm=True)
        self.internet_date = datetime(2005, 1, 1)  # Set starting date
        self.brightness = 1.0
        self.displayhatmini.on_button_pressed(self.button_callback)
        self.display_year()

    def display(self):
        self.displayhatmini.display()

    def display_year(self):
        self.draw.rectangle((0, 0, self.width, self.height), (0, 0, 0))
        self.draw.text(
            (50, 70),
            self.internet_date.strftime("%Y"),
            font=self.font,
            fill=(255, 0, 0)
        )

    def button_callback(self, pin):
        # Only handle presses
        if not self.displayhatmini.read_button(pin):
            return

        if pin == self.displayhatmini.BUTTON_A:
            self.internet_date = self.internet_date - relativedelta(years=1)

        if pin == self.displayhatmini.BUTTON_X:
            self.internet_date = self.internet_date + relativedelta(years=1)

        self.display_year()
