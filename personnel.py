from datetime import date

class personnel:
    def __init__(self, firstname: str, lastname: str, experience: int, salary: int, birthday: date ) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.exp = experience
        self.salary = salary
        self.birthday = birthday


    def __str__(self) -> str:
        return f"{self.firstname.title()} {self.lastname.title()}"

    def __gt__(self, other) -> bool:
        return self.salary > other.salary
    
    def __le__(self,other) -> bool:
        return self.exp <= other.exp

    def congrat(self) -> None:
        print(f"today {self}'s birthday. {self} wokrs for this company.")

    def birthd(self) -> date:
        return self.birthday


person1: personnel = personnel("liza", "tsibadze", 12, 40_000, date(year = 1992, month = 6, day = 23))
person2: personnel = personnel("Tornike", "tsibadze", 17, 45_000, date(year = 1986, month = 8, day = 28))
person3: personnel = personnel("Nikoloz", "tsibadze", 20, 42_000, date(year = 1983, month = 9, day = 11))


# print(person1 > person2)
# print(person3 <= person1)
# print(person1)
person2.congrat()
print(person3.birthd())