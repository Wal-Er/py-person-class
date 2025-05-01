class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons = list()
    for human in people:
        persons.append(Person(human["name"], human["age"]))

        persons_index = persons.index(persons[-1])
        human_spouse_key = list(human.keys())[2]
        if human[human_spouse_key]:
            human_spouse_value = human[human_spouse_key]
            setattr(
                persons[persons_index],
                human_spouse_key,
                human_spouse_value
            )

    for person in persons:
        if hasattr(person, "wife"):
            person.wife = person.people.get(person.wife)
        elif hasattr(person, "husband"):
            person.husband = person.people.get(person.husband)

    return persons
