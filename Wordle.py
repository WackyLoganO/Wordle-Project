import random
import os
os.system('cls')
from colorama import Fore, Back

word_list = ["wacky", "legos", "build", "guild", "pelts", "varys", "carry", "marry", "ferry", "fairy", "weary", "wrong", "exist", "tempt", "enter", "trams", "hairy", "dairy", "sight", "coded", "pulls", "issue", "forks", "watch", "seeds", "beads", "chart", "creed", "greed", "breed", "bleed", "reset", "lists", "guess", "styles", "games", "plays", "input", "wrong", "songs", "sorry", "story", "words", "place", "smell", "means", "yells", "mails", "tails", "tales", "fails", "hales", "atoll", "plate", "flute", "cents", "sense", "taste", "haste", "stale", "stout", "trout", "clout", "stole", "stilt", "stops", "wools", "roles", "rolls", "rules", "bears", "bares", "coast", "toast", "fares", "fairs", "cares", "ghost", "boots", "horse", "bells", "queen", "hyena", "skunk", "green", "balls", "wales", "nears", "close", "hoses", "poses", "loses", "anvil", "field", "heals", "meals", "ready", "yetis", "garlic", "weaps", "heads", "lemon", "thyme", "times", "clove", "chive", "chime", "hives", "swarm", "warms", "onion", "mince", "curry", "soups", "loops", "hoops", "chili", "chile", "basil", "weedy", "seedy", "needy", "kneed", "whole", "spice", "poppy", "poopy", "garam", "peels", "heals", "heels", "stick", "chick", "human", "cumin", "shoes", "whose", "those", "teddy", "ready", "sweat", "break", "shake", "hates", "makes", "takes", "lakes", "chain", "train", "lanes", "rains", "zebra", "shape", "capes", "tapes", "gapes", "gleam", "clean", "light", "ninja", "happy", "honey", "funny", "money", "kites", "mites", "yours", "where", "hairs", "glare", "mares", "house", "mouse", "mates", "keeps", "freed", "llama", "lapel", "clear", "blare", "clean", "clams", "angel", "plums", "glean", "slips", "death", "flask", "broke", "bloke", "stoke", "stove", "spike", "hands", "bands", "small", "calls", "hauls", "leaps", "heaps", "cheap", "sheep", "shave", "ladel", "table", "plane", "canes", "flaps", "claps", "legal", "truck", "right", "frays", "drain", "stray", "grain", "brain", "dream", "bread", "array", "crane", "hello", "magic", "cloud", "about", "after", "again", "below", "bring", "chair", "clock", "dance", "eight", "false", "fight", "front", "grape", "heart", "house", "jolly", "judge", "liver", "loose", "money", "night", "paint", "plane", "power", "quiet", "raise", "scale", "sheer", "short", "sleep", "smile", "stone", "table", "thick", "threw", "tight", "under", "video", "water", "woman", "world", "write", "young", "zebra", "apple", "black", "brown", "candy", "clash", "cliff", "couch", "drink", "dusty", "flame", "floor", "flood", "folds", "march", "peach", "pitch", "plumb", "scout", "worth", "lunar", "serve", "spoon", "smoke", "smash", "steam", "straw", "stone", "stain", "sunny", "sight", "wager", "wagon", "march", "vivid", "waste", "bison", "flirt", "honor", "clash", "sugar", "spark", "smart", "stark", "start", "steak", "short", "shift", "steal", "steel", "stave", "stuck", "shade", "sweep", "swarm", "snoop", "stone", "stool", "scale", "slink", "stack", "stack", "splash", "sharp", "scout", "stone", "stain", "stone", "sharp", "press", "knock", "light", "sweep", "scope", "trump", "thorn", "whack", "punch", "pouch", "crash", "doubt", "fight", "blend", "brake", "snare", "scare", "scorn", "stalk", "shout", "stand", "sworn", "worse", "fight", "score", "sword", "paste", "steal", "shale", "stead", "tread", "purse", "whale", "plush", "prune", "pearl", "tally", "track", "staff", "stack", "sweep", "traps", "pouch", "charm", "shade", "shine", "stark", "knack", "piano", "doubt", "drawn", "grill", "scroll", "think", "bliss", "style", "where", "scrap", "claim", "study", "bring", "trick", "stare", "smear", "sworn", "whale", "touch", "crack", "stand", "track", "spoon", "gloom", "grape", "grind", "pearl", "flour", "place", "spine", "fresh", "serve", "swipe", "spare", "spoon", "pest", "spine", "tread", "skirt", "swept", "perch", "score", "grape", "stray", "loose", "stone", "stain", "slate", "skate", "prong", "plume", "grove", "stack", "steel", "scent", "steel", "scoot", "prone", "start", "shoot"]
# Function to provide feedback on the guess
def get_feedback(secret_word, guess):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append(Back.GREEN + " " + Back.RESET)  # Correct letter in the correct place
        elif guess[i] in secret_word:
            feedback.append(Back.YELLOW + " " + Back.RESET)  # Correct letter in the wrong place
        else:
            feedback.append(Back.RED + " " + Back.RESET)  # Incorrect letter
    return ''.join(feedback)

# Main game function
def play_wordle():
    secret_word = random.choice(word_list)
    attempts = 6
    print(Fore.LIGHTBLUE_EX + "Welcome to Wordle! Guess the 5-letter word. " + Fore.RED + "Red" + Fore.LIGHTBLUE_EX + " means wrong letter, " + Fore.YELLOW + "Yellow" + Fore.LIGHTBLUE_EX + " means right letter wrong place, " + Fore.GREEN + "Green" + Fore.LIGHTBLUE_EX + " means right letter right place")

    while attempts > 0:
        guess = input(Fore.LIGHTBLUE_EX + "Enter your guess: "  + Fore.RESET).lower()
        if len(guess) != 5:
            print(Fore.LIGHTBLUE_EX + "Please enter a 5-letter word.")
            continue
        if guess not in word_list:
            print(Fore.LIGHTBLUE_EX + "Word does not exist. Try again.")
            continue

        feedback = get_feedback(secret_word, guess)
        print(f"Feedback: {feedback}")

        if guess == secret_word:
            print(Fore.LIGHTBLUE_EX + "Congratulations! You guessed the word!" + Fore.RESET)
            break

        attempts -= 1
        print(Fore.LIGHTBLUE_EX + f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(Fore.LIGHTBLUE_EX + f"Sorry, you've run out of attempts. The word was: {secret_word}" + Fore.RESET)

# Run the game
play_wordle()