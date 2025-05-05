import random

class ForestGame:

    def start_game(self):

        name = input("Enter your Beautiful Name:")

        print(f"\nWelcome {name},Mystery Forest Gold Hunt Adventure Game!")
        print("You will be lose in forest and find your Team mates or Gold Cave")

        direction = input("\nWhich Direction Do You Want to Go (forward/backward/left/right)?").lower()

        if direction == 'forward':
            forward = Forward()
            forward.forward()

        elif direction == 'backward':
            backward = Backward()
            backward.backward()

        elif direction == 'left':
            left = Left()
            left.left()

        elif direction == 'right':
            right = Right()
            right.right()

    def quit(self):
        print("\nMystery Forest Gold Hunt Adventure Game was Quit")

    def final_path(self):
        gold_coin = 0
        print("You now must choose your final direction to reach the gold cave.")
        directions = ["north", "south", "east"]
        correct_direction = random.choice(directions)

        choice = input("Which direction do you go? (north/south/east): ").lower()

        if choice == correct_direction:
            print("You found the Gold Cave, You Win!")
            gold_coin += 1000
            print(f"{gold_coin} GOLD COINS ARE RECEIVED")
            self.quit()
        else:
            print("Wrong direction!")
            print(f"The correct direction was: {correct_direction}")
            print("You walk in circles and end up back at the starting place. Game Over.")


class Forward(ForestGame):

    def forward(self):
        print("Your path going the reach the River")
        river_direction = input("Now you reached the river.Do you swim or walk across the river\n")

        if river_direction == 'swim':
            self.swim()

        elif river_direction == 'walk':
            self.walk()

    def swim(self):
        print("Now you choose to swim the River")
        print("You lose the game , because of Crocodiles round and eat you")
        self.quit()

    def walk(self):
        print("Now you choose to walk across the River")
        print("You may reach the Village,you can able to reach your Home through the train,You lose the game")
        self.quit()

class Backward(ForestGame):

    def backward(self):
        print("You lose the game, because of burial ground")
        self.quit()

class Left(Forward,ForestGame):

    def left(self):
        print("Now you choose to Left direction\n")
        left_direction = input("you reach the one old guest house, Do you Want to go inside or walk")
        if left_direction == 'inside':
            self.inside()

        elif left_direction == 'walk':
            self.walk()

    def inside(self):
        print("Now you choose to going inside the guest house")
        print("Inside the Guest House,You find the Gold cave map and flashlight")
        self.final_path()
        self.quit()

class Right(ForestGame):

    def right(self):
        gold_coins = 0
        print("Now you choose to Right direction")
        print("you can reach the under the Dark Forest")
        choice = input("Which Direction Do you want to go (north or south)")
        if choice == 'north':
            print("You can able to reach your teammates and easy to find Gold Cave,You win")
            gold_coins += 1000
            print(f"{gold_coins} GOLD COINS ARE RECEIVED ")
            self.quit()
        else:
            print("You lose the Game!")
            self.quit()

def main():

    forest = ForestGame()
    forest.start_game()

if __name__ == '__main__':
    main()












