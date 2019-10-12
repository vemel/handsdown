import re
from typing import Text, Optional

from handsdown.processors.base import BaseDocstringProcessor


class RSTDocstringProcessor(BaseDocstringProcessor):
    """
    This class implements the preprocessor for restructured text.
    """

    line_re_map = {
        re.compile(
            r'^\s*:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$'
        ): '- `{param}` *{type}* - {desc}',
        re.compile(
            r'^\s*:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:\s*(?P<desc>.+)$'
        ): '- `{param}` - {desc}',
        re.compile(
            r'^\s*:(?P<section>param|parameter)\s+(?P<type>\w+)\s+(?P<param>\w+)\s*:$'
        ): '- `{param}` *{type}*',
        re.compile(
            r'^\s*:(?P<section>param|parameter)\s+(?P<param>\w+)\s*:$'
        ): '- `{param}`',
        re.compile(r'\s*:(?P<section>returns?)\s*:\s*(?P<desc>.*)?$'): '{desc}',
        re.compile(r'\s*:(?P<section>returns?)\s+(?P<type>[^:]+):$'): 'Type: *{type}*',
        re.compile(
            r'\s*:(?P<section>returns?)\s+(?P<type>[^:]+)\s*:\s*(?P<desc>.+)$'
        ): 'Type: *{type}*\n{desc}',
        re.compile(r'\s*:(?P<section>rtype)\s+(?P<type>[^:]+):$'): 'Type: *{type}*',
        re.compile(r':(?P<section>raises?)\s+(?P<type>\w+)\s*:$'): '- `{type}`',
        re.compile(r':(?P<section>raises?)\s+(?P<type>\w+)\s*:(?P<desc>.+)$'): '- `{type}` - {desc}',
    }

    re_section_map = {
        'raise': 'Raises',
        'raises': 'Raises',
        'rtype': 'Returns',
        'return': 'Returns',
        'returns': 'Returns',
        'param': 'Arguments',
        'parameter': 'Arguments',
    }

    def _parse_line(self, line: Text) -> Optional[Text]:
        # self.current_section_name = None

        if line.strip().startswith("```"):
            self.in_codeblock = not self.in_codeblock
            return line

        if self.in_codeblock:
            return line

        for line_re, line_format in self.line_re_map.items():
            match = line_re.match(line)
            if not match:
                continue

            match_dict = match.groupdict()

            if 'section' in match_dict:
                self.current_section_name = self.re_section_map[match_dict['section']]

            return line_format.format(**match_dict)

        return line
