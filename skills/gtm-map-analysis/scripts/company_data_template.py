# Template: copy this block per company into company_data.py, replace values,
# then run: python3 gen_maps.py COMPANYNAME
# stages: 6 lists of verdicts (V/P/M/U) in canonical order per gen_maps.STAGE_ITEMS. All 34 must be assigned.
# highlight = the output where the positioning read's thesis lives (green ring), usually "Positioning".
# read.rows verdicts: Clear, Generic, Split, Behind, Missing. Every cell is quote-led and re-checkable.
# help = page 3, standard on every map. mode "kernel" for Kernel prospects, "role" for full-time role approaches.
# Rows: the issues from the positioning read, what would be done, and where it was done before (real proof points only).
# No em dashes anywhere (the generator stops on one).

COMPANYNAME = dict(
    out="out/Company_GTM_Map.pdf",
    company="Company", domain="company.com", date="13 Oct 2026", date_long="13 October 2026",
    prepared_for="First Last, Company",
    sources_line="Read company.com (EN and AR) · rival homepages · raw HTML · careers · press · LinkedIn · app stores · ChatGPT",
    stages=[
        ["U", "U", "M", "M", "U", "U"],
        ["U", "M", "M", "U"],
        ["P", "P", "M", "P", "V", "U"],
        ["P", "M", "P", "M"],
        ["U", "U", "P", "U", "U", "P", "P", "M"],
        ["U", "U", "P", "M", "U", "U"],
    ],
    highlight="Positioning",
    findings=[
        ("Positioning", "One plain-fact sentence, two short lines at most."),
    ],
    read=dict(
        thesis="One or two sentences naming the positioning problem as a fact.",
        thesis_body="Two or three sentences on why it matters at this stage.",
        rows=[
            ("Category", "What the company calls itself (quotes).", "What rivals call themselves (quotes).", "Split"),
            ("Who it is for", "...", "...", "Generic"),
            ("Where", "...", "...", "Split"),
            ("Why choose it", "...", "...", "Generic"),
            ("Proof", "...", "...", "Behind"),
        ],
        frame=[
            ("Rival A", "The ground it holds, with a short quote."),
            ("Rival B", "..."),
            ("Rival C", "..."),
            ("Rival D", "..."),
        ],
        open_position="The position no listed rival holds, and the nearest rival to it.",
        options=[
            ("A. Label", "What they would lead with, whose ground it is, the trade-off."),
            ("B. Label", "..."),
        ],
        decides="What cannot be read from outside that would decide it, and the cheapest way to get it.",
    ),
    help=dict(
        mode="kernel",
        intro=("The map shows what a stranger sees. This page is the other half: what I would do about it with Kernel, "
               "starting from the positioning read on page 2."),
        rows=[
            ("Issue 1 from the positioning read", "What Kernel would do first.", "Where you have done it before (real proof points only)."),
            ("Issue 2", "...", "..."),
            ("Issue 3", "...", "..."),
        ],
        about_title="If this is useful",
        about=("This is how I work: I read what is public, say what I find, and write it in plain language. "
               "More of the method at kernelpmm.com. If you want to talk any of it through, book a call:"),
    ),
    cannot="Fifteen of the 34 outputs are internal by nature: win/loss, the assumption log, launch process, sales enablement, funnel metrics and the rest. Whether they exist at Company is a conversation, not a crawl.",
    book_url="https://your-booking-link",
    method_footer="Read 13 Oct 2026: Company's site (EN and AR), rival homepages, press, LinkedIn, ChatGPT · Method: kernelpmm.com/gtm-map",
)
