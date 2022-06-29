from handsdown.processors.section_map import Section, SectionBlock, SectionMap


class TestSectionBlock:
    def test_init(self):
        block = SectionBlock(lines=["  line", " line2"])
        assert block.render() == " line\nline2"


class TestSection:
    def test_init(self):
        block = SectionBlock(lines=["  line", " line2"])
        section = Section(title="title", blocks=[block])
        assert section.title == "title"
        assert section.blocks == [block]


class TestSectionMap:
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

        assert section_map.sections["section"].blocks[0].lines == ["one", "two"]
        assert section_map.sections["section"].blocks[1].lines == ["three"]
        assert section_map.sections["section2"].blocks[0].lines == ["one"]
        assert "section3" not in section_map
        assert "section4" not in section_map

        assert len(list(section_map.sections)) == 2
