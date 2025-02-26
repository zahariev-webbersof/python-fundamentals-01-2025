class Party:
    def __init__(self):
        self.people = []

    def add_person(self, name):
        self.people.append(name)

    def get_party_info(self):
        party_info = {
            'going': ", ".join(party.people),
            'total': len(party.people)
        }
        return party_info


party = Party()

while True:
    name = input()

    if name == 'End':
        break

    party.add_person(name)

info = party.get_party_info()
print(f'Going:', info['going'])
print(f'Total:', info['total'])
