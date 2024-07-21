#!/usr/bin/python3

import argparse

def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail")

def list_ships():
    ships = ["Your ship", "My ship", "The ship"]
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f'{greeting}, {name}'
    print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maritime Control')
    parser.add_argument('--twice', '-t', help='Do it twice', action='store_true')
    subparsers = parser.add_subparsers(dest='func')
    ship_parser = subparsers.add_parser('ships', description='Ship related commands')
    ship_parser.add_argument('command', choices=['list', 'sail'])
    sailor_parser = subparsers.add_parser('sailors', help='talk to a sailor')
    sailor_parser.add_argument('name',  help='Name of the sailor')
    sailor_parser.add_argument('--greeting', '-g', help='Greeting', default='Ahoy there')
    args = parser.parse_args()
    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()