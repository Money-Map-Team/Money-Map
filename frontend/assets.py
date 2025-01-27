from PIL import Image
import os

def load_image(image_name):
    """Load an image from the assets folder."""
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    image_path = os.path.join(assets_dir, image_name)

    if not os.path.exists(image_path):
        print(f"Error: Image '{image_name}' not found in '{assets_dir}'.")
        return None

    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image '{image_name}': {e}")
        return None
