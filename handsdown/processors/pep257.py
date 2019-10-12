import re
from typing import Text, Optional

from handsdown.processors.base import BaseDocstringProcessor


class PEP257DocstringProcessor(BaseDocstringProcessor):
    """
    This class implements the preprocessor for PEP257 and Google style.
    """
    line_re_map = {
        re.compile(r'^\s*(?P<param>\S+):\s+(?P<desc>.+)$'): '- `{param}` - {desc}',
        re.compile(r'^\s*(?P<param>\S+)\s+(?P<type>\S+):\s+(?P<desc>.+)$'): '- `{param}` *{type}* - {desc}',
        re.compile(r'^\s*(?P<param>\S+)\s+\((?P<type>\S+)\):\s+(?P<desc>.+)$'): '- `{param}` *{type}* - {desc}',
        re.compile(r'^\s*(?P<param>\S+)\s+--\s+(?P<desc>.+)$'): '- `{param}` - {desc}',
        re.compile(
            r'^\s*(?P<param>\S+)\s+\{\[(?P<type>\S+)\]\}\s+--\s+(?P<desc>.+)$'): '- `{param}` *{type}* - {desc}',
        re.compile(
            r'^\s*(?P<param>\S+)\s+\{(?P<type>\S+)\}\s+--\s+(?P<desc>.+)$'): '- `{param}` *{type}* - {desc}',
    }

    def _parse_line(self, line: Text) -> Optional[Text]:
        if line.strip().startswith("```"):
            self.in_codeblock = not self.in_codeblock
            return line

        if self.in_codeblock:
            return line

        if line in self.section_name_map:
            self.current_section_name = self.section_name_map[line]
            return None

        for line_re, line_format in self.line_re_map.items():
            match = line_re.match(line)
            if not match:
                continue

            return line_format.format(**match.groupdict())

        return line
