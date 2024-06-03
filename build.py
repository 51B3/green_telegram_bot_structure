import os
import cutie
from colorama import Fore, Style
from tqdm import tqdm
from art import tprint

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

master = [
    'md core',
    'cd core & md databases',
    'cd core\databases & md methods',
    'cd core\databases & md models',
    'cd core & md exceptions',
    'cd core & md handlers',
    'cd core\handlers & type nul > callbacks.py',
    'cd core\handlers & type nul > commands.py',
    'cd core\handlers & type nul > documents.py',
    'cd core\handlers & type nul > messages.py',
    'cd core & md keyboards',
    'cd core\keyboards & type nul > inline.py',
    'cd core\keyboards & type nul > reply.py',
    'cd core & md misc',
    'cd core & md utils',
    'cd core\\utils & md FSM',
    'cd core & type nul > main.py',
    'type nul > run.py',
    '@echo off &echo./env>.gitignore',
    '@echo off &echo.TOKEN = \'\'>.env',
    'cd core & del main.py /f & rd exceptions misc & cd databases & rd methods models & cd .. & rd databases & cd handlers & del callbacks.py commands.py documents.py messages.py & cd .. & rd handlers & cd keyboards & del inline.py reply.py & cd .. & rd keyboards & cd utils & rd FSM & cd .. & rd utils & cd .. & rd core',
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
        Style.RESET_ALL + 'Quick generation of the project structure?',
        default_is_yes=True,
        yes_text='Yes',
        no_text='No'
    ):
        process([i for i in range(0, 20)])
    else:
        os.system('cls')
        logo()
        print('Select the directories or files that will not be created:\n<project>')
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


def process(list):
    for command in tqdm(list, bar_format='|{bar:30}{r_bar}', colour='GREEN'):
        os.system(master[command])
    complete()


def complete():
    os.remove(os.path.basename(__file__))


if __name__ == '__main__':
    main()
