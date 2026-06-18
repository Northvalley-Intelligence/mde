# Website Assessment To Build Context Pack

Applicable artifact profiles:

- `website_assessment`
- `client_website`
- `report_generation`
- `prompt_generation`

Use this context pack when turning a website assessment report, assessment JSON, or client intake into a client website build brief or Codex build prompt.

## Primary Goal

The generated website build prompt must produce a local service business website that is:

- SEO-friendly for humans and search engines.
- AEO-friendly for AI assistants and answer engines.
- Focused on the client's highest-value services and service areas.
- Evidence-backed by assessment findings and client intake.
- Ready for client-safe implementation in a new website repo.

Do not generate a generic brochure site. The output should tell the next Codex session how to build a site that answers:

- What does this business do?
- Who does it help?
- Where does it work?
- Why should a local customer trust it?
- How does the visitor call, book, request an estimate, or contact the business?

## Assessment Evidence Rules

- Check whether assessment data is current before using it.
- Record the assessment source, domain, scan date if available, and any known data freshness concerns.
- Trace every build recommendation back to assessment evidence, client intake, or an explicit assumption.
- Identify missing client details explicitly instead of inventing them.
- Do not claim a current-site problem exists unless the assessment provides evidence or the generated prompt asks the next agent to verify it.
- If an assessment reports broken images, broken links, missing service-area pages, missing Google Business Profile connection, or missing schema, require the generated prompt to preserve the evidence URLs/details when available.
- If evidence is weak, stale, or contradictory, the generated prompt must say "verify before implementing" and ask for a validation step.

## Recurring Assessment Findings To Address

Several local assessment reports repeatedly surface the same conversion and discovery gaps. The generated build prompt should address these by default unless the client intake says they are not applicable:

- Local Visibility: make business name, phone number, service area, location pages, and Google Business Profile connection clear on key pages.
- AI Discoverability: add clear service pages, service-area pages, FAQs, and specific answers that explain when and why customers hire the business.
- Message Clarity: say exactly what the business does, who it helps, where it works, and why a local customer should choose it.
- Lead Conversion: put visible phone number, click-to-call, contact form, and estimate/booking CTA near the top of important pages.
- Trust Signals: include reviews, testimonials, real team/location/project photos, licenses, years in business, and before/after or project examples when accurate.
- Mobile Experience: make call, booking, and contact actions visible on mobile without pinching, hunting, or scrolling through decorative content.
- Security and Reliability: use HTTPS, fix broken links/images, include favicon, Open Graph image, and sitemap.
- Performance: keep the homepage and service-area pages fast enough that mobile visitors can understand and contact the business quickly.

## SEO And AEO Service-Area Architecture

The generated build prompt should require a page map that includes:

- Homepage with clear service, service-area, trust, and CTA sections above the fold or early in the page.
- Core service pages for each high-value service or service category.
- Service-area landing pages for priority cities, counties, neighborhoods, or regions.
- Contact page with NAP details, form, click-to-call, map or Google Business link when available, and service-area summary.
- About/team/owner page with local credibility and proof.
- FAQ content that answers common buying, pricing, timing, fit, availability, and service-area questions.
- Sitemap and robots-compatible crawl path for all public pages.

Service-area pages must be crawlable, indexable unless there is a clear reason not to index them, and linked from navigation, footer, homepage, or a dedicated service areas index.

Do not create thin doorway pages. Each service-area page must include useful, locally specific content such as:

- The city, neighborhood, county, or region name.
- Services available in that area.
- Customer types served in that area.
- Relevant local proof, examples, routes, landmarks, neighborhoods, or constraints when known.
- CTA tailored to that area's likely intent.
- FAQ entries that mention the area when natural.
- Internal links to related service pages and contact/estimate paths.

If the client does not provide enough local detail, generate a content-needed checklist rather than fabricating local proof.

## AEO Requirements

AEO means the site should be easy for AI assistants, search answer boxes, and discovery systems to understand and quote accurately.

Generated prompts should require:

- Plain-language answers near the relevant service or service-area content.
- Concise FAQs for services, pricing factors, timing, availability, service area, and fit.
- Clear definitions of each core service.
- Structured sections for services, locations/service areas, process, proof, FAQs, and contact.
- Natural question headings where useful, such as "Do you offer [service] in [city]?"
- Direct answer paragraphs that can stand alone without surrounding marketing copy.
- LocalBusiness schema when appropriate.
- Service schema or structured JSON-LD when it can be accurate.
- FAQ schema only when the visible page includes the exact questions and answers.
- Organization/contact/social profile details only when verified or supplied by the client.

Do not invent reviews, ratings, licenses, service guarantees, locations, staff names, or credentials for AEO content.

## Local SEO Requirements

Generated prompts should require:

- Unique title tags and meta descriptions for homepage, service pages, service-area pages, and contact page.
- Headings that include service and service-area language naturally.
- Internal links between homepage, service pages, service-area pages, FAQs, and contact paths.
- NAP consistency across header/footer/contact sections.
- Click-to-call phone links on mobile and desktop.
- Google Business Profile or Google Maps link when supplied or discovered.
- Review/testimonial sections that reference real sources or are marked as content needed.
- Image alt text that describes real business/service/location content.
- Open Graph title, description, and image for key pages.
- XML sitemap that includes important public pages.
- Robots configuration that does not block important service or service-area pages.

## Lead Conversion Requirements

Assessment-to-build prompts must not produce pages that only inform. They must make contact easy.

Require:

- Primary CTA in the hero or first meaningful viewport.
- Persistent or repeated contact options where appropriate: phone, estimate, appointment, quote, consultation, or booking.
- Contact form with clear fields and success/failure states.
- Mobile-first click-to-call.
- CTA copy matched to the business model.
- Footer with NAP, service areas, key services, and contact links.

## Common Assessment-Report Failure Modes To Avoid

Generated build prompts must avoid repeating weaknesses observed in assessment/report workflows:

- Do not say "service-area pages are missing" unless the assessment evidence supports it. If uncertain, require the build agent to inspect current URLs before claiming the gap.
- Do not say "broken images" or "broken links" without requiring exact URLs or a verification step.
- Do not treat a general city mention as a sufficient service-area strategy.
- Do not treat one generic service page as sufficient for multiple high-value services.
- Do not create service-area pages by duplicating the same copy with city names swapped.
- Do not claim Google Business Profile linkage unless a URL or clear evidence exists.
- Do not invent testimonials, reviews, ratings, project photos, before/after examples, or licenses.
- Do not bury contact options below long decorative content.
- Do not optimize only for desktop.
- Do not optimize only for search crawlers while ignoring human trust and conversion.

## Generated Prompt Output Contract

When this context pack is used by the client website build prompt generator, the generated output should include:

- Website build mission.
- Client intake summary.
- Assessment evidence summary.
- Missing client details and content-needed checklist.
- SEO/AEO strategy focused on services and service areas.
- Page map with homepage, service pages, service-area pages, FAQ, about/proof, and contact.
- Technical implementation constraints supplied by the project or intake.
- Content rules that prevent invented claims.
- Validation plan.
- Codex build prompt for the new client repo.
- Confidentiality notes and client-safe MDE bootstrap instructions.

## Validation Expectations

The generated prompt should require the future client website repo to validate:

- Homepage states business, core services, service area, trust proof, and CTA.
- Priority services have explicit, crawlable service pages or clearly justified sections.
- Priority service areas have useful, crawlable pages or are listed as missing content decisions.
- FAQ content answers service, pricing-factor, timing, availability, fit, and service-area questions.
- LocalBusiness schema is valid when used and does not contain invented claims.
- Service/FAQ schema matches visible content when used.
- NAP and primary CTA are visible on desktop and mobile.
- Phone links use `tel:` where a phone number is available.
- Contact form works and preserves user input on validation errors.
- Google Business/Profile link is present when supplied.
- Sitemap includes homepage, service pages, service-area pages, FAQ, about, and contact.
- Broken links and broken images are checked before delivery.
- Mobile viewport and first useful mobile screen are reviewed.
- Performance is checked on the homepage and at least one service-area page.
- Assessment-derived recommendations are traceable to evidence, intake, or documented assumptions.
