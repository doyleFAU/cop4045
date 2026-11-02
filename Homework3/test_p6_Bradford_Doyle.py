import unittest

from p6_Bradford_Doyle import File, Folder, Entry, find_large_files


class AbsolutePathTests(unittest.TestCase):
    """Unit tests for Entry.absolute_path()."""

    def test_root_by_itself(self) -> None:
        """Root with no parent should return a list with only itself."""
        root = Folder("root")
        self.assertEqual(root.absolute_path(), [root])

    def test_short_parent_chain(self) -> None:
        """File added to root should path from file to root."""
        root = Folder("root")
        child = File("child.txt", 5)
        root.add(child)

        self.assertEqual(child.absolute_path(), [child, root])

    def test_deep_path_order(self) -> None:
        """Deep file path goes self first then parents up to root."""
        root = Folder("root")
        first = Folder("first")
        second = Folder("second")
        file = File("file.txt", 5)
        root.add(first)
        first.add(second)
        second.add(file)

        self.assertEqual(file.absolute_path(), [file, second, first, root])


class FindLargeFilesTests(unittest.TestCase):
    """Unit tests for find_large_files()."""

    def test_file_at_cutoff(self) -> None:
        """File with size equal to minimum should be included."""
        file = File("large.txt", 10)
        self.assertEqual(find_large_files(file, 10), [file])

    def test_file_below_cutoff_is_not_returned(self) -> None:
        """File smaller than minimum should return empty list."""
        file = File("small.txt", 5)
        self.assertEqual(find_large_files(file, 10), [])

    def test_searches_folder_and_nested_folder(self) -> None:
        """Search folder and nested folder and collect large files."""
        root = Folder("root")
        nested = Folder("nested")

        large_file = File("large.txt", 20)
        small_file = File("small.txt", 5)
        nested_large_file = File("nested-large.txt", 15)

        root.add(large_file)
        root.add(small_file)
        root.add(nested)
        nested.add(nested_large_file)

        self.assertEqual(
            find_large_files(root, 10),
            [large_file, nested_large_file],
        )


if __name__ == "__main__":
    unittest.main()
