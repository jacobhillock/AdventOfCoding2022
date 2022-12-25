import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('day', type=int, help='')
    return parser.parse_args()


if __name__ == '__main__':
    sep = '\\' if os.name == 'nt' else '/'

    args = get_args()
    root_dir = sep.join(__file__.split(sep)[:-1])

    new_dir = f'{root_dir}{sep}day{args.day:02d}'

    default_files = [
        'test',
        'input',
        'main.py',
        'README.md'
    ]

    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    for file_name in default_files:
        with open(f'{new_dir}{sep}{file_name}', 'a'):
            pass
