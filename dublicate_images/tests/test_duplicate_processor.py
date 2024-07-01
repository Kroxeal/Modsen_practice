import unittest
from unittest.mock import MagicMock
from src.process_dublicate.process_dublicate import DuplicateProcessor


class TestDuplicateProcessor(unittest.TestCase):

    def test_process_folders(self):
        processor = DuplicateProcessor()

        processor.duplicate_finder.add_image_hashes = MagicMock()
        processor.duplicate_finder.find_duplicates = MagicMock()
        processor.duplicate_finder.print_duplicates = MagicMock()

        folders = ["folder1", "folder2"]
        processor.process_folders(folders)

        processor.duplicate_finder.add_image_hashes.assert_called()
        processor.duplicate_finder.find_duplicates.assert_called()
        processor.duplicate_finder.print_duplicates.assert_called()


if __name__ == '__main__':
    unittest.main()
