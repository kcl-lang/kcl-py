schema BasePerson:
    fullName = firstName + ' ' + lastName
    firstName: str
    lastName: str

schema Person(BasePerson):
    firstName = "John"
    lastName: str

JohnDoe = Person {
    lastName: "Doe"
}
