# pylint: disable=missing-docstring
import unittest

from handsdown.utils.import_string import ImportString, ImportStringError


class TestImportString(unittest.TestCase):
    def test_init(self):
        self.assertEqual(ImportString("value").value, "value")
        self.assertEqual(str(ImportString("value")), "value")
        self.assertTrue(hash(ImportString("value")))
        self.assertTrue(ImportString("value"))
        self.assertFalse(ImportString(""))
        self.assertEqual((ImportString("value") + "add").value, "value.add")
        self.assertEqual((ImportString("") + "add").value, "add")
        self.assertEqual(ImportString("value"), ImportString("value"))
        self.assertEqual(ImportString("value"), "value")
        self.assertNotEqual(ImportString("value"), ImportString("value1"))
        self.assertNotEqual(ImportString("value"), "value1")
        self.assertEqual(
            ImportString("parent.parent2.value").parent.value, "parent.parent2"
        )

        with self.assertRaises(ImportStringError):
            _ = ImportString("value").parent

    def test_is_top_level(self):
        self.assertTrue(ImportString("value").is_top_level())
        self.assertTrue(ImportString("").is_top_level())
        self.assertFalse(ImportString("parent.value").is_top_level())

    def test_startswith(self):
        self.assertTrue(
            ImportString("parent.parent2.value").startswith(ImportString("parent"))
        )
        self.assertTrue(
            ImportString("parent.parent2.value").startswith(
                ImportString("parent.parent2")
            )
        )
        self.assertFalse(
            ImportString("parent.parent2.value").startswith(ImportString("parent2"))
        )
        self.assertFalse(
            ImportString("parent.parent2.value").startswith(
                ImportString("parent.parent2value")
            )
        )
