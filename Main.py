# Before running the code, please install dependencies
# pip install pygame speech_recognition pyaudio
import speech_recognition as sr
import pygame

def word_count():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Word count:", len(words))

def calculate_average_score():
    try:
        with open('students.txt', 'r') as file:
            total_score = 0
            count = 0
            for line in file:
                parts = line.split()
                score = int(parts[-1])
                total_score += score
                count += 1
            average_score = total_score / count
            print(f"Average score: {average_score:.2f}")
    except FileNotFoundError:
        print("The file students.txt was not found.")

def mouse_interaction():
    pygame.init()
    size = (400, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mouse Interaction")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                print(f"Mouse moved to {event.pos}")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse clicked at {event.pos}")
        pygame.display.flip()
    pygame.quit()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("You said: " + recognized_text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said")
    except sr.RequestError as e:
        print(f"Error occurred; {e}")

def main():
    tasks = {
        '1': word_count,
        '2': calculate_average_score,
        '3': mouse_interaction,
        '4': speech_to_text
    }

    while True:
        choice = input(
            "\nWhich task would you like to run?\n1. Word Count\n2. Student Score Average\n3. Mouse Interaction\n4. Speech to Text\nEnter number or 'q' to quit: ")
        if choice == 'q':
            print("Exiting program.")
            break
        task = tasks.get(choice)
        if task:
            task()
        else:
            print("Invalid choice. Please enter a valid option or 'q' to quit.")

if __name__ == "__main__":
    main()
