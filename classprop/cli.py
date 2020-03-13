# -*- coding: utf-8 -*-

"""Console script for classprop."""
import sys
import typing

import click


@click.command()
def main(args: typing.Optional[str] = None) -> int:
    """Console script for classprop."""
    click.echo("Replace this message by putting your code into classprop.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
