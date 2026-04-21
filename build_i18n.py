# -*- coding: utf-8 -*-
"""Generate i18n.js from flexa_translations.DATA (run from repo root)."""
import json
from pathlib import Path

from flexa_translations import DATA


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "i18n.js"
    with out.open("w", encoding="utf-8") as f:
        f.write("(function(){window.FLEXA_I18N=")
        json.dump(DATA, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";})();")


if __name__ == "__main__":
    main()
