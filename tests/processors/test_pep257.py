from pathlib import Path

from handsdown.processors.pep257 import PEP257DocstringProcessor


class TestLoader:
    def test_init(self):
        pep257_docstring = (
            Path(__file__).parent.parent / "static" / "pep257_docstring.txt"
        ).read_text()
        processor = PEP257DocstringProcessor()
        sections = processor.build_sections(pep257_docstring)
        assert sections.sections[""].title == ""
        assert (
            sections.sections[""].render() == "Summary line.\n\nExtended description of method.\n\n"
        )
