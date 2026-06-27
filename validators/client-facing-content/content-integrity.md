# Client-Facing Content Integrity Validator Candidate

Goal:
Prevent generated client-facing material from leaking process notes, publishing placeholder proof, or making unsupported business claims.

Applies to:

- `client_website`
- `public_content`
- `client_facing_document`
- `business_document`
- `pdf_generation`
- `print_layout`

Suggested checks:

- Fail public pages or documents that include implementation-process, AI-process, SEO-process, assessment-process, or template-explanation copy instead of customer-facing language.
- Fail sample articles, fake case studies, fake testimonials, invented reviews, invented project examples, or placeholder proof unless they are clearly excluded from public/client delivery.
- Confirm every client proof item has permission, attribution when needed, and enough source evidence to publish.
- Confirm operational facts match the source of truth: services offered, services not offered, directions, hours, availability, materials, guarantees, credentials, locations, delivery, and quote expectations.
- Mark missing client inputs as pending instead of filling the gap with invented or generic copy.
- Check that repeated visual examples genuinely add proof variety; if photos or examples are too similar, record the gap and request approved client assets.
- Replace internal labels such as "quote fit details", "current-site service signal", or "this page should..." with language a real customer would understand.

Run policy:

- Before client review of a website, flyer, report, sales PDF, proposal, or public content page.
- When generated copy, testimonials, service pages, service-area pages, gallery captions, project examples, quote guidance, or proof sections change.
- During third-person validation for client-facing deliverables.

Default severity:
High. Critical if the issue could mislead a client/customer, publish false proof, expose confidential/internal process, or create a legally or commercially risky claim.
