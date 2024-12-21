class Person:

    people = {}

    def __init__(self, name: "str", age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})

    def add_partner(self, pertner_name: str) -> None:
        self.partner = Person.people[pertner_name]


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for index, obj in enumerate(people_list):
        partner_name = list(people[index].values())[2]
        if partner_name is not None:
            partner = Person.people[list(people[index].values())[2]]
            setattr(obj, list(people[index].keys())[2], partner)
    return people_list
