from typing import Any
def testif(condition: bool, pass_msg: str, fail_msg: str) -> None:
    if condition:
        print("PASS:", pass_msg)
    else: 
        print("FAIL:", fail_msg)

#part A and B
class NVector:
    """Class for a vcetor that can have any number of dimensions."""
    def __init__(self, *args: Any) -> None:
        """Make a new vestor. If you pass one argument it should be a list or tuple of
  numbers. If you pass more than one, each argument is one element in the
  vector. We copy into a new list so changing the old list does not
  change the vector."""
        if len(args) == 1:
            self._elements: list[float] = list(args[0])
        else:
            self._elements = list(args)

#part C
    def __len__(self) -> int:
        """Returns length of the vector"""
        return len(self._elements)

    #part D
    def __getitem__(self, index: int) -> float:
        """Gets self[index]. negtive indexes work like a list."""
        return self._elements[index]

    #part E
    def __setitem__(self, index: int, value: float) -> None:
        """Sets self[index]  =. value. Bad index gives IndexError."""
        self._elements[index] = value

    #part F
    def __str__(self) -> str:
        """String for print."""
        return "NVector(" + str(self._elements) + ")"

    #part G
    def __eq__(self, other: object) -> bool:
        """Two NVectors are equal if every element matches."""
        if type(other) != NVector:
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self._elements)):
            if self._elements[i] != other._elements[i]:
                return False
        return True
    def __ne__(self, other: object) -> bool:
        """False when __eq__ would be True"""
        if self == other:
            return False
        return True

    #part H
    def __add__(self, other: object) -> "NVector":
        """Add two vectors or add a number to each elements"""
        if type(other) == NVector:
            result = []
            i = 0
            while i < len(self._elements):
                result .append(self._elements[i] + other._elements[i])
                i = i + 1
            return NVector(result)
        if type(other) == int or type(other) == float:
            result = []
            for i in range(len(self._elements)):
                result.append(self._elements[i] + other)
            return NVector(result)
        return NotImplemented
    
    def __radd__(self, other: object) -> "NVector":
        """So 10 + vector works"""
        return self.__add__(other)

    #part I
    def __mul__(self, other: object) -> float:
        """Vector times vector is dot product. Vector times number is sum of ai*number"""
        if type(other) == NVector:
            total = 00.0
            for i in range (len(self._elements)):
                total = total + self._elements[i] * other._elements[i]
            return total
        if type(other) == int or type(other) == float:
            total = 0.0
            for i in range(len(self._elements)):
                total = total + self._elements[i] * other
            return total
        return NotImplemented
    def __rmul__(self, other: object) -> float:
        """So 10 * vector works"""
        return self.__mul__(other)

    #part J
    @classmethod
    def zeros(cls, n: int) -> "NVector":
        """Makes a vector of n zeros"""
        vals = []
        for j in range(n):
            vals.append(0)
        return cls(vals)

#part K
def main() -> None:
    print("Doyle Bradford #23673509")
    v1 = NVector([3, 0, 1, -1])
    v2 = NVector(3, 0, 1, -1)
    testif(v1 == v2, "contructor works", "contructor failed")
    shared = [1, 2, 3]
    w = NVector(shared)
    shared[0] = 50
    testif(w[0] == 1, "list copy ok", "list copy failed")


    testif(len(v1) == 4, "len good", "len not good")

    testif(v1[1] == 0 and v1[-2] == 1, "getitem good", "getitem failed")

    v = NVector(1, 2, 3, 4)
    v[3] = 10
    testif(str(v1)[0:7] == "NVector", "str good", "str failed")

    testif(v1 == NVector(3, 0, 1, -1), "eq good", "eq failed")
    testif(v1 != NVector(0, 0, 0, 0), "ne good", "ne failed")

    a = NVector([3, 0, 1, -1])
    b = NVector([1, 2, 3, 4])
    testif(a + b == NVector([4, 2, 4, 3]), "add vec", "add vec failed")
    testif(a + 10 == NVector([13, 10, 11, 9]), "add num", "add num failed")
    testif(10 + a == NVector([13, 10, 11, 9]), "radd", "radd failed")

    testif(a * b == 2, "mul dot", "mul dot failed")
    testif(a * 10 == 30, "mul num", "mul num failed")
    testif(10 * a == 30, "rmul", "rmul failed")
if __name__ == "__main__":
    main()

