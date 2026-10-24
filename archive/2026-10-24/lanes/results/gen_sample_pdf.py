from pathlib import Path
from fpdf import FPDF
import re
import unicodedata

md_path = Path("/workspace/fantasy/quantum-blitz/results/week-0-scorecard-SAMPLE.md")
pdf_path = Path("/workspace/fantasy/quantum-blitz/results/week-0-scorecard-SAMPLE.pdf")
text = md_path.read_text(encoding="utf-8")

replacements = {
    "\u26a0\ufe0f": "WARNING",
    "\u26a0": "WARNING",
    "\u00b7": "-",
    "\u0394": "d",
    "\u2014": "-",
    "\u2013": "-",
    "\u2212": "-",
    "\u00d7": "x",
    "\u2265": ">=",
    "\u2264": "<=",
    "\u00b1": "+/-",
    "\u2192": "->",
    "\u2190": "<-",
    "\u2026": "...",
    "\u201c": '"',
    "\u201d": '"',
    "\u2018": "'",
    "\u2019": "'",
    "\u2022": "*",
    "\ufe0f": "",
}
for k, v in replacements.items():
    text = text.replace(k, v)

def to_ascii(s: str) -> str:
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        else:
            n = unicodedata.normalize("NFKD", ch)
            ascii_part = "".join(c for c in n if ord(c) < 128)
            out.append(ascii_part if ascii_part else "?")
    return "".join(out)

text = to_ascii(text)

lines = []
for raw in text.splitlines():
    line = raw
    line = re.sub(r"^#{1,6}\s*", "", line)
    line = line.replace("**", "").replace("__", "")
    # remove leftover markdown italics asterisks carefully for table pipes
    if line.startswith("> "):
        line = line[2:]
    elif line.startswith(">"):
        line = line[1:].lstrip()
    line = line.replace("`", "")
    # strip remaining single asterisks used for italics
    line = re.sub(r"(?<!\*)\*(?!\*)", "", line)
    if re.match(r"^-{3,}$", line.strip()) or re.match(r"^={3,}$", line.strip()):
        lines.append("-" * 96)
        continue
    lines.append(line)

WRAP = 100

class ScorecardPDF(FPDF):
    def header(self):
        self.set_fill_color(255, 220, 0)
        self.set_text_color(0, 0, 0)
        self.set_font("Courier", "B", 9)
        banner = "WARNING SAMPLE ONLY -- FAKE DATA -- NOT REAL WEEK RESULTS"
        self.cell(0, 8, banner, border=0, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
        self.ln(2)

    def footer(self):
        self.set_y(-12)
        self.set_font("Courier", "", 7)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "SAMPLE / FAKE DATA", align="C")

pdf = ScorecardPDF(orientation="P", unit="mm", format="Letter")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Courier", "", 7)
pdf.set_text_color(0, 0, 0)

effective_width = pdf.w - pdf.l_margin - pdf.r_margin

for line in lines:
    if not line.strip():
        pdf.ln(3)
        continue
    while len(line) > WRAP:
        chunk = line[:WRAP]
        br = chunk.rfind(" ")
        if br < WRAP // 2:
            br = WRAP
        part = line[:br]
        line = line[br:].lstrip() if br < len(line) else ""
        pdf.multi_cell(effective_width, 3.5, part)
    pdf.multi_cell(effective_width, 3.5, line)

pdf.output(str(pdf_path))
size = pdf_path.stat().st_size
print(f"PDF written: {pdf_path}")
print(f"bytes: {size}")
print(f"pages: {pdf.page_no()}")
