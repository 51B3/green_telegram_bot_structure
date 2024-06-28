import os
import cutie
from colorama import Fore
from tqdm import tqdm
from art import tprint

# The tuple is an ordered structure for creating project objects, where elements are passed in the format: path, object, data (optional)
master = (
    ('.', 'core'),
    ('core', 'databases'),
    ('core\\databases', 'methods'),
    ('core\\databases', 'models'),
    ('core', 'exceptions'),
    ('core', 'handlers'),
    ('core\\handlers', 'callbacks.py', ''),
    ('core\\handlers', 'commands.py', ''),
    ('core\\handlers', 'documents.py', ''),
    ('core\\handlers', 'messages.py', ''),
    ('core', 'keyboards'),
    ('core\\keyboards', 'inline.py', ''),
    ('core\\keyboards', 'reply.py', ''),
    ('core', 'misc'),
    ('core', 'utils'),
    ('core\\utils', 'FSM'),
    ('core', 'main.py', ''),
    ('.', '.env', 'TOKEN = \'\''),
    ('.', '.gitignore', ''),
    ('.', 'run.py', '')
)


def label():
    print(Fore.GREEN)
    tprint('Green Telegram bot structure', font="mini")
    print(Fore.RESET, end='\r')


def creation(arg):
    for el in tqdm(arg, bar_format='|{bar:30}{r_bar}', colour='GREEN'):
        # Checking the existence of an object path
        if not os.path.exists(el[0]):
            continue

        # Checking the type of the transmitted object
        if len(el) == 3:
            with open(f'{el[0]}\\{el[1]}', 'w') as file:
                try:
                    file.write(el[2])
                except:
                    continue
        else:
            os.mkdir(f'{el[0]}\\{el[1]}')


def main():
    label()
    if cutie.prompt_yes_or_no(
        'Quick generation of the project structure?',
        default_is_yes=True,
        yes_text='Yes',
        no_text='No'
    ):
        creation(master)
    else:
        os.system('cls')
        label()
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
        selection = cutie.select_multiple(
            tree,
            deselected_unticked_prefix="● ",
            deselected_ticked_prefix="× ",
            selected_unticked_prefix=Fore.GREEN + "○ " + Fore.RESET,
            selected_ticked_prefix=Fore.GREEN + "× " + Fore.RESET,
            hide_confirm=False,
            deselected_confirm_label="CONFIRM",
            selected_confirm_label=Fore.GREEN + "CONFIRM" + Fore.RESET)
        # Calling an object creation function in which objects rejected during selection are not passed as part of an argument
        creation(tuple(el for i, el in enumerate(master) if i not in selection))
    os.remove(os.path.basename(__file__))


if __name__ == '__main__':
    main()
