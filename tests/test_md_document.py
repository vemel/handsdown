from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from handsdown.md_document import MDDocument


class TestMDDocument:
    def test_init(self):
        with NamedTemporaryFile(mode="w+") as temp_f:
            temp_f.write(
                "\n".join(
                    [
                        "# my title",
                        "",
                        "subtitle",
                        "",
                        "",
                        "",
                        "subtitle2",
                        "",
                        "- [TOC](#toc)",
                        "- [TOC2](#toc2)",
                        "",
                        "## my title 2",
                        "",
                        "some content",
                        "new line",
                    ]
                )
            )
            temp_f.flush()
            md_doc = MDDocument(Path(temp_f.name))
            md_doc.read(Path(temp_f.name))

        assert md_doc.path == Path(temp_f.name)
        assert md_doc.title == "my title"
        assert md_doc.subtitle == "subtitle\n\nsubtitle2"
        assert md_doc.toc_section == "- [TOC](#toc)\n- [TOC2](#toc2)"
        assert md_doc.sections[0] == "## my title 2"
        assert md_doc.sections[1] == "some content\nnew line"

        md_doc.subtitle = "my subtitle"
        assert md_doc.subtitle == "my subtitle"

        with NamedTemporaryFile(mode="w+") as temp_f:
            temp_f.write(
                "\n".join(
                    [
                        "# my title",
                        "",
                        "- [TOC](#toc)",
                        "- [TOC2](#toc2)",
                        "",
                        "",
                        "some content",
                    ]
                )
            )
            temp_f.flush()
            md_doc = MDDocument(Path(temp_f.name))
            md_doc.read(Path(temp_f.name))

        assert md_doc.subtitle == "some content"

    def test_context_manager(self):
        with NamedTemporaryFile(mode="w+") as temp_f:
            with MDDocument(Path(temp_f.name)) as md_doc:
                md_doc.title = "test"

            assert temp_f.read() == "# test\n"

        with pytest.raises(ValueError):
            with MDDocument(Path(temp_f.name)):
                raise ValueError("test")

    def test_append(self):
        md_doc = MDDocument(Path("/test.md"))
        md_doc.append("subtitle")
        md_doc.append("test")
        md_doc.append("")
        assert md_doc.subtitle == "subtitle"
        assert md_doc.sections[0] == "test"

    def test_get_anchor(self):
        assert MDDocument.get_anchor("s T_e-s%t") == "s-t_e-st"
        assert MDDocument.get_anchor("test") == "test"

    def test_render_doc_link(self):
        md_doc = MDDocument(Path("/root/test.md"))
        assert md_doc.render_doc_link("title", anchor="tag") == "[title](#tag)"
        assert (
            md_doc.render_doc_link("title", anchor="tag", target_path=Path("/root/test.md"))
            == "[title](#tag)"
        )
        assert (
            md_doc.render_doc_link("title", anchor="tag", target_path=Path("/root/test2.md"))
            == "[title](./test2.md#tag)"
        )
        assert md_doc.render_doc_link("title", target_path=Path("/root/test.md")) == "[title]()"
        assert (
            md_doc.render_doc_link("title", target_path=Path("/root/test2.md"))
            == "[title](./test2.md)"
        )
        assert md_doc.render_doc_link("title") == "[title]()"

    def test_render_link(self):
        assert MDDocument.render_link("title", link="#tag") == "[title](#tag)"
        assert MDDocument.render_link("title", link="") == "[title]()"

    def test_is_toc(self):
        assert MDDocument.is_toc("- [TOC](#toc)\n- [TOC2](#toc2)")
        assert not MDDocument.is_toc("- [TOC](#toc)\n- [TOC2](#toc2)\nTOC3")
        assert not MDDocument.is_toc("- [TOC](#toc)\n")
