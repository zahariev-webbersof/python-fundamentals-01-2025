def board_tourists(tourists, wagons):
    max_capacity = 4

    for i in range(len(wagons)):
        available_space = max_capacity - wagons[i]

        if tourists > 0 and available_space > 0:
            people_to_board = min(available_space, tourists)
            wagons[i] += people_to_board
            tourists -= people_to_board

    return tourists, wagons


tourists = int(input())
wagons = list(map(int, input().split()))

remaining_tourists, wagons = board_tourists(tourists, wagons)

if remaining_tourists == 0 and any(current_wagon < 4 for current_wagon in wagons):
    print("The lift has empty spots!")
elif remaining_tourists > 0:
    print(f"There isn't enough space! {remaining_tourists} people in a queue!")

print(' '.join(map(str, wagons)))
