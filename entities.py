class Entity:
    def __init__(self, entity_type, value):
        self.entity_type = entity_type
        self.value = value
        self.properties = {}

    def add_property(self, key, value):
        self.properties[key] = value

    def __str__(self):
        return f"{self.entity_type}: {self.value}"

# Example entity types
class Person(Entity):
    def __init__(self, name):
        super().__init__("Person", name)

class Domain(Entity):
    def __init__(self, domain):
        super().__init__("Domain", domain)
