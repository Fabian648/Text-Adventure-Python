import random
import map
import characters

def game_help():
    print(commands.keys())

def fight():
    enemies = map.get_enemies()
    while len(enemies) > 0:
        current_enemy = enemies[0]
        characters.get_hit(current_enemy)
        if current_enemy[characters.HEALTH] <= 0:
            enemies.remove(current_enemy)
        for enemy in enemies:
            characters.get_hit(characters.PLAYER, current_enemy)
        print("You are wounded and have " + str(characters.PLAYER[characters.HEALTH]) + " hp left")

commands = {
    "help": game_help,
    "quit": lambda : exit("You commit suicide and leave this world."),
    "fight": fight,
    "rest": characters.game_rest_player,
    "forward": map.forward,
    "backwards": map.backwards,
    "right": map.right,
    "left": map.left
}

dealercommands = {}


if __name__ == "__main__":
    characters.PLAYER[characters.NAME] = input("Enter your name: ")
    map.init(10, 10)
    print("Type help to list the available commands\n")
    while True:
        command = input("> ").lower().split(" ")[0]
        if command in commands:
            commands[command]()
        else:
            print("You run around in circles and don't know what to do.")
        map.print_current_enemies()