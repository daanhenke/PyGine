import os

from debug.woodcuck import WoodChuck

def main():
    paths = os.path.abspath('logs')
    print paths
    chuck = WoodChuck(pygine=None, to_file=True, to_console=True, mirror_console_emulator=True, log_path=paths)
    chuck.log_raw('Hello blazers', 'log', (255, 255, 0))


if __name__ == '__main__':
    main()
