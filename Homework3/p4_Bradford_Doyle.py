def testif(condition: bool, pass_msg: str, fail_msg: str) -> None:
    """tests if it passes or fails"""
    if condition:
        print("PASS:", pass_msg)
    else:
        print("FAIL:", fail_msg)

#part A
def _read_file(filename: str) -> str:
    """reads file to text"""
    f = open(filename, "r")
    text = f.read()
    f.close()
    return text

def _write_file(filename: str, text: str) -> None:
    """writes to file"""
    f = open(filename, "w")
    f.write(text)
    f.close()


def ed_read(filename: str, from_pos: int = 0, to: int = -1) -> str:
    """Return file text in (from_pos, to =-1) means end. Raises IndexError if to is past end"""
    text = _read_file(filename)
    if to == -1:
        return text[from_pos:]
    if to >len(text):
        raise IndexError("to index past end of file")
    return text[from_pos:to]

def ed_find(filename: str, search_str: str) -> list[int]:
    """Return list of indices where search_str occurs in file"""
    text = _read_file(filename)
    result: list[int] = []
    pos = 0
    while True:
        i = text.find(search_str, pos)
        if i == -1:
            break
        result.append(i)
        pos = i + 1
    return result

def ed_replace(filename: str, search_str: str, replace_with: str, occurrence: int = -1) -> int:
    """Replace search_str with replace_with. occurrence=-1 means all. Returns count replaced."""
    text = _read_file(filename)
    spots = ed_find(filename, search_str)
    if len(spots) == 0:
        return 0
    if occurrence == -1:
        count = text.count(search_str)
        new_text = text.replace(search_str, replace_with)
        _write_file(filename, new_text)
        return count
    if occurrence >= len(spots):
        return 0
    i = spots[occurrence]
    new_text = text[:i] + replace_with + text[i + len(search_str):]
    _write_file(filename, new_text)
    return 1
def ed_append(filename: str, string: str) -> int:
    """Append string to file. Creates file if needed. Returns len(string) written."""
    f = open(filename, "a")
    f.write(string)
    f.close()
    return len(string)

#part B
def test_ed_find() -> None:
    """tests file with exmaples"""
    fn = "test_ed.txt"
    f = open(fn, "w")
    f.write("01234567890123456789")
    f.close()
    testif(ed_find(fn, "345") == [3, 13], "find 345 ok", "find 345 failed")
    testif(ed_find(fn, "356") == [], "find missing ok", "find missing failed")

def test_ed_replace() -> None:
    """tests when you replace whats in"""
    fn = "test_ed.txt"
    f = open(fn, "w")
    f.write("01234567890123456789")
    f.close()
    n = ed_replace(fn, "345", "ABCDE", 1)
    testif(n == 1, "replace one ok", "replace one failed")
    testif(ed_read(fn, 0, 20) == "0123456789012ABCDE67", "replace one text ok", "replace one text failed")

    f = open(fn, "w")
    f.write("01234567890123456789")
    f.close()
    n2 = ed_replace(fn, "345", "ABCDE", -1)
    testif(n2 == 2, "replace all count ok", "replace all failed")

def main() -> None:
    print("Doyle Bradford #23673509")
    fn = "file1.txt"
    ed_append(fn, "0123456789")
    ed_append(fn, "0123456789")

    print(ed_read(fn, 3, 9))
    print(ed_read(fn, 3))
    print(ed_find(fn, "345"))
    print(ed_find(fn, "356"))
    ed_replace(fn, "345", "ABCDE", 1)
    print(ed_read(fn))

    f = open(fn, "w")
    f.write("01234567890123456789")
    f.close()
    ed_replace(fn, "345", "ABCDE")
    print(ed_read(fn))

    test_ed_find()
    test_ed_replace()
if __name__ == "__main__":
    main()
