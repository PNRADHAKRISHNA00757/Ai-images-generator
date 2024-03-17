import io
import unittest
from PIL import Image

from my_ai_package import ImageGenerator

class TestImageGenerator(unittest.TestCase):
    def test_generate_image(self):
        generator = ImageGenerator(api_key="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")
        image = generator.generate_image(prompt="a cat")
        self.assertIsInstance(image, Image.Image)
        self.assertGreater(image.width, 0)
        self.assertGreater(image.height, 0)

if __name__ == "__main__":
    unittest.main()