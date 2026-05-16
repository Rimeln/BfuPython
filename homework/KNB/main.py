import random

class Move:
    k = "камень"
    b = "бумага"
    n = "ножницы"

    @staticmethod
    def get_winner(player_move, computer_move):
        if player_move == computer_move:
            return "Ничья"

        rules = {
            Move.k: Move.n,
            Move.n: Move.b,
            Move.b: Move.k
        }

        if rules[player_move] == computer_move:
            return "Игрок"
        else:
            return "Компьютер"

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

class Game:
    def __init__(self):
        self.player = Player("Игрок")
        self.computer = Player("Компьютер")
        self.moves = [Move.k, Move.b, Move.n]
        self.rounds = 0

    def computer_move(self):
        return random.choice(self.moves)

    def play_round(self, player_choice):
        computer_choice = self.computer_move()
        winner = Move.get_winner(player_choice, computer_choice)
        if winner == "Игрок":
            self.player.add_score()
            result = "победа"
        elif winner == "Компьютер":
            self.computer.add_score()
            result = "поражение"
        else:
            result = "ничья"

        self.rounds += 1

        return {
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'winner': winner,
            'result': result
        }

    def reset(self):
        self.player.reset_score()
        self.computer.reset_score()
        self.rounds = 0

    def get_scores(self):
        return {
            'player': self.player.score,
            'computer': self.computer.score
        }

def main():
    game = Game()

    print("=" * 50)
    print("Игра Камень Ножницы Бумага")
    print("=" * 50)

    while True:
        print(f"\nСчет: Игрок {game.player.score} : {game.computer.score} Компьютер")
        print("\nВаш ход:")
        print("1 - Камень")
        print("2 - Бумага")
        print("3 - Ножницы")
        print("0 - Выйти из игры")

        try:
            choice = int(input("\nВыберите (0-3): "))

            if choice == 0:
                print("\nСпасибо за игру!")
                print(f"Финальный счет: Игрок {game.player.score} : {game.computer.score} Компьютер")
                break

            if choice not in [1, 2, 3]:
                print("Ошибка! Выберите 1, 2, 3 или 0")
                continue

            moves_map = {1: Move.k, 2: Move.b, 3: Move.n}
            player_choice = moves_map[choice]

            result = game.play_round(player_choice)

            print("\n" + "-" * 30)
            print(f"Ваш ход: {result['player_choice']}")
            print(f"Ход компьютера: {result['computer_choice']}")
            print("-" * 30)

            if result['winner'] == 'player':
                print("Победа")
            elif result['winner'] == 'computer':
                print("Поражение")
            else:
                print("Ничья")

            if game.player.score >= 5:
                print("\n" + "=" * 50)
                print("Вы выиграли")
                print("=" * 50)
                game.reset()
                play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
                if play_again == 'да':
                    continue
                else:
                    print("\nСпасибо за игру!")
                    break

            elif game.computer.score >= 5:
                print("\n" + "=" * 50)
                print("Компьютер выиграл")
                print("=" * 50)
                game.reset()
                play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
                if play_again == 'да':
                    continue
                else:
                    print("\nСпасибо за игру!")
                    break

        except ValueError:
            print("Ошибка! Введите число от 0 до 3")

if __name__ == "__main__":
    main()