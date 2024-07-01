import unittest
from unittest.mock import MagicMock
from src.show_image.show_image import ImageDisplay


class TestImageDisplay(unittest.TestCase):

    def test_show_images(self):
        duplicates = {
            1234567890: ["image1.jpg", "image2.jpg"]
        }

        ImageDisplay.show_images = MagicMock()

        display = ImageDisplay()
        display.show_images(duplicates, 2)

        ImageDisplay.show_images.assert_called_once_with(duplicates, 2)


if __name__ == '__main__':
    unittest.main()
