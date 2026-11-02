from __future__ import annotations

class Entry:
    """The base class for a storage entry"""
    def __init__(self, name: str, parent: Entry | None = None) -> None:
        self.name = name
        self._parent = parent    

    def parent(self) -> Entry | None:
        return self._parent

    def size(self) -> int:
        """Return the size of the entry in bytes"""
        raise NotImplementedError("Subclasses has to implement size()")

    def absolute_path(self) -> list[Entry]:
        """Return entries in order from this entry up to the root."""
        if self._parent is None:
            return [self]
        return [self] + self._parent.absolute_path()

class File(Entry):
    """A file with a size in bytes"""
    def __init__(self, name: str, bytes_used: int, parent: Entry | None = None) -> None:
        """creates file with size thats not negative"""
        if bytes_used < 0:
            raise ValueError("File size cannot be negative")
        super().__init__(name, parent)
        self.bytes_used = bytes_used
    def size(self) -> int:
        return self.bytes_used

class Folder(Entry):
    """A folder that has other entries"""
    def __init__(self, name: str, parent: Entry | None = None) -> None:
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        """Adds an entry to the folder"""
        self._children.append(entry)
        entry._parent = self

    def size(self) -> int:
        """returns the size of folder"""
        return sum(entry.size() for entry in self._children)
    def children(self) -> tuple[Entry, ...]:
        """returns a tuple of the entries in the folder"""
        return tuple(self._children)

def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """check file recursively and return large files"""
    if isinstance(entry, File):
        if entry.size() >= minimum_size:
            return [entry]
        return []
    if isinstance(entry, Folder):
        result: list[File] = []
        for child in entry.children():
            result.extend(find_large_files(child, minimum_size))
        return result
    raise TypeError("Entry must be a File or Folder")

def demo_storage_tree() -> None:
    """Build and show a nested storage tree"""
    
    print("Doyle Bradford #23673509")

    outer = Folder("output")
    projects = Folder("projects")
    reports = Folder("reports")
    archive = Folder("archive")

    outer.add(File("readme.txt", 8))
    outer.add(projects)
    projects.add(File("notes.txt", 24))
    projects.add(reports)
    reports.add(File("summary.txt", 60))
    reports.add(archive)
    archive.add(File("backup.txt", 120))

    total_size = outer.size()
    print("Total size:", total_size, "bytes")


    smaller_cutoff = find_large_files(outer, 20)
    larger_cutoff = find_large_files(outer, 100)

    print("Files at least 20 bytes:", [file.name for file in smaller_cutoff])
    print("Files at least 100 bytes:", [file.name for file in larger_cutoff])


    print("Abslute paths(entry up to roots):")
    for entry in (archive.children()[0], reports):
        path_names = [item.name for item in entry.absolute_path()]
        print(f"{entry.name}: " + " <- ".join(path_names))


if __name__ == "__main__":
    demo_storage_tree()
