import PySimpleGUI as sg
import random
import data

def generate_random_number():
    return random.randint(1, 100)

def play_guess_the_number():
    secret_number = generate_random_number()
    attempts = 0

    layout = [
        [sg.Text("Вгадайте число від 1 до 100.")],
        [sg.InputText(key="input_guess")],
        [sg.Button("Відправити"), sg.Button("Вийти")],
        [sg.Text("", size=(30, 2), key="output_message")]
    ]

    window = sg.Window("Гра 'Вгадай число'", layout, resizable=True, finalize=True, element_justification="c")

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вийти":
            break

        user_guess = values["input_guess"]

        if user_guess.isnumeric():
            user_guess = int(user_guess)
            attempts += 1

            if user_guess == secret_number:
                window["output_message"].update(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб.")
                window["input_guess"].update(disabled=True)
                window["Відправити"].update(disabled=True)
                break
            elif user_guess < secret_number:
                window["output_message"].update("Спробуйте більше.")
            else:
                window["output_message"].update("Спробуйте менше.")
        else:
            window["output_message"].update("Будь ласка, введіть число.")

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вийти":
            break

    window.close()