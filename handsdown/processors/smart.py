from typing import Text

from handsdown.processors.rst import RSTDocstringProcessor
from handsdown.processors.pep257 import PEP257DocstringProcessor
from handsdown.processors.base import BaseDocstringProcessor
from handsdown.type_defs import SectionMap


class SmartDocstringProcessor(BaseDocstringProcessor):
    """
    This class implements the preprocessor for restructured text and google.
    """

    def __init__(self) -> None:
        self._pep257_processor = PEP257DocstringProcessor()
        self._rst_processor = RSTDocstringProcessor()
        super(SmartDocstringProcessor, self).__init__()

    def _parse_line(self, line: Text) -> Text:
        return line

    def build_sections(self, content: Text) -> SectionMap:
        """
        Preprocessors a given section into it's components.
        """
        stripped_lines = []
        for original_line in content.split("\n"):
            stripped_lines.append(original_line)

        google_keywords = self._pep257_processor.section_name_map.keys()
        for google_keyword in google_keywords:
            if google_keyword in stripped_lines:
                return self._pep257_processor.build_sections(content)

        return self._rst_processor.build_sections(content)
