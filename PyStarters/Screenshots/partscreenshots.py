import pyscreenshot
from PIL import Image

# To capture the part of the screen
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))

# To view the screenshot
image.show()

# To save the screenshot
image.save("PartScreenshotCaptured.png")
