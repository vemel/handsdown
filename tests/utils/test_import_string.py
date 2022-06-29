import pytest

from handsdown.exceptions import ImportStringError
from handsdown.utils.import_string import ImportString


class TestImportString:
    def test_init(self):
        assert ImportString("value").value == "value"
        assert str(ImportString("value")) == "value"
        assert hash(ImportString("value"))
        assert ImportString("value")
        assert not ImportString("")
        assert (ImportString("value") + "add").value == "value.add"
        assert (ImportString("") + "add").value == "add"
        assert ImportString("value") == ImportString("value")
        assert ImportString("value") == "value"
        assert ImportString("value") != ImportString("value1")
        assert ImportString("value") != "value1"
        assert ImportString("value") != b"value"
        assert ImportString("parent.parent2.value").parent.value == "parent.parent2"

        with pytest.raises(ImportStringError):
            _ = ImportString("value").parent

    def test_is_top_level(self):
        assert ImportString("value").is_top_level()
        assert ImportString("").is_top_level()
        assert not ImportString("parent.value").is_top_level()

    def test_startswith(self):
        assert ImportString("parent.parent2.value").startswith(ImportString("parent"))
        assert ImportString("parent.parent2.value").startswith(ImportString("parent.parent2"))
        assert not ImportString("parent.parent2.value").startswith(ImportString("parent2"))
        assert not ImportString("parent.parent2.value").startswith(
            ImportString("parent.parent2value")
        )

    def test_get_parents(self):
        assert not ImportString("value").get_parents()
        assert not ImportString("").get_parents()

        actual = ImportString("parent1.parent2.value").get_parents()
        expected = [
            ImportString("parent1"),
            ImportString("parent1.parent2"),
        ]
        assert all([a == b for a, b in zip(actual, expected)])
