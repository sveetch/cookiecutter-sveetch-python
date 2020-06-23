"""
Main entrance to commandline actions
"""
try:
    import click
except ImportError:
    def cli_frontend(*args, **kwargs):
        print("You don't seem to have installed command line dependancies.")
        print("You should be able to do so with:")
        print("pip install {{ cookiecutter.package_name }}[cli]")
else:
    from {{ cookiecutter.app_name }}.logger import init_logger

    from {{ cookiecutter.app_name }}.cli.version import version_command
    from {{ cookiecutter.app_name }}.cli.greet import greet_command

    # Help alias on '-h' argument
    CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

    # Default logger conf
    APP_LOGGER_CONF = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', None)

    @click.group(context_settings=CONTEXT_SETTINGS)
    @click.option(
        '-v', '--verbose',
        type=click.IntRange(min=0, max=5),
        default=4,
        metavar='INTEGER',
        help=(
            "An integer between 0 and 5, where '0' make a totaly "
            "silent output and '5' set level to DEBUG (the most verbose "
            "level). Default to '4' (Info level)."
        )
    )
    @click.pass_context
    def cli_frontend(ctx, verbose):
        """
        A tool to validate web pages.
        """
        printout = True
        if verbose == 0:
            verbose = 1
            printout = False

        # Verbosity is the inverse of logging levels
        levels = [item for item in APP_LOGGER_CONF]
        levels.reverse()
        # Init the logger config
        root_logger = init_logger("{{ cookiecutter.package_name }}", levels[verbose],
                                  printout=printout)

        # Init the default context that will be passed to commands
        ctx.obj = {
            'verbosity': verbose,
            'logger': root_logger,
        }

    # Attach commands methods to the main grouper
    cli_frontend.add_command(version_command, name="version")
    cli_frontend.add_command(greet_command, name="greet")
