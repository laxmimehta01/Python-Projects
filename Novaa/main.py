import os
import random
import datetime

# customizing voice and speech rate (wpm)
voice = "samantha"
rate = 170 
history = []  # list to store history of nova

# list of random farewells
farewells = [
    "Bye. See you again later.",
    "Goodbye! Take care.",
    "Shutting down. Catch you soon!",
    "See you later, friend!",
    "Signing off. Stay awesome!"
]

if __name__ == "__main__":
    # greeting Nova
    greet = "Hello there. I am Nova, your virtual speaker."
    print(greet)
    os.system(f'say -v {voice} -r {rate} "{greet}"')
    history.append(greet)

    while True:
        text = input("Enter text to speak (or press 'q' to quit) : ").strip()

        # to quit the speaker
        if text.lower() == 'q':
            quit_msg = random.choice(farewells)
            print(quit_msg)
            os.system(f'say -v {voice} -r {rate} "{quit_msg}"')
            history.append(quit_msg)
            break

        # to clear the terminal
        if text.lower() == "clear":
            os.system("clear")
            speak_ready = "I am ready to speak again."
            os.system(f'say -v {voice} -r {rate} "{speak_ready}"')
            continue

        # to handle blanks or empty text
        if text == "":
            print("⚠️ Please enter something to speak!")
            continue

        # speak the entered text
        os.system(f'say -v {voice} -r {rate} "{text}"')
        history.append(text)

    # Save history after session ends
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history.txt", "a") as f:
        f.write(f"\n\n--- Nova Session @ {now} ---\n")
        for i in history:
            f.write(i + "\n")

    print("✅ Nova session history saved to history.txt")
