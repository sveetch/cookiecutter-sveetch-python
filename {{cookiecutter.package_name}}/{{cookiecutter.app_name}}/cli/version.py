import click

from {{ cookiecutter.app_name }} import __version__


@click.command()
@click.pass_context
def version_command(context):
    """
    Print out version information.
    """
    click.echo("{{ cookiecutter.package_name }} {}".format(__version__))
