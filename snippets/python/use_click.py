#!/usr/bin/env python
import click

"""
ref: https://dbader.org/blog/python-commandline-tools-with-click
https://click.palletsprojects.com/en/8.0.x/options/
"""

@click.command()
@click.option('--input','-i',help='help example', required=True)
@click.option('--output','-o', help='2nd help')
def main(input, output):
    click.echo(input)
    click.echo(output)
        
if __name__ == '__main__':
    main()
