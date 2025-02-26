class Lift:
    def __init__(self, wagons):
        self.wagons = wagons
        self.max_capacity = 4

    def board_tourists(self, tourists):
        for i in range(len(self.wagons)):
            available_space = self.max_capacity - self.wagons[i]

            if tourists > 0 and available_space > 0:
                people_to_board = min(available_space, tourists)
                self.wagons[i] += people_to_board
                tourists -= people_to_board

        return tourists

    def __str__(self):
        return ' '.join(map(str, self.wagons))


def main():
    tourists = int(input())
    current_wagons = list(map(int, input().split()))
    lift = Lift(current_wagons)
    remaining_tourists = lift.board_tourists(tourists)

    if remaining_tourists == 0 and any(current_wagon < lift.max_capacity for current_wagon in lift.wagons):
        print("The lift has empty spots!")
    elif remaining_tourists > 0:
        print(f"There isn't enough space! {remaining_tourists} people in a queue!")

    print(lift)

if __name__ == '__main__':
    main()