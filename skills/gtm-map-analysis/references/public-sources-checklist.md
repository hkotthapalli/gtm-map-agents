# GTM Map Analysis · Public sources checklist

**Purpose:** what to check, per map, beyond the website. Each source is listed with what it reveals and which of the 34 outputs it can move (U→P, M→P, or verify a V). Two tiers: the **Quick Map** (45–60 min, what every outreach artifact gets) and the **Deep Map** (2–3 hrs, for paid work or high-value targets).

---

## Tier 1 · Quick Map (every outreach artifact)

| # | Source | How | What it moves |
|---|--------|-----|---------------|
| 1 | **The complete website, rendered** | Every page reachable from nav + sitemap: hero, product pages, pricing, about, careers, blog, legal | Positioning, Landing page, ICP, Packaging/pricing, Channel/funnel |
| 2 | **Raw HTML (JS off)** | Fetch without JavaScript; compare to rendered | What crawlers/AI actually read. Keyper lesson: counters read AED 0M raw vs 71M rendered |
| 3 | **Funding press** | TechCrunch, Wamda, MENAbytes, Zawya, LinkedIn announcement | Message drift (investor narrative vs site), Why now, budget signal |
| 4 | **LinkedIn company page** | Tagline, last 10 posts, employee count, open roles | Message drift (page vs site), launch cadence, team/budget signals |
| 5 | **Live job listings** | Careers page + LinkedIn Jobs + Ashby/Greenhouse/Workable | Strategy leaks (new markets, new products in reqs); PMM gap confirmation |
| 6 | **One AI-engine ask** | Ask ChatGPT or Perplexity "what is [company]?" and one buyer question ("best [category] in Dubai") | AI visibility: named or absent, described correctly or wrongly |
| 7 | **App stores + applicable review surfaces** | iOS/Play Store if an app exists; plus Trustpilot, Reddit, Product Hunt, G2/Capterra (B2B SaaS), and industry/vertical review sites as applicable — presence + headline score at this tier | Release notes, VoC, Trust metrics |
| 8 | **Every internal link on the homepage** | Click them all | Broken surfaces (qeen's blog 404), orphan pages, hidden pricing |
| 8b | **Rival scan (4-6 rivals)** | Render each rival's market-facing homepage; quote hero, segment, category, reason-to-choose, proof, local cues | The positioning read on page 2; Table-stakes read; Positioning |

## Tier 2 · Deep Map additions (paid work / high-value targets)

| # | Source | How | What it moves |
|---|--------|-----|---------------|
| 9 | **Wayback Machine** | web.archive.org: homepage 12 and 24 months ago | Message drift over time; how many repositionings; what was abandoned |
| 10 | **Review platforms** | G2, Capterra, Trustpilot, Google Maps (B2C/local) | VoC U→P; Trust metrics; competitor comparisons in reviewers' words |
| 11 | **Reddit / community forums** | Search "[company]" on Reddit, local forums, Facebook groups (GCC: also Arabic queries) | Unfiltered VoC; objections the FAQ should answer |
| 12 | **Founder/exec public content** | LinkedIn posts, podcast appearances, conference talks, YouTube | The internal narrative; drift between founder story and site; Why now argument |
| 13 | **Terms of service + privacy page** | Read the legal pages | Real pricing mechanics (attribution windows, ownership, terms) the marketing site hides |
| 14 | **Help center / docs / changelog** | support.x.com, docs.x.com, /changelog | Onboarding journey, Release notes, FAQ (internal one leaks here) |
| 15 | **SERP read** | Google the brand + top 3 category queries; read titles/snippets/People Also Ask | What crawlers chose to say; meta/OG quality; competitor adjacency |
| 16 | **Link preview test** | Paste URL into WhatsApp/LinkedIn draft | The card most GCC buyers actually see first (WhatsApp is the channel here) |
| 17 | **Competitor surface scan, deeper** | Rival pricing, product pages and sales pages beyond the Quick Map's homepage scan | Table-stakes read M→P; whitespace the target could claim |
| 18 | **Traffic/SEO estimate** | Similarweb free tier, Ahrefs free tools | Channel reality vs channel claims |
| 19 | **Glassdoor** | Company reviews, esp. sales/marketing roles | GTM chaos signals ("no positioning", "messaging changes weekly") |
| 20 | **Regulator registers (GCC)** | DFSA, VARA, SCA, CBUAE, ADGM/DIFC public registers | Claim check for regulated fintech; licence claims vs register |
| 21 | **Local language parity** | GCC: compare Arabic surfaces to English. EU and other markets: same check in each market's local language (ES, FR, DE...) | Whether the local-language buyer gets the same story or a stale one |
| 22 | **Marketplace listings** | Shopify App Store, AWS/Azure marketplace, partner directories | Channel/funnel; reviews; how partners describe them (drift) |

---

## Source → output map (which glyphs each source can move)

- **Voice of customer** (usually U): app reviews (7), G2/Trustpilot (10), Reddit (11) → P
- **Win/loss, Assumption log, Pre-mortem, Launch brief/tiers, Product Oracle, funnel metrics, Half-Life, Six-stage, Deck spine, Sales enablement**: genuinely internal. Stay U — saying so honestly is part of the map's credibility.
- **Market report**: blog/insights content (1, 14), founder talks (12)
- **Why now**: funding press (3), founder content (12)
- **The Fifty / Table-stakes / Competitor monitor**: competitor scan (17), SERP (15), reviews naming rivals (10)
- **AI visibility**: direct ask (6), SERP (15)
- **ICP/segments, Use cases, Buying committee**: site (1), job reqs (5), case-study personas (1)
- **Positioning**: site (1) vs Wayback (9) vs founder content (12) — three-way consistency test
- **Packaging/pricing**: pricing page (1), ToS (13), marketplace listings (22)
- **Messaging framework / Message drift**: site vs LinkedIn (4) vs press (3) vs Arabic (21) vs Wayback (9)
- **Claim check**: every claim on (1) vs press (3), registers (20), reviews (10)
- **Landing page**: rendered (1) + raw (2) + preview card (16)
- **Channel/funnel**: CTAs (1), SERP (15), traffic estimate (18), marketplaces (22)
- **FAQ**: site (1), help center (14), the questions Reddit/reviews actually ask (10, 11)
- **Onboarding journey**: docs (14), app store screenshots (7), signup flow (1)
- **Release notes**: changelog (14), app update history (7)
- **Trust metrics**: review platforms (10), status page, security page (1)
- **Launch post-mortem**: launch posts (4) vs what shipped (7, 14) — outside-in inference only

---

## Rules

1. **The map states its own sources.** Footer names what was read ("public pages, app stores, press, AI engines, as of [date]"). Currently it says "public pages only" — keep that literally true per tier.
2. **A glyph only upgrades on evidence you can quote.** No inference upgrades.
3. **Every Quick Map gets one raw-HTML read and one AI-engine ask minimum.** Both have produced the sharpest findings so far (Keyper's zeros, qeen's identity guess).
4. **Deep Map is billable.** The Quick Map is the outreach artifact; the Deep Map is what a paid audit or sprint opens with. Never give away tier 2 in cold outreach — mention that it exists.
5. **Language parity always:** Arabic check on every GCC target, local-language check on every EU or other-market target, WhatsApp preview test on every UAE/KSA target.

## False-positive traps (learned in the field, 26 Aug 2026)

1. **Carousel duplication is not visible duplication.** Sliders duplicate slides in the DOM for looping. A quote appearing twice in raw HTML is only a finding if a human sees it twice on the rendered page. (Caught on Qashio before send.)
2. **JS-rendered UI is invisible to fetchers.** Language switchers, counters, geo-banners and toggles often exist only after JavaScript runs. Never claim a surface is "missing" (no Arabic version, no pricing toggle, no chat) from a raw fetch alone — confirm in a real browser first. (Qashio has an Arabic version the fetcher could not see; Keyper's counters read as zeros the same way.)
3. **The rule that generalizes both:** raw-vs-rendered differences are findings about *crawlers and AI engines*, never findings about what a human visitor experiences. Attribute each claim to the right reader.

## The reproducibility standard (27 Aug 2026)

Every glyph and every gap must survive the prospect re-running the check themselves via kernelpmm.com/gtm-map. Before any map ships: (a) no absolutes ("anywhere", "never", "no X at all") unless every relevant page was read — otherwise write "on the pages I read"; (b) any claim naming third-party surfaces (affiliates, review scores, SERP results) must come from a live search in the same week, not from memory; (c) the sources line lists only what was actually run.

## Language rules (27 Aug 2026)

Findings are written in direct, simple sentences. Say what is there, what is missing, and what it costs the business. Specifically: gap headlines are plain statements of fact ("The site shows no numbers"), never slogans or parallel constructions ("Brave pricing, thin proof", "Four products, one sentence, no one named"); no metaphors doing the work of evidence ("old wallpaper", "the comparison shelf"); no rhetorical questions as closers; every sentence should survive being read aloud to the prospect's face. If a line sounds like a LinkedIn post, rewrite it as a fact.

## Email sources (finding the recipient's address)

Two independent sources minimum; when they conflict, majority wins and the runner-up becomes the bounce fallback.

1. **Directories with masked previews (free):** RocketReach, ZoomInfo, LeadIQ, ContactOut, Lusha, Kaspr. Masks plus format percentages triangulate most addresses without paying. They disagree roughly a fifth of the time.
2. **Format + verification tools:** Hunter.io (25 free/month, format confidence per domain), Apollo.io (largest B2B database, free tier, built-in verify), Snov.io, Prospeo, FindThatLead, Skrapp.
3. **Verifiers before sending:** MillionVerifier, NeverBounce, ZeroBounce (free credits). Run the guessed address; catch-all domains verify nothing, note it and rely on LinkedIn instead.
4. **Manual sources tools miss:** PR contact lines in funding press, WHOIS on young domains, conference speaker pages, podcast show notes, GitHub commits (technical founders), EU legal/imprint pages, and LinkedIn Contact Info after a connect is accepted (ground truth).
5. **Volume (Track B) stack:** Apollo or Hunter to generate, MillionVerifier to clean; this is what hired researchers charge ~$0.10/verified row to do.
