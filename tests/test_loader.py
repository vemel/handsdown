from pathlib import Path

from handsdown.loader import Loader


class TestLoader:
    def test_init(self):
        loader = Loader(root_path=Path.cwd(), output_path=Path.cwd() / "docs")
        assert isinstance(loader, Loader)
