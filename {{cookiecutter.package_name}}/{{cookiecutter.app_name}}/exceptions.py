"""
Specific application exceptions.
"""


class {{ cookiecutter.__class_name }}BaseException(Exception):
    """
    Exception base.

    You should never use it directly except for test purpose. Instead make or
    use a dedicated exception related to the error context.
    """
    pass


class AppOperationError({{ cookiecutter.__class_name }}BaseException):
    """
    Sample exception to raise from your code.
    """
    pass
