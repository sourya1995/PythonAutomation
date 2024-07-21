#!/usr/bin/python3

import click

@click.command()
@click.option('--greeting', '-g', default='Ahoy there', help='Greeting')
@click.option('--name', '-n', default='Mate', help='Name')
def greet(greeting, name):
    click.echo(f'{greeting}, {name}')

if __name__ == '__main__':
    greet()