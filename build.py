import os
import cutie
from colorama import Fore, Style
from tqdm import tqdm
from art import tprint

master = [
    'md core',
    'md core\databases',
    'md core\databases\methods',
    'md core\databases\models',
    'md core\exceptions',
    'md core\handlers',
    'type nul > core\handlers\callbacks.py',
    'type nul > core\handlers\commands.py',
    'type nul > core\handlers\documents.py',
    'type nul > core\handlers\messages.py',
    'md core\keyboards',
    'type nul > core\keyboards\inline.py',
    'type nul > core\keyboards\\reply.py',
    'md core\misc',
    'md core\\utils',
    'md core\\utils\FSM',
    'type nul > core\main.py',
    'type nul > run.py',
    '@echo off &echo./env>.gitignore',
    '@echo off &echo.TOKEN = \'\'>.env',
    'del core\main.py core\handlers\callbacks.py core\handlers\commands.py core\handlers\documents.py core\handlers\messages.py core\keyboards\inline.py core\keyboards\\reply.py & rd core\databases\methods core\databases\models core\databases core\exceptions core\handlers core\keyboards core\misc core\\utils\FSM core\\utils core',
    'rd core\databases\methods core\databases\models core\databases',
    'rd core\databases\methods',
    'rd core\databases\models',
    'rd core\exceptions',
    'del core\handlers\callbacks.py core\handlers\commands.py core\handlers\documents.py core\handlers\messages.py & rd core\handlers',
    'del core\handlers\callbacks.py',
    'del core\handlers\commands.py',
    'del core\handlers\documents.py',
    'del core\handlers\messages.py',
    'del core\keyboards\inline.py core\keyboards\\reply.py & rd core\keyboards',
    'del core\keyboards\inline.py',
    'del core\keyboards\\reply.py',
    'rd core\misc',
    'rd core\\utils\FSM core\\utils',
    'rd core\\utils\FSM',
    'del core\main.py',
    'del .env',
    'del .gitignore',
    'del run.py'
]


def logo():
    print(Fore.GREEN)
    tprint('Green Telegram bot structure', font="mini")
    print(Style.RESET_ALL, end='\r')


def main():
    logo()
    if cutie.prompt_yes_or_no(
        'Quick generation of the project structure?',
        default_is_yes=True,
        yes_text='Yes',
        no_text='No'
    ):
        process([i for i in range(0, 20)])
    else:
        os.system('cls')
        logo()
        print('Select the directories or files that will not be created:\n<project>')
        tree = [
            '  ├─ <core>',
            '  │     ├─ <database>',
            '  │     │       ├─ <methods>',
            '  │     │       └─ <models>',
            '  │     ├─ <exceptions>',
            '  │     ├─ <handlers>',
            '  │     │       ├─ callbacks.py',
            '  │     │       ├─ commands.py',
            '  │     │       ├─ documents.py',
            '  │     │       └─ messages.py',
            '  │     ├─ <keyboards>',
            '  │     │       ├─ inline.py',
            '  │     │       └─ reply.py',
            '  │     ├─ <misc>',
            '  │     ├─ <utils>',
            '  │     │     └─ <FSM>',
            '  │     └─ main.py',
            '  ├─ .env',
            '  ├─ .gitignore',
            '  └─ run.py'
        ]
        choice = cutie.select_multiple(
            tree,
            deselected_unticked_prefix="● ",
            deselected_ticked_prefix="× ",
            selected_unticked_prefix=Fore.GREEN + "○ " + Style.RESET_ALL,
            selected_ticked_prefix=Fore.GREEN + "× " + Style.RESET_ALL,
            hide_confirm=False,
            deselected_confirm_label="CONFIRM",
            selected_confirm_label=Fore.GREEN + "CONFIRM" + Style.RESET_ALL)
        process([i for i in range(0, 20)] +
                list(map(lambda x: x+20, choice)))


def process(arg):
    print('\r')
    for command in tqdm(arg, bar_format='|{bar:30}{r_bar}', colour='GREEN'):
        os.system(master[command])
    complete()


def complete():
    os.remove(os.path.basename(__file__))


if __name__ == '__main__':
    main()
