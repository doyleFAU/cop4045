import turtle
from p1_Bradford_Doyle import testif
#part A
def draw_leaf_straight(level: int, petiole: float) -> None:
    """Recursive leaf. Level is recursion depth, petiole is teh lower stem length"""
    if level <= 0:
        return
    turtle.forward(petiole)
    if level > 1:
        size = petiole * 0.6
        turtle.left(40)
        draw_leaf_straight(level - 1, size)
        turtle.right(80)
        draw_leaf_straight(level - 1, size)
        turtle.left(40)
    turtle.backward(petiole)

def show_leaf() -> None:
    """draws leaf recursively"""
    turtle.delay(0)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -280)
    turtle.setheading(90)
    turtle.pendown()
    draw_leaf_straight(6, 120)
    turtle.done()

#part B
def _digit_char(d: int) -> str:
    """digit of char"""
    if d < 10:
        return str(d)
    return chr(ord("A") + d - 10)
def strB(n: int, base: int = 10) -> str:
    """Non-negative n as string in given base. Recursive"""
    if n == 0:
        return "0"
    def helper(num: int) -> str:
        if num < base:
            return _digit_char(num)
        return helper(num // base) + _digit_char(num % base)
    return helper(n)

def test_strB() -> None:
    """tests to see if they pass with differnt bases in bytes"""
    testif(strB(0) == "0", "strB 0", "strB 0 fail")
    testif(strB(1234, base=10) == "1234", "strB 10", "strB 10 fail")
    testif(strB(100, base=16) == "64", "strB hex", "strB hex fail")
    testif(strB(16, base=2) == "10000", "strB bin", "strB bin fail")

#partC
def Cnk_m(n: int, k: int, memo: dict[tuple[int, int], int] | None = None) -> int:
    """Binomial coefficient n choose k with memoization."""
    if memo is None:
        memo = {}
    key = (n, k)
    if key in memo:
        return memo[key]
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    val = Cnk_m(n - 1, k - 1, memo) + Cnk_m(n - 1, k, memo)
    memo[key] = val
    return val

def run_Cnk() -> None:
    """Print some binomial values for console screenshot"""
    print("C(5,2) =", Cnk_m(5, 2))
    print("C(10,4) =", Cnk_m(10, 4))
    print("C(20,10) =", Cnk_m(20, 10))

def test_Cnk_m() -> None:
    """tests binmoal and prints fail if wrong"""
    testif(Cnk_m(5, 2) == 10, "C 5 2", "C 5 2 fail")
    testif(Cnk_m(6, 0) == 1, "C n 0", "C n 0 fail")
    testif(Cnk_m(6, 6) == 1, "C n n", "C n n fail")
    testif(Cnk_m(10, 4) == 210, "C 10 4", "C 10 4 fail")

#part D
def make_pairs(seq1: list, seq2: list) -> list[tuple]:
    """Pairs (seq1[i], seq2[i]) until shorter list ends. Recursive"""
    def helper(i: int, acc: list[tuple]) -> list[tuple]:
        if i >= len(seq1) or i >= len(seq2):
            return acc
        acc.append((seq1[i], seq2[i]))
        return helper(i + 1, acc)
    return helper(0, [])

def test_make_pairs() -> None:
    """prints if pairs are equal or not"""
    testif(make_pairs([1, 2, 3], [4, 5, 6]) == [(1, 4), (2, 5), (3, 6)], "pairs equal", "pairs equal fail")
    testif(make_pairs([1, 2, 3], [4, 5]) == [(1, 4), (2, 5)], "pairs short2", "pairs short2 fail")
    testif(make_pairs([1, 2, 3], [4, 5, 6, 7, 8, 9]) == [(1, 4), (2, 5), (3, 6)], "pairs short1", "pairs short1 fail")
    testif(make_pairs([], [4, 5]) == [], "pairs empty1", "pairs empty1 fail")
    testif(make_pairs([1, 2, 3], []) == [], "pairs empty2", "pairs empty2 fail")


def main() -> None:
    print("Doyle Bradford #23673509")
    test_strB()
    test_Cnk_m()
    test_make_pairs()
    run_Cnk()
    
    show_leaf()
if __name__ == "__main__":
    main()

