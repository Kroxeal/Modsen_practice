import unit_test
import os
import shutil
from dublicate_imagess import ImageDuplicateFinder


class TestImageDuplicateFinder(unittest.TestCase):
    def setUp(self):
        self.temp_folders = [
            "temp_folder1",
            "temp_folder2"
        ]

        for folder in self.temp_folders:
            os.makedirs(folder, exist_ok=True)

        test_images = [
            "002c100a56.jpg",
            "d7719c1ca7.jpg",
            "00d715b92f.jpg"
        ]

        for image in test_images:
            shutil.copy(os.path.join("../test_data", image), self.temp_folders[0])
            shutil.copy(os.path.join("../test_data", image), self.temp_folders[1])

        self.finder = ImageDuplicateFinder()

    def tearDown(self):
        for folder in self.temp_folders:
            shutil.rmtree(folder, ignore_errors=True)

    def test_process_folders(self):
        folders = [os.path.abspath(folder) for folder in self.temp_folders]
        self.finder.process_folders(folders)

        self.assertTrue(self.finder.duplicates)

        expected_duplicates = [
            "002c100a56.jpg",
            "d7719c1ca7.jpg",
            "00d715b92f.jpg"
        ]

        # Check if each expected duplicate image name is found in the results
        for img_paths in self.finder.duplicates.values():
            for img_path in img_paths:
                self.assertIn(os.path.basename(img_path), expected_duplicates)

    def test_show_images(self):
        folders = [os.path.abspath(folder) for folder in self.temp_folders]
        self.finder.process_folders(folders)

        try:
            self.finder.show_images(3)
        except Exception as e:
            self.fail(f"show_images raised exception: {str(e)}")


if __name__ == "__main__":
    unittest.main()

