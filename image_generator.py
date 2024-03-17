import io
from PIL import Image

class ImageGenerator:
    def __init__(self, api_key: str):
        self.api = OpenAIAPI(api_key=api_key)

    def generate_image(self, prompt: str) -> Image.Image:
        image_data = self.api.generate_image(prompt=prompt)
        image = Image.open(io.BytesIO(image_data))
        return image