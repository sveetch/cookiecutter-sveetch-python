"""
Hello world sample
==================

"""
from {{ cookiecutter.app_name }}.exceptions import DummyError


class HelloBase:
    """
    Basic hello world builder.

    Atribute:
        name (str): Name to greet, default to ``world``.

    Keyword Arguments:
        name (str): Define a custom name to greet if given.
    """
    def __init__(self, *args, name=None, **kwargs):
        self.name = name or "world"

    def greet(self):
        """
        Return the greeting text.

        Returns:
            str: Complete greeting text with name.
        """
        return "Hello {}!".format(self.name)

    def bye(self):
        """
        Unimplemented method for demonstration and test purpose around
        application exceptions.

        Raises:
            {{ cookiecutter.app_name }}.exceptions.DummyError: A basic
            exception.
        """
        raise DummyError("I don't like to say goodbye.")


class HelloHTML(HelloBase):
    """
    HTML hello world builder to surround greeting text with a HTML element.

    Atribute:
        container (str): HTML element name to use for container around text.
            Default to ``p`` for HTML paragraph.

    Keyword Arguments:
        container (str): Define a custom HTML element name to use for container
            if given.
    """
    def __init__(self, *args, **kwargs):
        self.container = kwargs.pop("container", None) or "p"
        super().__init__(*args, **kwargs)

    def greet(self):
        """
        Return the greeting text surrounded by HTML element container.

        Returns:
            str: Complete greeting text with name surrounded by container.
        """
        text = super().greet()
        return "<{container}>{text}</{container}>".format(
            container=self.container,
            text=text,
        )
