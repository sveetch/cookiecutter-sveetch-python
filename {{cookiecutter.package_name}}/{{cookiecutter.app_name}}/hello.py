"""
Hello world sample
==================
"""
from {{ cookiecutter.app_name }}.exceptions import DummyError


class HelloBase:
    """
    Basic hello world builder.

    Keyword Arguments:
        name (str): Name to greet, default to ``world``.
    """
    def __init__(self, name=None):
        self.name = name or "world"

    def greet(self):
        return "Hello {}!".format(self.name)

    def bye(self):
        raise DummyError("I don't like to say goodbye.")


class HelloHTML(HelloBase):
    """
    HTML hello world builder.

    Keyword Arguments:
        container (str): HTML element name to use for container around text.
            Default to ``p`` for HTML paragraph.
    """
    def __init__(self, *args, **kwargs):
        self.container = kwargs.pop("container", None) or "p"
        super().__init__(*args, **kwargs)

    def greet(self):
        text = super().greet()
        return "<{container}>{text}</{container}>".format(
            container=self.container,
            text=text,
        )
