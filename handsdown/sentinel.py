from typing import Text


class Sentinel:
    """
    Sentinel value than can be used as a placeholder.
    Doc generation friendly.

    Examples::
        NOT_SET = Sentinel('NOT_SET')

        def check_value(name=NOT_SET):
            if name is NOT_SET:
                return 'This is a NOT_SET value'

            return 'This is something else'

        repr(NOT_SET) # 'NOT_SET'

    Arguments:
        name -- String used as a representation of the object.
    """

    def __init__(self, name="DEFAULT"):
        # type: (Text) -> None
        self._name = name

    def __repr__(self):
        # type: () -> Text
        return self._name

    def __str__(self):
        # type: () -> Text
        return self._name
