# pylint: disable=missing-docstring
import unittest

from handsdown.processors.section_map import Section, SectionBlock, SectionMap


class TestSectionBlock(unittest.TestCase):
    def test_init(self):
        block = SectionBlock(lines=["  line", " line2"])
        self.assertEqual(block.render(), " line\nline2")


class TestSection(unittest.TestCase):
    def test_init(self):
        block = SectionBlock(lines=["  line", " line2"])
        section = Section(title="title", blocks=[block])
        self.assertEqual(section.title, "title")
        self.assertEqual(section.blocks, [block])


class TestSectionMap(unittest.TestCase):
    def test_init(self):
        section_map = SectionMap()
        section_map.add_line("section", "one")
        section_map.add_line("section", "two")
        section_map.add_block("section")
        section_map.add_line("section", "three")
        section_map.add_line("section2", "")
        section_map.add_line("section2", "one")
        section_map.add_line("section2", "")
        section_map.trim_block("section2")
        section_map.add_block("section3")
        section_map.trim_block("section3")
        section_map.add_block("section4")

        self.assertEqual(section_map.sections["section"].blocks[0].lines, ["one", "two"])
        self.assertEqual(section_map.sections["section"].blocks[1].lines, ["three"])
        self.assertEqual(section_map.sections["section2"].blocks[0].lines, ["one"])
        self.assertNotIn("section3", section_map)
        self.assertNotIn("section4", section_map)

        self.assertEqual(len(list(section_map.sections)), 2)
