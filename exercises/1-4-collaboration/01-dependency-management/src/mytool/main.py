import click

from . import analysis


@click.command("mytool")
@click.argument("a", type=int)
@click.argument("b", type=int)
def main(a: int, b: int):
    click.echo(analysis.calculate(a, b))
