#part A
class ParkingPermit:
    """Base parking permit with owner, months, and fee schedule dict."""
    def __init__(self, owner: str, months: int, fee_schedule: dict[str, float]) -> None:
        """Store owner name, months purchased, and rates in fee_schedule."""
        self._owner = owner
        self._months = months
        self._fee_schedule = fee_schedule
    def cost(self) -> float:
        """Subclasses override to compute permit cost."""
        return 0.0

#part B
class StudentPermit(ParkingPermit):
    """Student permit; also tracks number of vehicles."""
    def __init__(self, owner: str, months: int, fee_schedule: dict[str, float], vehicles: int) -> None:
        """Create student permit with vehicle count."""
        super().__init__(owner, months, fee_schedule)
        self._vehicles = vehicles

    #part C
    def cost(self) -> float:
        """Monthly rate plus one-time fee for each vehicle after the first."""
        monthly = self._fee_schedule["monthly"]
        extra_car = self._fee_schedule["extra_vehicle"]
        total = self._months * monthly
        if self._vehicles > 1:
            total = total + (self._vehicles - 1) * extra_car
        return total

#part D
    def __str__(self) -> str:
        """Readable string for print."""
        return("StudentPermit(" + self._owner + ", " + str(self._months) + " months, " + str(self._vehicles) + " vehicles)")

    def __repr__(self) -> str:
        """Debug string to recreate object."""
        return ("StudentPermit(" + repr(self._owner) + ", " + repr(self._months) + ", " + repr(self._fee_schedule) + ", " + repr(self._vehicles) + ")")


class FacultyPermit(ParkingPermit):
    """Faculty permit; also tracks garage access."""
    def __init__(self, owner: str, months: int, fee_schedule: dict[str, float], garage: bool) -> None:
        """Create faculty permit with garage flag."""
        super().__init__(owner, months, fee_schedule)
        self._garage = garage

#part C
    def cost(self) -> float:
        """Monthly rate plus garage fee per month if garage is included"""
        monthly = self._fee_schedule["monthly"]
        total = self._months * monthly
        if self._garage:
            garage_fee = self._fee_schedule["garage"]
            total = total + self._months * garage_fee
        return total

#part D
    def __str__(self) -> str:
        """Readable string for print."""
        if self._garage:
            g = "yes"
        else:
            g = "no"
        return("FacultyPermit(" + self._owner + ", " + str(self._months) + " months, garage=" + g + ")")

    def __repr__(self) -> str:
        """Debug string to recreate object."""
        return ("FacultyPermit(" + repr(self._owner) + ", " + repr(self._months) + ", " + repr(self._fee_schedule) + ", " + repr(self._garage) + ")")


# part E
def summarize_list(permits: list[ParkingPermit]) -> float:
    """print each owner name and permit cost. Return total revenue"""
    total = 0.0
    for p in permits:
        c = p.cost()
        print(p._owner, c)
        total = total + c
    return total

#part F
def main() -> None:
    """Demo permits and summarize_list for homework screenshot."""
    print("Doyle Bradford #23673509")
    student_rates: dict[str, float] ={"monthly": 25.0, "extra_vehicle": 10.0}
    faculty_rates: dict[str, float] = {"monthly": 40.0, "garage": 15.0}
    s1 = StudentPermit("Doyle", 2, student_rates, 1)
    s2 = StudentPermit("Zack", 1, student_rates, 3)
    f1 = FacultyPermit("Dr Ionut", 3, faculty_rates, True)
    f2 = FacultyPermit("Dr Bradford", 1, faculty_rates, False)
    print(s1)
    print(repr(s2))
    print(f1)
    print(repr(f2))
    print()
    mixed: list[ParkingPermit] = [s1, s2, f1, f2]
    print("summarize_list:")
    revenue = summarize_list(mixed)
    print("total revenue:", revenue)

if __name__ == "__main__":
    main()
