def process_todo_notes(todo_notes):
    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    string_sorted = [note.split('-')[1] for note in sorted_notes]
    return string_sorted


todo_ = []
while True:
    note = input()
    if note == 'End':
        break
    todo_.append(note)

result = process_todo_notes(todo_)
print(result)
