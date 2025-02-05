people = [('Ani', 30), ('Bat Boyko', 62), ('Mike', 55)]

sorted_people = sorted(people, key=lambda person: person[1])

print(sorted_people)