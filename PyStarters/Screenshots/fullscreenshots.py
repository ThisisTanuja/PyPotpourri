import pyscreenshot
from PIL import Image

# To capture the screen
image = pyscreenshot.grab()

# To view the screenshot
image.show()

# To save the screenshot
image.save("FullScreenCaptured.png")

