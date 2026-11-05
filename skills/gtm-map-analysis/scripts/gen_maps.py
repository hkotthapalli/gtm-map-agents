#!/usr/bin/env python3
"""Kernel GTM Map Analysis generator.
Page 1: the 34-output grid. Page 2: the positioning read. Page 3 (standard): how the gaps would be closed (d["help"], mode "role" or "kernel")."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import math

GREEN = HexColor("#00FF7F")
BLACK = HexColor("#0A0A0A")
GREY = HexColor("#555555")
MGREY = HexColor("#8A8A8A")
LGREY = HexColor("#BBBBBB")
FGREY = HexColor("#E4E4E4")
BGGREY = HexColor("#F4F4F4")

W, H = A4
SITE = "https://kernelpmm.com/"  # every output name on page 1 links here
# Footer on page 3. Change to your own name and site.
AUTHOR_FOOTER = "Harsha Kotthapalli \u00b7 Kernel \u00b7 kernelpmm.com/work"
SLUGS = {
    "Voice of customer": "voice-of-customer", "Win/loss analysis": "win-loss",
    "Market report": "market-sizing", "Why now": "why-now",
    "Assumption log": "assumption-log", "Pre-mortem": "pre-mortem",
    "The Fifty": "the-fifty", "Table-stakes read": "table-stakes",
    "AI visibility": "ai-visibility", "Competitor monitor": "competitor-monitor",
    "ICP and segments": "icp-and-segments", "Use cases": "use-cases",
    "Buying committee": "buying-committee", "Positioning": "positioning",
    "Packaging and pricing": "packaging-and-pricing", "Deck spine": "deck-spine",
    "Messaging framework": "messaging-framework", "Claim check": "claim-check",
    "Landing page review": "landing-page-review", "Message drift": "message-drift",
    "Launch tiers": "launch-tiers", "Launch brief": "launch-brief",
    "Channel and funnel": "channel-and-funnel", "Product Oracle": "product-oracle",
    "Sales enablement": "sales-enablement", "FAQ": "internal-external-faq",
    "Onboarding journey": "onboarding-journey", "Release notes": "release-notes",
    "Funnel metrics": "product-funnel-metrics", "Launch post-mortem": "launch-post-mortem",
    "Trust metrics": "trust-metrics", "Case studies": "customer-case-studies",
    "Half-Life Map": "half-life-map", "Six-stage readout": "six-stage-readout",
}

# canonical 34, grouped in 6 stages
STAGE_NAMES = ["RESEARCH", "COMPETITION", "POSITION", "MESSAGE", "LAUNCH", "MEASURE"]
STAGE_ITEMS = [
    ["Voice of customer", "Win/loss analysis", "Market report", "Why now", "Assumption log", "Pre-mortem"],
    ["The Fifty", "Table-stakes read", "AI visibility", "Competitor monitor"],
    ["ICP and segments", "Use cases", "Buying committee", "Positioning", "Packaging and pricing", "Deck spine"],
    ["Messaging framework", "Claim check", "Landing page review", "Message drift"],
    ["Launch tiers", "Launch brief", "Channel and funnel", "Product Oracle", "Sales enablement", "FAQ",
     "Onboarding journey", "Release notes"],
    ["Funnel metrics", "Launch post-mortem", "Trust metrics", "Case studies", "Half-Life Map", "Six-stage readout"],
]


def glyph(c, x, y, s, kind, highlight=False):
    c.saveState()
    fill = GREEN if highlight else BLACK
    if kind == "V":
        c.setFillColor(fill)
        c.rect(x, y, s, s, stroke=0, fill=1)
    elif kind == "P":
        if highlight:
            c.setFillColor(GREEN); c.rect(x, y, s, s, stroke=0, fill=1)
        c.setStrokeColor(BLACK); c.setLineWidth(1)
        c.rect(x, y, s, s, stroke=1, fill=0)
        c.setFillColor(BLACK)
        c.rect(x, y, s, s / 2.0, stroke=0, fill=1)
    elif kind == "M":
        if highlight:
            c.setFillColor(GREEN); c.rect(x, y, s, s, stroke=0, fill=1)
        c.setStrokeColor(BLACK); c.setLineWidth(1); c.setDash(2, 2)
        c.rect(x, y, s, s, stroke=1, fill=0)
    else:  # U
        c.setFillColor(FGREY)
        c.rect(x, y, s, s, stroke=0, fill=1)
    c.restoreState()


def page1(c, d):
    counts = {"V": 0, "P": 0, "M": 0, "U": 0}
    for stage in d["stages"]:
        for k in stage:
            counts[k] += 1

    # ---- old Kernel chrome: green band header ----
    c.setFillColor(GREEN)
    c.rect(0, H - 90, W, 90, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.rect(40, H - 68, 26, 26, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(80, H - 58, "Kernel")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(80, H - 76, "GTM Map Analysis")
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 40, H - 46, "Prepared for " + d["prepared_for"])
    c.drawRightString(W - 40, H - 59, "Read from %s's public surfaces" % d["company"])
    c.drawRightString(W - 40, H - 72, d["date_long"])

    # intro
    c.setFillColor(BLACK)
    c.setFont("Helvetica", 10)
    c.drawString(40, H - 120, "A product marketing function produces 34 outputs. This is what a stranger can and cannot see of")
    c.drawString(40, H - 133, "%s's, from the outside. No judgement of the work itself: only of what is visible." % d["company"])

    # legend line (old style, Helvetica)
    ly = H - 162
    leg = [("V", "%d visible" % counts["V"]), ("P", "%d partial" % counts["P"]),
           ("M", "%d missing from public surfaces" % counts["M"]),
           ("U", "%d cannot be known from outside" % counts["U"])]
    lx = 40
    c.setFont("Helvetica", 9)
    for kind, label in leg:
        glyph(c, lx, ly, 8, kind)
        c.setFillColor(BLACK)
        c.drawString(lx + 13, ly + 0.5, label)
        lx += 13 + c.stringWidth(label, "Helvetica", 9) + 22

    # sources line (must fit one line)
    src = d["sources_line"]
    if c.stringWidth(src, "Helvetica", 7.5) > W - 80:
        raise SystemExit("sources_line overruns page width: %.1f > %.1f" % (c.stringWidth(src, "Helvetica", 7.5), W - 80))
    c.setFillColor(GREY); c.setFont("Helvetica", 7.5)
    c.drawString(40, H - 178, src)

    findings = dict(d.get("findings", []))
    allnames = [n for st in STAGE_ITEMS for n in st]
    for fname in findings:
        if fname not in allnames:
            raise SystemExit("finding on unknown output: " + fname)
    FW = 140  # max finding width in points
    def wrap_finding(text):
        words = text.split(); lines = [""]
        for w_ in words:
            t = (lines[-1] + " " + w_).strip()
            if c.stringWidth(t, "Helvetica-Oblique", 6.5) <= FW:
                lines[-1] = t
            else:
                lines.append(w_)
        if len(lines) > 2:
            raise SystemExit("finding too long (more than two lines): " + text)
        return lines

    # ---- output map display: the numbered mono grid ----
    y = H - 205
    idx = 0
    word = {"V": "VISIBLE", "P": "PARTIAL", "M": "MISSING", "U": "UNKNOWABLE"}
    for si, sname in enumerate(STAGE_NAMES):
        items = STAGE_ITEMS[si]
        kinds = d["stages"][si]
        # per-stage counts
        sc = {"V": 0, "P": 0, "M": 0, "U": 0}
        for k in kinds:
            sc[k] += 1
        c.setFillColor(BLACK)
        c.setFont("Courier-Bold", 10.5)
        c.drawString(40, y, sname)
        parts = ["%d %s" % (sc[k], word[k]) for k in ("V", "P", "M", "U") if sc[k]]
        c.setFont("Courier", 7.5)
        c.setFillColor(MGREY)
        c.drawRightString(W - 40, y, " · ".join(parts))
        c.setStrokeColor(HexColor("#DDDDDD")); c.setLineWidth(0.8)
        c.line(40, y - 5, W - 40, y - 5)
        y -= 22
        # items in 3 columns
        colx = [40, 213, 386]
        rows = math.ceil(len(items) / 3.0)
        for r in range(int(rows)):
            row_extra = 0
            for ci in range(3):
                i = r * 3 + ci
                if i >= len(items):
                    continue
                name = items[i]
                kind = kinds[i]
                num = "%02d" % (idx + i + 1)
                x0 = colx[ci]
                hi = (d.get("highlight") == name)
                glyph(c, x0, y - 1.5, 9, kind, highlight=hi and kind == "V")
                if hi and kind != "V":
                    # green underlay ring for non-solid glyphs
                    c.saveState()
                    c.setStrokeColor(GREEN); c.setLineWidth(2)
                    c.rect(x0 - 1.5, y - 3, 12, 12, stroke=1, fill=0)
                    c.restoreState()
                unknown = (kind == "U")
                c.setFont("Courier", 8)
                c.setFillColor(LGREY if unknown else MGREY)
                c.drawString(x0 + 14, y, num)
                c.setFont("Courier" if unknown else "Courier-Bold", 8)
                c.setFillColor(LGREY if unknown else BLACK)
                disp = name.upper()
                c.drawString(x0 + 30, y, disp)
                slug = SLUGS.get(name)
                if slug:
                    tw = c.stringWidth(disp, "Courier" if unknown else "Courier-Bold", 8)
                    c.linkURL(SITE + slug, (x0 + 28, y - 3, x0 + 32 + tw, y + 9), relative=0)
                if name in findings:
                    if unknown:
                        raise SystemExit("finding on unknowable output: " + name)
                    fl = wrap_finding(findings[name])
                    c.setFont("Helvetica-Oblique", 6.5); c.setFillColor(GREY)
                    fy = y - 8.5
                    for ln in fl:
                        c.drawString(x0 + 30, fy, ln); fy -= 7.5
                    row_extra = max(row_extra, 7.5 * len(fl) + 1)
            y -= 15 + row_extra
        idx += len(items)
        y -= 12

    # green start-here note directly under the grid
    if y - 4 < 62:
        raise SystemExit("page 1 grid overruns the footer: y=%.1f" % y)
    ly = y - 4
    if d.get("highlight"):
        c.saveState(); c.setStrokeColor(GREEN); c.setLineWidth(2)
        c.rect(40, ly - 1, 10, 10, stroke=1, fill=0); c.restoreState()
        c.setFillColor(BLACK)
        c.setFont("Helvetica", 8.5)
        c.drawString(56, ly, "marks where the positioning read on page 2 starts.")

    c.setFillColor(GREY)
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(40, ly - 18, "Every output name above is a link: click it to see what that output is and why it matters, on kernelpmm.com.")

    # old-style footer
    c.setFillColor(HexColor("#999999"))
    c.setFont("Helvetica", 8)
    c.drawString(40, 30, "Kernel · fractional product marketing · kernelpmm.com")
    c.drawRightString(W - 40, 30, "Page 1 of %d" % d.get("_pages", 2))
    c.linkURL(SITE + "gtm-map", (40, 26, 300, 40), relative=0)
    c.showPage()


NUMWORD = {12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen"}


def wrap(c, text, font, size, width):
    words = text.split(); lines = [""]
    for w_ in words:
        t = (lines[-1] + " " + w_).strip()
        if c.stringWidth(t, font, size) <= width:
            lines[-1] = t
        else:
            lines.append(w_)
    return lines


VERDICTS = {
    # verdict: (fill colour, text colour)
    "Clear": (BLACK, HexColor("#FFFFFF")),
    "Generic": (FGREY, BLACK),
    "Split": (GREEN, BLACK),
    "Missing": (HexColor("#FFFFFF"), BLACK),
    "Behind": (FGREY, BLACK),
}


def page2(c, d):
    """Page 2: the positioning read.

    d["read"] = dict(
        thesis="one-sentence headline: the positioning problem, stated as fact",
        thesis_body="2-3 sentences: why it matters at this stage",
        rows=[(component, what_the_company_says, what_rivals_say, verdict), ...],  # 5 rows
        frame=[(rival, the ground it holds), ...],   # 4-6 rivals
        open_position="the slot no rival holds, one or two sentences",
        options=[(label, one or two sentences), ...],  # 2-3 positioning options
        decides="what evidence would decide between the options",
    )
    """
    r = d.get("read")
    if not r:
        raise SystemExit("missing field: read (the positioning read)")
    for k in ("thesis", "thesis_body", "rows", "frame", "open_position", "options", "decides"):
        if not r.get(k):
            raise SystemExit("missing read field: " + k)
    for k in ("cannot", "book_url", "method_footer"):
        if not d.get(k):
            raise SystemExit("missing field: " + k)
    if not 4 <= len(r["rows"]) <= 6:
        raise SystemExit("read rows must be 4-6")
    if not 3 <= len(r["frame"]) <= 6:
        raise SystemExit("frame must name 3-6 rivals")
    if not 2 <= len(r["options"]) <= 3:
        raise SystemExit("options must be 2-3")

    c.setFillColor(GREEN)
    c.rect(0, H - 62, W, 62, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.rect(40, H - 43, 18, 18, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(70, H - 39, "The positioning read")
    c.setFont("Helvetica", 8.5)
    c.drawRightString(W - 40, H - 39, "What %s says it is, next to what its rivals say" % d["company"])

    TW = W - 80
    y = H - 88
    c.setFillColor(BLACK)
    for ln in wrap(c, r["thesis"], "Helvetica-Bold", 11.5, TW):
        c.setFont("Helvetica-Bold", 11.5); c.drawString(40, y, ln); y -= 14
    y -= 2
    c.setFont("Helvetica", 8.8)
    for ln in wrap(c, r["thesis_body"], "Helvetica", 8.8, TW):
        c.drawString(40, y, ln); y -= 11.3
    y -= 8

    # component table
    cols = [40, 108, 278, 448]  # component | company says | rivals say | verdict
    widths = [64, 164, 164, W - 40 - 448]
    c.setFont("Courier-Bold", 7); c.setFillColor(GREY)
    for x, h in zip(cols, ["COMPONENT", "WHAT %s SAYS" % d["company"].upper(), "WHAT RIVALS SAY", "VERDICT"]):
        c.drawString(x, y, h)
    y -= 5
    c.setStrokeColor(BLACK); c.setLineWidth(0.8); c.line(40, y, W - 40, y)
    y -= 10
    for comp, says, rivals, verdict in r["rows"]:
        if verdict not in VERDICTS:
            raise SystemExit("verdict must be one of %s, got %s" % (list(VERDICTS), verdict))
        a = wrap(c, says, "Helvetica", 7.6, widths[1])
        b = wrap(c, rivals, "Helvetica", 7.6, widths[2])
        n = max(len(a), len(b), 1)
        if n > 5:
            raise SystemExit("table cell too long (more than five lines): " + comp)
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 8)
        for i, ln in enumerate(wrap(c, comp, "Helvetica-Bold", 8, widths[0])):
            c.drawString(cols[0], y - 9.5 * i, ln)
        c.setFont("Helvetica", 7.6)
        for i, ln in enumerate(a):
            c.drawString(cols[1], y - 9.5 * i, ln)
        for i, ln in enumerate(b):
            c.drawString(cols[2], y - 9.5 * i, ln)
        fill, txt = VERDICTS[verdict]
        c.setFillColor(fill); c.setStrokeColor(BLACK); c.setLineWidth(0.6)
        if verdict == "Missing":
            c.setDash(2, 1.5)
        c.rect(cols[3], y - 3, 54, 12, stroke=1, fill=1)
        c.setDash()
        c.setFillColor(txt); c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(cols[3] + 27, y, verdict)
        y -= 9.5 * n + 4
        c.setStrokeColor(FGREY); c.setLineWidth(0.6); c.line(40, y + 3, W - 40, y + 3)
        y -= 6
    c.setFillColor(GREY); c.setFont("Helvetica-Oblique", 6.8)
    c.drawString(40, y + 1, "Clear: one specific claim, stated the same way everywhere. Generic: a rival could sign it unchanged. "
                 "Split: surfaces disagree. Behind: rivals show more. Missing: not stated.")
    y -= 16

    # competitive frame
    c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 10.5)
    c.drawString(40, y, "The ground each rival holds")
    y -= 13
    for name, ground in r["frame"]:
        lines = wrap(c, ground, "Helvetica", 8, TW - 90)
        if len(lines) > 2:
            raise SystemExit("frame line too long: " + name)
        c.setFont("Helvetica-Bold", 8); c.drawString(40, y, name)
        c.setFont("Helvetica", 8)
        for ln in lines:
            c.drawString(130, y, ln); y -= 10
        y -= 1.5
    y -= 3
    c.setFont("Helvetica-Bold", 8.5); c.drawString(40, y, "Open ground:")
    ol = wrap(c, r["open_position"], "Helvetica", 8.5, TW - 90)
    c.setFont("Helvetica", 8.5)
    for ln in ol:
        c.drawString(130, y, ln); y -= 11
    y -= 10

    # decision box
    inner = W - 150
    body = []
    for label, text in r["options"]:
        body.append(("opt", label, wrap(c, text, "Helvetica", 8.5, inner - 72)))
    dec = wrap(c, r["decides"], "Helvetica-Oblique", 8.3, inner)
    bh = 26 + sum(11 * len(t) + 3 for _, _, t in body) + 6 + 10.5 * len(dec) + 6
    c.setFillColor(GREEN); c.rect(55, y - bh, W - 110, bh, stroke=0, fill=1)
    c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 10)
    c.drawString(70, y - 15, "The positioning choice to settle first")
    yy = y - 30
    for _, label, t in body:
        c.setFont("Helvetica-Bold", 8.5); c.drawString(70, yy, label)
        c.setFont("Helvetica", 8.5)
        for ln in t:
            c.drawString(142, yy, ln); yy -= 11
        yy -= 3
    yy -= 3
    c.setFont("Helvetica-Oblique", 8.3)
    for ln in dec:
        c.drawString(70, yy, ln); yy -= 10.5
    y = y - bh - 16

    c.setFillColor(BLACK); c.setFont("Helvetica", 8.3)
    for ln in wrap(c, " ".join(d["cannot"]) if isinstance(d["cannot"], list) else d["cannot"], "Helvetica", 8.3, TW):
        c.drawString(40, y, ln); y -= 10.5
    y -= 8

    c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 8.5)
    c.drawString(40, y, "Page 3: how these gaps would be closed.")
    y -= 14
    if y < 44:
        raise SystemExit("page 2 overruns the footer: y=%.1f (shorten the read)" % y)

    c.setFillColor(HexColor("#999999"))
    if c.stringWidth(d["method_footer"], "Helvetica", 7.5) > W - 130:
        raise SystemExit("method_footer overruns: %.1f" % c.stringWidth(d["method_footer"], "Helvetica", 7.5))
    c.setFont("Helvetica", 7.5)
    c.drawString(40, 30, d["method_footer"])
    c.linkURL(SITE + "gtm-map", (40, 26, 40 + c.stringWidth(d["method_footer"], "Helvetica", 7.5), 38), relative=0)
    c.setFont("Helvetica", 8)
    c.drawRightString(W - 40, 30, "Page 2 of %d" % d.get("_pages", 2))


HELP_MODES = {
    # mode: (title, left column header)
    "role": ("How I would close these gaps from inside %s", "WHAT I WOULD DO IN THE FIRST 90 DAYS"),
    "kernel": ("How Kernel would close these gaps with %s", "WHAT KERNEL WOULD DO FIRST"),
}


def page3(c, d):
    """Page 3 (standard): how the gaps on page 2 would be closed.

    d["help"] = dict(
        mode="role" (full-time role approach) or "kernel" (Kernel prospect),
        intro="2-3 sentences",
        rows=[(issue from the positioning read, what would be done, where it was done before), ...],  # 3 rows
        about_title="closing box title", about="closing box text",
        linkedin="https://www.linkedin.com/in/your-profile/",  # shown in role mode
    )
    """
    h = d.get("help")
    if not h:
        raise SystemExit("missing field: help (page 3 is standard)")
    for k in ("mode", "intro", "rows", "about_title", "about"):
        if not h.get(k):
            raise SystemExit("missing help field: " + k)
    if h["mode"] not in HELP_MODES:
        raise SystemExit("help mode must be 'role' or 'kernel'")
    if len(h["rows"]) != 3:
        raise SystemExit("help needs exactly 3 rows")
    title_fmt, left_head = HELP_MODES[h["mode"]]
    h = dict(h, title=title_fmt % d["company"])
    c.setFillColor(GREEN)
    c.rect(0, H - 62, W, 62, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.rect(40, H - 43, 18, 18, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(70, H - 39, h["title"])
    TW = W - 80
    y = H - 90
    c.setFont("Helvetica", 9.5)
    for ln in wrap(c, h["intro"], "Helvetica", 9.5, TW):
        c.drawString(40, y, ln); y -= 13
    y -= 10
    colw = (TW - 20) / 2.0
    for i, (gap, plan, proof) in enumerate(h["rows"], 1):
        if c.stringWidth(gap, "Helvetica-Bold", 11) > TW:
            raise SystemExit("help row title overruns: " + gap)
        c.setStrokeColor(FGREY); c.setLineWidth(0.8); c.line(40, y + 4, W - 40, y + 4)
        y -= 12
        c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 11)
        c.drawString(40, y, "%d \u00b7 %s" % (i, gap))
        y -= 15
        c.setFont("Courier-Bold", 7.5); c.setFillColor(GREY)
        c.drawString(40, y, left_head)
        c.drawString(40 + colw + 20, y, "WHERE I HAVE DONE IT BEFORE")
        y -= 12
        c.setFillColor(BLACK); c.setFont("Helvetica", 8.8)
        a = wrap(c, plan, "Helvetica", 8.8, colw)
        b = wrap(c, proof, "Helvetica", 8.8, colw)
        for k in range(max(len(a), len(b))):
            if k < len(a): c.drawString(40, y, a[k])
            if k < len(b): c.drawString(40 + colw + 20, y, b[k])
            y -= 11.5
        y -= 12
    # about box
    y -= 2
    bl = wrap(c, h["about"], "Helvetica", 9, W - 150)
    bh = 30 + 12 * len(bl) + 14
    c.setFillColor(GREEN); c.rect(55, y - bh, W - 110, bh, stroke=0, fill=1)
    c.setFillColor(BLACK); c.setFont("Helvetica-Bold", 10)
    c.drawString(75, y - 17, h["about_title"])
    c.setFont("Helvetica", 9)
    yy = y - 32
    for ln in bl:
        c.drawString(75, yy, ln); yy -= 12
    url = d["book_url"]; disp = url.replace("https://", "")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(75, yy, disp)
    c.linkURL(url, (73, yy - 3, 77 + c.stringWidth(disp, "Helvetica-Bold", 9), yy + 10), relative=0)
    li = h.get("linkedin") if h["mode"] == "role" else None
    if li:
        ldisp = li.replace("https://www.", "")
        x2 = 75 + c.stringWidth(disp, "Helvetica-Bold", 9) + 18
        c.drawString(x2, yy, ldisp)
        c.linkURL(li, (x2 - 2, yy - 3, x2 + 2 + c.stringWidth(ldisp, "Helvetica-Bold", 9), yy + 10), relative=0)
    y = y - bh - 10
    if y < 48:
        raise SystemExit("page 3 overruns the footer: y=%.1f" % y)
    c.setFillColor(HexColor("#999999")); c.setFont("Helvetica", 7.5)
    c.drawString(40, 30, AUTHOR_FOOTER)
    c.setFont("Helvetica", 8)
    c.drawRightString(W - 40, 30, "Page 3 of %d" % d.get("_pages", 2))
    c.showPage()


def build(d):
    n = sum(len(st) for st in d["stages"])
    if n != 34 or [len(st) for st in d["stages"]] != [len(st) for st in STAGE_ITEMS]:
        raise SystemExit("verdicts must be 34 in canonical shape, got %d" % n)
    if d.get("highlight") not in [x for st in STAGE_ITEMS for x in st]:
        raise SystemExit("highlight must name an output")
    for blob in [str(v) for v in d.values()]:
        if "\u2014" in blob:
            raise SystemExit("em dash found in prospect-facing text")
    d["_pages"] = 3
    c = canvas.Canvas(d["out"], pagesize=A4)
    page1(c, d)
    page2(c, d)
    c.showPage()
    page3(c, d)
    c.save()
    print("saved", d["out"])


if __name__ == "__main__":
    # Only the current company; older sent reports stay as they were.
    import sys
    import company_data
    name = sys.argv[1]
    build(getattr(company_data, name.upper()))
