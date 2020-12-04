# main_example.py
"""
This is a module docstring. It will appear in documentation.

## Notes

You can use Markdown here to make it nicer. Also, in any docstring you
can put a global object import string in backticks, like `other_module.OtherClass`,
and it will be transformed to a link.
"""
from typing import TYPE_CHECKING

from my_project.other_module import BaseClass  # pylint: disable=import-error

if TYPE_CHECKING:
    from my_project.type_defs import StuffCallable  # pylint: disable=import-error

# This is a comment-style documented global variable, so it is added to
# `main_example` module attributes with this comment as a documentation for it
# FIXME: FIXME and TODO comments are igonred
MODULE_NAME = "My Module"

# Private args never appear in docs
_PRIVATE_ATTR = "Private attr"


def hello(name: str) -> str:
    """
    This is module function and it is added to documentation even if it does
    not have a docstring. Function signature will be also generated respecting
    regular and comment-style type annotations. Let's use PEP 257 format here.

    Examples::

        # Google-style code block here, but we could use Markdown code block as well
        >>> hello('John')
        'Hello, John!'

        >>> hello('')
        'Hello!'

    Arguments:
        name -- Name of the person to greet.

    Returns:
        A greeting. No need to put types here if you use type annotations.
    """
    if not name:
        return "Hello!"

    return f"Hello, {name}!"


class MyClass(BaseClass):
    """
    MyClass documentation here.

    .. note:: This time we use RST docstrings format.
    """

    # This is a comment-style documented class attribute, so it is added to
    # `main_example.MyClass` attributes with this comment as a documentation for it.
    STUFF_COUNT = 3

    @classmethod
    def do_something(cls, stuff):
        # type: (StuffCallable) -> bool
        """
        This is a public method that uses comment-style type annotations. If decorators
        or types from annotations are from your project, links to them will be added
        to `See also` section. Since this function depends on `STUFF_COUNT`, we can add
        it to a docstring in backticks and it will be transformed to a link.

        .. code-block:: python

            # usage example
            def my_stuff(amount):
                return amount > 5

            MyClass.do_something(my_stuff)  # False

        .. versionadded:: 1.3
        .. deprecated:: 1.8
        .. versionchanged:: 1.4
            All these directives are added to `Notes` section and formatted in Sphinx-style.

        :param stuff: Function do execute.
        :returns: `stuff` result.
        """
        return stuff(cls.STUFF_COUNT)

    def __bool__(self):
        # type: () -> bool
        """
        Magic methods are added to docs only if they have docstrings.

        :returns: True if `STUFF_COUNT` is not zero
        """
        return self.STUFF_COUNT
