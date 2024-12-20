import random
import os
os.system('cls')
from colorama import init, Fore, Back, Style

import random
from colorama import init, Fore, Back, Style

# List of 1000 words
word_list = ["cloud, apple, table, chair, beach, clock, happy, world, river, smile, bread, plant, light, stone, clean, sharp, space, ocean, grass, cream, house, flame, tower, dream, sweet, water, green, metal, clear, brown, black, white, dance, cloud, peace, quiet, laugh, magic, bloom, heart, laugh, track, chest, blunt, brick, north, south, amber, blink, grass, fruit, train, crowd, brush, flash, glass, patch, grain, force, angle, prize, charm, coral, steel, curve, crash, crown, drift, pearl, quick, spark, taste, frame, scoop, print, sharp, slice, scale, front, block, broad, split, crust, flash, twist, thick, blend, fling, crack, sweep, flush, dream, realm, gloom, blaze, crisp, flame, flock, grape, lemon, plaza, trend, alert, bingo, cable, eager, float, gloom, lunch, march, quilt, slice, storm, toast, vault, wheat, zebra, arena, batch, brave, bride, chess, choke, clerk, cover, dance, draft, fence, flood, flute, focus, forge, frost, gauge, glare, greet, grill, guard, guilt, inbox, joint, knife, laser, level, lever, lodge, modal, moist, mover, opera, orbit, parka, pause, penny, piano, plank, plush, pulse, queen, racer, raise, range, react, reset, scare, screw, shake, shame, shine, shock, short, sight, slide, spice, squad, stage, stake, steam, store, storm, strip, suite, sweep, tiger, timer, title, toast, tower, trace, trail, train, trash, trend, tribe, trunk, tulip, union, vital, vivid, water, weave, whale, wheat, width, windy, witch, zebra, apple, table, chair, beach, clock, happy, world, river, smile, bread, plant, light, stone, clean, sharp, space, ocean, grass, cream, house, flame, tower, dream, sweet, water, green, metal, clear, brown, black, white, dance, cloud, peace, quiet, laugh, magic, bloom, heart, laugh, track, chest, blunt, brick, north, south, amber, blink, grass, fruit, train, crowd, brush, flash, glass, patch, grain, force, angle, prize, charm, coral, steel, curve, crash, crown, drift, pearl, quick, spark, taste, frame, scoop, print, sharp, slice, scale, front, block, broad, split, crust, flash, twist, thick, blend, fling, crack, sweep, flush, dream, realm, gloom, blaze, crisp, flame, flock, grape, lemon, plaza, trend, alert, bingo, cable, eager, float, gloom, lunch, march, quilt, slice, storm, toast, vault, wheat, zebra, arena, batch, brave, bride, chess, choke, clerk, cover, dance, draft, fence, flood, flute, focus, forge, frost, gauge, glare, greet, grill, guard, guilt, inbox, joint, knife, laser, level, lever, lodge, modal, moist, mover, opera, orbit, parka, pause, penny, piano, plank, plush, pulse, queen, racer, raise, range, react, reset, scare, screw, shake, shame, shine, shock, short, sight, slide, spice, squad, stage, stake, steam, store, storm, strip, suite, sweep, tiger, timer, title, toast, tower, trace, trail, train, trash, trend, tribe, trunk, tulip, union, vital, vivid, water, weave, whale, wheat, width, windy, witch, zebra, apple, table, chair, beach, clock, happy, world, river, smile, bread, plant, light, stone, clean, sharp, space, ocean, grass, cream, house, flame, tower, dream, sweet, water, green, metal, clear, brown, black, white, dance, cloud, peace, quiet, laugh, magic, bloom, heart, laugh, track, chest, blunt, brick, north, south, amber, blink, grass, fruit, train, crowd, brush, flash, glass, patch, grain, force, angle, prize, charm, coral, steel, curve, crash, crown, drift, pearl, quick, spark, taste, frame, scoop, print, sharp, slice, scale, front, block, broad, split, crust, flash, twist, thick, blend, fling, crack, sweep, flush, dream, realm, gloom, blaze, crisp, flame, flock, grape, lemon, plaza, trend, alert, bingo, cable, eager, float, gloom, lunch, march, quilt, slice, storm, toast, vault, wheat, zebra, arena, batch, brave, bride, chess, choke, clerk, cover, dance, draft, fence, flood, flute, focus, forge, frost, gauge, glare, greet, grill, guard, guilt, inbox, joint, knife, laser, level, lever, lodge, modal, moist, mover, opera, orbit, parka, pause, penny, piano, plank, plush, pulse, queen, racer, raise, range, react, reset, scare, screw, shake, shame, shine, shock, short, sight, slide, spice, squad, stage, stake, steam, store, storm, strip, suite, sweep, tiger, timer, title, toast, tower, trace, trail, train, trash, trend, tribe, trunk, tulip, union, vital, vivid, water, weave, whale, wheat, width, windy, witch, zebra, apple, table, chair, beach, clock, happy, world, river, smile, bread, plant, light, stone, clean, sharp, space, ocean, grass, cream, house, flame, tower, dream, sweet, water, green, metal, clear, brown, black, white, dance, cloud, peace, quiet, laugh, magic, bloom, heart, laugh, track, chest, blunt, brick, north, south, amber, blink, grass, fruit, train, crowd, brush, flash, glass, patch, grain, force, angle, prize, charm, coral, steel, curve, crash, crown, drift, pearl, quick, spark, taste, frame, scoop, print, sharp, slice, scale, front, block, broad, split, crust, flash, twist, thick, blend, fling, crack, sweep, flush, dream, realm, gloom, blaze, crisp, flame, flock, grape, lemon, plaza, trend, alert, bingo, cable, eager, float, gloom, lunch, march, quilt, slice, storm, toast, vault, wheat, zebra, arena, batch, brave, bride, chess, choke, clerk, cover, dance, draft, fence, flood, flute, focus, forge, frost, gauge, glare, greet, grill, guard, guilt, inbox, joint, knife, laser, level, lever, lodge, modal, moist, mover, opera, orbit, parka, pause, penny, piano, plank, plush, pulse, queen, racer, raise, range, react, reset, scare, screw, shake, shame, shine, shock, short, sight, slide, spice, squad, stage, stake, steam, store, storm, strip, suite, sweep, tiger, timer, title, toast, tower, trace, trail, train, trash, trend, tribe, trunk, tulip, union, vital, vivid, water, weave, whale, wheat, width, windy, witch, zebra, apple, table, chair, beach, clock, happy, world, river, smile, bread, plant, light, stone, clean, sharp, space, ocean, grass, cream, house, flame, tower, dream, sweet, water, green, metal, clear, brown, black, white, dance, cloud, peace, quiet, laugh, magic, bloom, heart, laugh, track, chest, blunt, brick, north, south, amber, blink, grass, fruit, train, crowd, brush, flash, glass, patch, grain, force, angle, prize, charm, coral, steel, curve, crash, crown, drift, pearl, quick, spark, taste, frame, scoop, print, sharp, slice, scale, front, block, broad, split, crust, flash, twist, thick, blend, fling, crack, sweep, flush, dream, realm, gloom, blaze, crisp, flame, flock, grape, lemon, plaza, trend, alert, bingo, cable, eager, float, gloom, lunch, march, quilt, slice, storm, toast, vault, wheat, zebra, arena, batch, brave, bride, chess, choke, clerk, cover, dance, draft, fence, flood, flute, focus, forge, frost, gauge, glare, greet, grill, guard, guilt, inbox, joint, knife, laser, level, lever, lodge, modal, moist, mover, opera, orbit, parka, pause, penny, piano, plank, plush, pulse, queen, racer, raise, range, react, reset, scare, screw, shake, shame, shine, shock, short, sight, slide, spice, squad, stage, stake"]

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
    print("Welcome to Wordle! Guess the 5-letter word. Red means wrong letter, Yellow means right letter wrong place, Green means right letter right place")

    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess not in word_list:
            print("Word not in list. Try again.")
            continue

        feedback = get_feedback(secret_word, guess)
        print(f"Feedback: {feedback}")

        if guess == secret_word:
            print("Congratulations! You've guessed the word!")
            break

        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word}")

# Run the game
play_wordle()