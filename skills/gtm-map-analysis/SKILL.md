---
name: "gtm-map-analysis"
description: "Run Kernel's GTM Map Analysis on a target company - read their public surfaces, mark each of the 34 product marketing outputs as visible, partial, missing, or unknowable, read their positioning against the rivals a buyer would compare them with, and produce the branded three-page PDF (the map, the positioning read, how the gaps would be closed) plus outreach messages. Use when the user says \"run the GTM map\", \"map check\", names a new target company for outreach, or wants the free analysis artifact for a prospect."
---

# GTM Map Analysis

Kernel's outreach artifact and diagnostic, built only from public surfaces. Page 1 maps what a stranger can and cannot see of a company's product marketing. Page 2 is the positioning read: what the company says it is, next to what its rivals say, and the positioning choice that follows. Page 3 says how those gaps would be closed and where you have done it before. The prospect must be able to re-run the check themselves at kernelpmm.com/gtm-map and get the same result.

The map shows coverage. The positioning read is the part a founder or CMO cares about, so it carries the argument. Copy slips (a stale blog, a wrong count, a missing country name) are evidence inside the read, never its headlines: on their own they read as a content person's checklist, not a product marketer's judgement.

## The frame

A product marketing function produces 34 outputs across 6 stages. Each gets one verdict:

- **Visible (V)** - the output exists and works on public surfaces. Solid black square.
- **Partial (P)** - a real but incomplete version of the output is on the public surfaces. Square with bottom half filled.
- **Missing (M)** - the surfaces were read and the output is not there. Dashed outline square.
- **Unknowable (U)** - internal by nature; cannot be judged from outside. Light grey square, greyed text. Never guess these; saying "cannot be known from outside" honestly is part of the map's credibility.

### The bar for Partial

Partial is the verdict most easily given too freely, so it has a bar: **a real but incomplete version of the output, not a trace of it.** Both of these must be true:

1. You can point to the thing itself: a page, section, table or document that does part of this output's job, and you can quote it.
2. You can say what a complete version would also have, and that part is absent from the surfaces read.

Write both halves as one line for every Partial, even when that line does not appear in the PDF. If you cannot write both halves, the verdict is Missing.

These are traces, not partials:

- One stray fact. A single market figure in a press release is not a Market report.
- A by-product of a different output. Pricing tiers by balance are Packaging and pricing, not ICP and segments.

When the evidence is thin and the choice is between Partial and Missing, mark Missing and say what was looked for. Never mark Partial to soften a map.

The 34 outputs, in canonical order (each links to its kernelpmm.com page - slugs in `scripts/gen_maps.py` SLUGS dict):

1. RESEARCH: Voice of customer, Win/loss analysis, Market report, Why now, Assumption log, Pre-mortem
2. COMPETITION: The Fifty, Table-stakes read, AI visibility, Competitor monitor
3. POSITION: ICP and segments, Use cases, Buying committee, Positioning, Packaging and pricing, Deck spine
4. MESSAGE: Messaging framework, Claim check, Landing page review, Message drift
5. LAUNCH: Launch tiers, Launch brief, Channel and funnel, Product Oracle, Sales enablement, FAQ, Onboarding journey, Release notes
6. MEASURE: Funnel metrics, Launch post-mortem, Trust metrics, Case studies, Half-Life Map, Six-stage readout

Typical shape: 2-5 V, 9-13 P, 4-6 M, 14-16 U. All 34 verdicts must sum to 34. The shape is a sanity check, never a target: do not move a verdict to fit it.

If a check was not run (for example the AI-engine ask), say so in the "cannot be known" line and in the summary to the user. Do not mark that output Missing or Partial from a check that did not happen.

## The check (Quick Map - every outreach artifact)

Read `references/public-sources-checklist.md` for the full source list. Minimum run:

1. The complete website, rendered as a human sees it: every page reachable from the navigation and sitemap (pricing, product pages, about, careers, blog, legal), not just the homepage. For JS-rendered sites (Next.js/React SPAs), a plain fetch under-reads the page - use a real browser (Playwright or Chrome automation) for the rendered read, and `curl` with a standard user-agent string for the raw-HTML read below. Screenshot each page while there; it makes later fact-checks fast. In the cloud sandbox, Playwright needs `executablePath: '/opt/pw-browsers/chromium-<version>/chrome-linux/chrome'` when its bundled browser version differs.
2. Raw HTML vs rendered comparison (what crawlers/AI read) - fetch without JavaScript and diff against what the browser shows
3. Funding press (drift between investor narrative and site)
4. LinkedIn company page and live job listings (strategy leaks, PMM gap confirmation)
5. One AI-engine ask ("what is [company]?" and one buyer question). Default to an anonymous/incognito ask. Using the user's own logged-in AI assistant session (via browser automation) is only allowed with explicit per-target permission asked in the moment - never assume a blanket yes from an earlier target carries forward to the next one.
6. App store listings if an app exists (rating, review themes, release notes), plus the review surfaces that apply to the company: Trustpilot, Reddit, Product Hunt, G2/Capterra for B2B SaaS, and any industry- or vertical-specific review site
7. Click every internal link (broken surfaces are quick-fix gold)
8. Comparison/review SERP ("[company] vs [rival]", "best [category] in [market]")
9. Language parity: GCC targets get the Arabic surface check; EU and other targets get the same check in each market's local language
10. The rival scan (feeds the positioning read; see below). Pick 4 to 6 rivals the buyer would actually compare: the names in the AI-engine answers, the "best [category] in [market]" lists, the comparison searches, the funding press, and the local players a buyer in that market meets first. Render each rival's market-facing homepage (and pricing, if quick) and record, with a direct quote and URL: hero and subhead, who it says it is for, the category word it uses, the main reason-to-choose it claims, the proof it shows, and the local cues it uses (country, currency, local payment methods, licences). Save the captures with the company's screenshots. Read the company's own pricing and support pages against its homepage claims: a support-hours or fee line that contradicts the hero is often the strongest Split.

## Verification rules (non-negotiable)

- **A verdict only lands on evidence you can quote.** No inference upgrades.
- **Reproducibility standard:** every glyph and gap must survive the prospect re-running the check. No absolutes ("anywhere", "never") unless every relevant page was read - otherwise write "on the pages I read". Third-party claims (affiliate names, review scores, SERP results) come from a live search the same week, never from memory.
- **False-positive traps:** carousel duplication in raw HTML is not visible duplication; JS-rendered UI (language switchers, counters, pricing toggles) is invisible to fetchers - never claim a surface is missing from a raw fetch alone; raw-vs-rendered differences are findings about crawlers and AI engines, never about what a human visitor sees.
- **Any link placed in the PDF (the book-a-call link, kernelpmm.com) must be a real, verified URL** - scrape it from the live site that turn, never reuse a remembered or guessed one.
- **Rival quotes follow the same standard as the company's.** Every rival line in the read is a quote from a page rendered this run, or labelled "(fetched, not rendered)" when only a text fetch worked, or labelled as second-hand. A rival you could not read at all does not go in the frame.
- **The sources line and footer state only what was actually run**, and must fit the page width - check with `stringWidth()` before finalizing; shorten the source list rather than letting it wrap or overrun.

## Language rules

Direct, simple sentences. Say what is there, what is missing, what it costs. The thesis and every verdict are plain statements of fact ("The site shows no numbers"), never slogans, parallel constructions, metaphors, or rhetorical questions. If a line sounds like a LinkedIn post, rewrite it as a fact. Always mention Kernel in messages.

### Anti-slop pass (required on every map and message)

Run the `anti-ai-slop` standard on all prospect-facing copy before generating: the company data block (thesis, rows, findings, rival lines, options, page 3 rows, closing box), the sources line, the footer and the outreach messages. At minimum:

1. **Zero banned marks.** No semicolons, em dashes, vertical bars, arrows or dot separators. Write sources lines and footers as comma lists: "Read company.com (EN, ES), pricing, case studies, raw HTML, Perk, Navan and press". Grep the data block for these marks before running the generator and confirm zero.
2. **No metaphor labels.** Never use "ground", "open ground", "slot", "territory", "white space" or similar for positioning. Say what the rival leads with and what no rival claims.
3. **Rival lines are sentences, not staged fragments.** Write "Sells travel and expenses in one automated platform: "quote"", never "Automation plus spend: "quote"".
4. **Active voice, no "It's not X, it's Y", no slogan triads, no framing labels** ("Bottom line:", "Key idea:", "Cheapest route:"). The "what decides it" line names the facts that decide and how to get them, as a sentence.
5. **Findings are full sentences.** Two short sentences are fine. A semicolon joining them is not.

## The positioning read (page 2)

A positioning read judges the company the way a buyer meets it: next to its alternatives. It uses the components every serious positioning method shares (April Dunford's competitive alternatives, unique attributes, value, best-fit customer and market category; Fletch's what it is, who it is for, why it is better), read from the outside and checked against the rivals' own words.

**The five components.** One row each, in this order:

1. **Category**: what the company calls itself, on the homepage, the page title and in the funding press.
2. **Who it is for**: the customer the pages name, from hero to pricing plans.
3. **Where**: the markets it says it serves, and whether each market's pages speak to that market.
4. **Why choose it**: the reasons-to-choose on the homepage.
5. **Proof**: the numbers, licences, logos and stories that stand behind the claims.

For each row write two cells, both quote-led: what the company says (across its own surfaces, including the funding press when it says something different) and what the rivals say on the same component. Then one verdict:

- **Clear**: one specific claim, stated the same way on every surface, that the rivals do not make.
- **Generic**: a rival could sign it unchanged. Run the swap test: put a rival's name in place of the company's; if the line is still true on that rival's own homepage (quote it), it is Generic.
- **Split**: the company's surfaces disagree (homepage vs press, homepage vs pricing, English vs Arabic, one market site vs another).
- **Behind**: the rivals show more on this component than the company does (for example, they put their licence or review count in the hero and the company does not show it).
- **Missing**: the component is not stated on the surfaces read.

Never give Clear to soften a read; if no row is Clear, say so.

**The verdict legend (required).** Page 2 always carries a legend titled "What the verdicts mean", drawn directly under the table: each of the five verdict chips, in the same colours as the table, next to one plain sentence that uses the company's name:

- Clear: [Company] makes one specific claim, says it the same way on every page, and no rival makes it.
- Generic: A rival makes the same claim on its own homepage.
- Split: [Company]'s own pages say different things.
- Behind: Rivals show more on this than [Company] does.
- Missing: The pages read do not say it.

A one-line italic key is not enough; a founder must be able to read the verdicts without asking.

**The thesis.** One or two sentences at the top of the page that name the positioning problem as a fact, built from the verdicts. The strongest theses come from a Split between what the company tells investors and what it tells buyers, or from Generic reasons-to-choose next to a claim no rival makes. Then two or three sentences on why it matters at this stage. A copy slip can be the evidence, never the thesis.

**What each rival leads with.** One line per rival (4 to 5 on the page): what the rival sells and leads with, as a sentence, with a short quote. Then **No rival claims**: the claim none of the listed rivals makes, stated as an observation from the quotes, and the rival that comes closest to it.

**The positioning choice to settle first.** Two or three options, each a short label (one or two words, so it fits the label column) and one or two sentences: what the company would lead with, which rival already leads with it, and the trade-off. Do not pick for them and do not rewrite their homepage: the free read frames the choice; a paid engagement makes it. End the box with **what decides it**, as a sentence: the facts that cannot be read from outside (why customers chose them over the named rivals, win/loss, usage of the feature the story rests on) and how to get them, usually a round of customer interviews. This is the line that separates Kernel's read from a homepage teardown that never talks to a customer.

**What the read is not.** Not a copy review, not a homepage rewrite, not a score. It does not judge the team's work; it reports what the surfaces say next to what the market says.

**Page 1 link.** The green ring on page 1 sits on the output where the read's thesis lives, usually Positioning, sometimes Message drift or ICP and segments.

## The deliverable (three A4 pages: the map, the read, how the gaps would be closed)

Built with `gen_maps.py` + a data block per company (see `company_data_template.py`).

**Which generator to use:** this skill's `scripts/gen_maps.py` is the current generator. It draws everything in this section (in-grid findings, sources line, the positioning read, page 3 and its closing box) and stops with an error when a line would overrun the page, a field is missing or a verdict is not one of the five. Copy the scripts to a work folder for each company and generate there. Never edit the bundled files in place, and never loosen a check to make one map fit: shorten the text instead.

**Patching an older generator copy.** If the copied `gen_maps.py` still draws the old one-line italic verdict key ("Clear: one specific claim, stated the same way everywhere. Generic: ...") or the headings "The ground each rival holds" and "Open ground:", patch the work copy before generating:

1. Replace the italic key block in `page2()` with the five-row legend above: for each verdict, draw its chip (46 x 10.5 pt, same fill and dashed border for Missing as the table) at x=40 and the sentence in Helvetica 7.6 at x=94, 12.5 pt per row, under a bold "What the verdicts mean" label, then leave 8 pt before the next section.
2. Change the heading "The ground each rival holds" to "What each rival leads with".
3. Change the label "Open ground:" to "No rival claims:".

Check page 2 still fits (the generator stops if it overruns the footer); shorten the read rather than the legend.

**Page 1:** Kernel green header band, intro sentence, glyph legend with counts, then the output map as a numbered mono grid (01-34, three columns, per-stage counts on each rule, unknowables greyed, every output name a live link to kernelpmm.com, one green-ringed glyph marking where the positioning read's thesis lives).

**In-grid findings (standard practice now):** add a `findings` list of `(output name, one-sentence finding)` tuples to the company data block. Each finding renders in small grey italic text directly beneath its output's name in the grid (not as a separate strip) - one or two short plain-fact sentences, no explanation clause, no semicolons, tight enough to fit the column width (the current generator wraps a finding to at most two short lines and stops if it is longer). Rows that contain an annotated output get a little extra vertical space so the finding doesn't crowd the next row. Use findings to cover the outputs that most inform the read, not necessarily all 34 - ICP/segments, use cases, positioning, packaging/pricing, messaging framework, channel/funnel, FAQ, AI visibility, market report, message drift, funnel metrics, trust metrics, landing page review, onboarding journey, and claim check are the outputs that have carried findings so far. A finding never sits on an unknowable output.

**Page 2: the positioning read** (see the section above). Green header band "The positioning read", the thesis in bold, the five-component table (component, what the company says, what rivals say, verdict chip), the verdict legend "What the verdicts mean", "What each rival leads with" with "No rival claims", a green box "The positioning choice to settle first" with the options and what decides it, one line on what cannot be known from outside (the U count, named honestly, plus any check that was not run), and a pointer to page 3.

The old page 2 ("three gaps" and "Quick fix, this week") is retired. A quick fix can still go in the message or the conversation when it is worth it, but it never leads.

**Page 3 (standard on every map): how these gaps would be closed.** Set `help` in the data block with a `mode`:

- `mode="kernel"` for Kernel prospects (the default). Title: "How Kernel would close these gaps with [Company]". Left column: what Kernel would do first.
- `mode="role"` when you are approaching the company for a full-time role, including interview prep. Title: "How I would close these gaps from inside [Company]". Left column: what you would do in the first 90 days. The closing box also shows your LinkedIn URL (`linkedin` in `help`).

Content: a two- or three-sentence intro, then exactly three rows. Each row takes one issue from the positioning read (a Split, Generic or Behind row, or the claim no rival makes), says what would be done about it, and names where you have done it before. Proof points come only from your own real record; never invent a result. Then the closing box: `about_title` and `about`, ending on your real booking link (`book_url`). In kernel mode the box says this is how you work and invites a call: no pricing, no pitch. In role mode it states the role ask plainly.

Generate one company at a time: `python3 gen_maps.py COMPANYNAME`. Render each page to PNG and look at it before sending: check that option labels do not overlap their text and that nothing overruns. Never regenerate already-sent reports; improve forward only - a generator change applies to future runs, not past PDFs.

## The messages

Email first, LinkedIn connect note (under 300 chars) the next day; if 1st-degree, a direct DM replaces both. Verify the recipient's email format via two independent directories before sending; when they conflict, majority wins and the runner-up becomes the bounce fallback.

**Format (fixed):** short single-idea paragraphs separated by blank lines. Never dense blocks. This exact skeleton:

```
Hi [First name],

[One line on who you are and why you are writing.]

Before writing to you I did what I do for clients: read [Company]'s public surfaces the way a stranger would, [list of surfaces actually read].

I mapped it all against the 34 outputs a product marketing function produces. The map is attached, every output links to a plain explanation, and you can re-run the same check yourself at kernelpmm.com/gtm-map.

[One real strength, as a plain sentence, only if earned.]

The part I would want a founder to see is the positioning read on page 2. Page 3 says how I would close the gaps.

[The thesis, one short paragraph, as on page 2.]
[The rival line that makes it sharp: which rival leads with the same claim, with a short quote.]
[The claim no rival makes, and the choice it leaves them, in one sentence.]

No pitch attached, the map is yours to use either way. If any of it is useful, happy to hear your feedback.

Best,

[Your name]
```

Rules: only the positioning read goes in the message (copy slips stay in the PDF as evidence); every quoted line matches the PDF word for word; the anti-slop pass applies (no semicolons, em dashes or framing labels); no title block under the sign-off. Keep excerpts tight - cut explanatory sub-clauses and lead with the fact, roughly half the length of a first draft is usually right.

When the recipient is a 1st-degree LinkedIn connection with a live relationship context (e.g. the map lands right after their launch), the tone can shift from cold critique to a friendly readout - "launch-week readout from a friend" rather than an audit - while keeping every finding as factual and quotable as in the cold version.

## Targeting fit (who gets a map)

Primary segment: GCC fintech/proptech, funded and growing, a Head of Marketing / CMO / senior marketing leader in place, no PMM function visible. A live PMM req is the highest-value trigger (arrive before the hire is locked; the map doubles as the new hire's day-one brief). Never send a leader a map that reads as a critique of their own work: frame findings as the product marketing layer nobody owns yet.

User-requested targets outside the core segment (e.g. F&B, consumer retail, travel tech for an interview) are valid and get the same rigor - tag them in the GCC/EU target list as outside the core segment (with the reason, e.g. "user-requested" or "interview prep") rather than force-fitting fintech/proptech language onto the findings.

## After the send

Log in your outreach tracker: row ID, person, role, LinkedIn, moment, offer fit, observation used, channel, date, next step. Log replies verbatim. Retractions and corrections get written into the tracker notes so they never resurface in follow-ups.