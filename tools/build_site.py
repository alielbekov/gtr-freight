#!/usr/bin/env python3
"""Generate the static GTR Freight site (12 pages) into the project folder."""
import os, sys

OUT = sys.argv[1]

# ---------- icons ----------
I = {
    "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25c1.1.37 2.3.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8z"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="12" fill="currentColor"/><path d="M7 12.5l3 3 7-7" stroke="#fff" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "arrow-l": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>',
    "arrow-r": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.4 2H3.6A1.6 1.6 0 0 0 2 3.6v16.8A1.6 1.6 0 0 0 3.6 22h16.8a1.6 1.6 0 0 0 1.6-1.6V3.6A1.6 1.6 0 0 0 20.4 2zM8 19H5V9h3zM6.5 7.7A1.7 1.7 0 1 1 8.2 6a1.7 1.7 0 0 1-1.7 1.7zM19 19h-3v-4.9c0-1.2 0-2.7-1.6-2.7s-1.9 1.3-1.9 2.6V19h-3V9h2.9v1.4a3.2 3.2 0 0 1 2.9-1.6c3 0 3.6 2 3.6 4.6z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm-.4 2L12 11.4 4.4 6zM4 18V7.9l8 5.7 8-5.7V18z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2zm-3 10H7v-2h10zm0-3H7V7h10z"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><line x1="12" y1="3" x2="12" y2="7"/><line x1="12" y1="17" x2="12" y2="21"/><line x1="3" y1="12" x2="7" y2="12"/><line x1="17" y1="12" x2="21" y2="12"/></svg>',
    "cursor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 3l16 7-7 2-3 7z"/></svg>',
    "thumb": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 11v10H3V11z"/><path d="M7 11l4-8a2.5 2.5 0 0 1 2.5 2.5V9h5.2a2 2 0 0 1 2 2.3l-1.2 7.4a2 2 0 0 1-2 1.7H7"/></svg>',
    "menu": '<svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
    "close": '<svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>',
}

PHONE = "+1 513 244 8706"
PHONE_HREF = "tel:+15132448706"

SHIPPERS = [
    ("freight-brokerage.html", "Freight brokerage"),
    ("managed-transportation.html", "Managed transportation"),
    ("warehousing.html", "Warehousing and Fulfillment"),
    ("cross-border.html", "Cross-Border Logistics"),
    ("ship-international.html", "Ship International"),
    ("become-shipper.html", "Become a shipper"),
]
CARRIERS = [
    ("become-carrier.html", "Become a carrier"),
    ("become-carrier.html#requirements", "Carrier requirements"),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
"""


def menu(items):
    return '<div class="dropdown-menu">' + "".join(f'<a href="{h}">{t}</a>' for h, t in items) + "</div>"


def header(active, home=False):
    def cur(page):
        return ' aria-current="page"' if active == page else ""
    actions = (
        '<a class="btn btn-black" href="become-shipper.html">Become shipper</a>'
        '<a class="btn btn-primary" href="contacts.html#form">Request a quote</a>'
        if home else
        f'<a class="nav-phone" href="{PHONE_HREF}">{I["phone"]}{PHONE}</a>'
        '<a class="btn btn-primary" href="contacts.html#form">Request a quote</a>'
    )
    shippers_active = ' aria-current="page"' if active in ("shippers",) else ""
    carriers_active = ' aria-current="page"' if active in ("carriers",) else ""
    return f"""<header class="site-header">
  <div class="container nav">
    <a class="nav-logo" href="index.html" aria-label="GTR Freight home"><img src="assets/img/logo.png" alt="GTR Freight" width="120" height="48"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Toggle menu">{I["menu"]}{I["close"]}</button>
    <nav class="nav-menu" id="nav-menu" aria-label="Main">
      <ul class="nav-links">
        <li class="dropdown"><button class="nav-link" type="button" aria-expanded="false"{shippers_active}>Shippers {I["chev"]}</button>{menu(SHIPPERS)}</li>
        <li class="dropdown"><button class="nav-link" type="button" aria-expanded="false"{carriers_active}>Carriers {I["chev"]}</button>{menu(CARRIERS)}</li>
        <li><a class="nav-link" href="about.html"{cur("about")}>About</a></li>
        <li><a class="nav-link" href="careers.html"{cur("careers")}>Careers</a></li>
        <li><a class="nav-link" href="contacts.html"{cur("contacts")}>Contacts</a></li>
      </ul>
      <div class="nav-actions">{actions}</div>
    </nav>
  </div>
</header>
"""


FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>Contact</h4>
          <ul>
            <li>Phone: <a href="tel:8555555555">855-555-5555</a></li>
            <li>Email: <a href="mailto:info@gtrfreight.com">info@gtrfreight.com</a></li>
            <li class="addr">4030 SMITH RD STE 200<br>CINCINNATI, OH 45209</li>
          </ul>
          <div class="social">
            <a href="https://www.linkedin.com/" aria-label="LinkedIn" target="_blank" rel="noopener">{I["linkedin"]}</a>
            <a href="https://www.facebook.com/" aria-label="Facebook" target="_blank" rel="noopener">{I["facebook"]}</a>
            <a href="https://www.instagram.com/" aria-label="Instagram" target="_blank" rel="noopener">{I["instagram"]}</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="contacts.html#form">Request a quote</a></li>
            <li><a href="about.html">Overview</a></li>
            <li><a href="about.html#mission">Our mission</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Solutions</h4>
          <ul>
            <li><a href="freight-brokerage.html#services">Dry Van</a></li>
            <li><a href="freight-brokerage.html#services">Refrigerated</a></li>
            <li><a href="freight-brokerage.html#services">Flatbed/Specialized</a></li>
            <li><a href="freight-brokerage.html#services">Expedited</a></li>
            <li><a href="freight-brokerage.html#services">Heavy Haul/Oversize</a></li>
            <li><a href="freight-brokerage.html#services">White Glove</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About us</a></li>
            <li><a href="team.html">Our team</a></li>
            <li><a href="careers.html">Careers</a><br><span class="badge-hiring">Hiring!</span></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="footer-bar">© GTR Freight. All rights reserved.</div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def hero(title, sub, img, home=False, extra=""):
    cls = "hero hero--home" if home else "hero hero--inner"
    return f"""<section class="{cls}" style="background-image:url('assets/img/{img}')">
  <div class="container">
    <h1>{title}</h1>
    {extra}
    <p>{sub}</p>
    {"" if not home else '<div class="hero-actions"><a class="btn btn-primary btn-lg" href="become-shipper.html">Ship with us</a><a class="btn btn-white btn-lg" href="contacts.html">Contact us</a></div>'}
  </div>
</section>
"""


def cta(title, label, href):
    return f"""<section class="cta-section">
  <div class="container">
    <div class="cta" style="background-image:url('assets/img/cta-truck.jpg')">
      <h2>{title}</h2>
      <a class="btn btn-white" href="{href}">{label}</a>
    </div>
  </div>
</section>
"""


TESTIMONIALS = [
    ("David Nguyen", "Keystone Manufacturing",
     "From planning to final delivery, GTR Freight keeps our freight moving on schedule. Their real-time tracking and proactive updates give our team complete peace of mind."),
    ("John Anderson", "Swift Solutions Inc.",
     "GTR Freight has been an incredible partner for our flatbed and heavy-haul needs. They handle our specialized shipments with expertise and care, ensuring everything arrives safely. Their dedication to excellence makes them our go-to logistics provider."),
    ("Emily Carter", "FreshFlow Distribution",
     "GTR Freight has been a dependable partner for our refrigerated shipping solutions, saving us both time and money. Their customer service team understands our business and responds to our needs promptly."),
]


def testimonials():
    cards = "".join(
        f'<article class="testimonial"><p class="t-name">{n}</p><p class="t-company">{c}</p><p class="t-quote">{q}</p></article>'
        for n, c, q in TESTIMONIALS)
    return f"""<section class="testimonials">
  <div class="container"><h2 class="section-title">True Partnership Approach</h2></div>
  <div class="carousel">
    <div class="carousel-track">{cards}</div>
    <div class="carousel-nav">
      <button class="carousel-btn" type="button" data-dir="prev" aria-label="Previous testimonial">{I["arrow-l"]}</button>
      <button class="carousel-btn" type="button" data-dir="next" aria-label="Next testimonial">{I["arrow-r"]}</button>
    </div>
  </div>
</section>
"""


BAND = """<section class="band" style="background-image:url('assets/img/band-road.jpg')">
  <div class="container">
    <h2>Ready to ship your goods with us?</h2>
    <div class="band-side">
      <p>Unlock competitive shipping rates and personalized logistics solutions tailored to your business needs.</p>
      <a class="btn btn-white" href="contacts.html#form">Request a quote</a>
    </div>
  </div>
</section>
"""


def info_cards(email):
    return f"""<aside class="info-cards">
  <div class="info-card">{I["mail"]}<div><h3>Email Us</h3><p>We'll respond to your inquiry as soon as possible.</p><a href="mailto:{email}">{email}</a></div></div>
  <div class="info-card">{I["phone"]}<div><h3>Call Us</h3><p>Our customer support team is available</p><a href="{PHONE_HREF}">+1 (513) 244 8706</a></div></div>
  <div class="info-card">{I["chat"]}<div><h3>Live Chat</h3><p>Chat with us in real-time using our live chat feature.</p><a href="mailto:support@gtrfreight.com">support@gtrfreight.com</a></div></div>
</aside>
"""


def field(label, name, placeholder, typ="text", cls="", required=True):
    req = " required" if required else ""
    return f'<div class="field {cls}"><label for="{name}">{label}</label><input type="{typ}" id="{name}" name="{name}" placeholder="{placeholder}"{req}></div>'


def phone_field(label="Phone", name="phone", cls=""):
    return f"""<div class="field {cls}"><label for="{name}">{label}</label>
  <div class="phone-group"><select aria-label="Country code" name="{name}_country"><option>US</option><option>CA</option><option>MX</option></select><input type="tel" id="{name}" name="{name}" placeholder="+1 (876) 987 621" required></div></div>"""


def select_field(label, name, options, cls=""):
    opts = "".join(f"<option>{o}</option>" for o in options)
    return f'<div class="field {cls}"><label for="{name}">{label}</label><select id="{name}" name="{name}">{opts}</select></div>'


SERVICES_LIST = ["Freight brokerage", "Managed transportation", "Warehousing and Fulfillment", "Cross-Border Logistics", "Ship International"]

pages = {}

# ---------------- HOME ----------------
badges = "".join(f'<span>{I["check"]}{t}</span>' for t in ["99% satisfaction rate", "Reliable carrier network", "Customer Support"])
home_services = [
    ("Dry Van", "Reliable and secure transportation for all your freight needs.", ""),
    ("Refrigerated", "Temperature-controlled solutions to keep your goods fresh.", " card--active"),
    ("Flatbed/Specialized", "Versatile transport for oversized and specialized freight.", ""),
    ("Expedited", "Fast, time-critical delivery for urgent or high-value shipments.", ""),
    ("Heavy Haul/Oversize", "Safe transport for overweight loads with expert routing and permits.", ""),
    ("White Glove", "Careful handling and inside delivery for sensitive, high-touch freight.", ""),
]
home_cards = "".join(
    f'<article class="card{c}"><h3>{t}</h3><p>{d}</p><a class="card-link" href="freight-brokerage.html#services">See Details</a></article>'
    for t, d, c in home_services)
pins = [(11.5, 58, ""), (31, 44, ""), (44, 51, ""), (71, 40.5, "Indianapolis, IN"), (70, 59, ""), (71, 68, "")]
pins_html = "".join(
    f'<span class="pin" style="left:{x}%;top:{y}%">{f"<span class=\'pin-label\'>{l}</span>" if l else ""}</span>'
    for x, y, l in pins)
partners = [("dat", "DAT", ""), ("123loadboard", "123Loadboard", ""), ("truckstop", "Truckstop.com", ""),
            ("coyote", "Coyote Logistics", "wide"), ("convoy", "Convoy", "wide"), ("loadsmart", "Loadsmart", "")]
partners_html = "".join(f'<img src="assets/img/partners/{f}.png" alt="{a}" class="{c}">' for f, a, c in partners)

pages["index.html"] = head("GTR Freight — Support Your Global Delivery Without Breaking The Bank",
                           "GTR Freight is a freight brokerage and logistics partner offering dry van, refrigerated, flatbed, managed transportation, warehousing and cross-border solutions.") \
    + header("home", home=True) \
    + hero("Support Your Global Delivery <br>Without Breaking The Bank",
           "Discover how our unmatched expertise, unrivalled scale and tailored solutions can solve your toughest supply chain challenges, every single time.",
           "hero-home.jpg", home=True, extra=f'<div class="hero-badges">{badges}</div>') \
    + f"""<section class="partners">
  <div class="container">
    <div class="trusted-pill">Trusted by <strong>50+ partners</strong></div>
    <div class="partner-logos">{partners_html}</div>
  </div>
</section>
<section class="redefine">
  <div class="container">
    <h2 class="section-title">Redefining logistics with <span class="accent">innovative</span> and <span class="accent">reliable</span> freight brokerage</h2>
    <p class="section-lead">Our commitment to innovation, reliability, and customer success sets us apart in the industry. By connecting businesses with trusted carriers and leveraging advanced technology, we ensure cost-effective and timely transportation solutions.</p>
    <a class="btn btn-primary" href="about.html">Learn about us</a>
  </div>
</section>
{BAND}
<section class="map-section">
  <div class="map-panel">
    <h2 class="section-title">Everywhere you <span class="accent">need</span> to be</h2>
    <div class="map-wrap">
      <img src="assets/img/map-us.png" alt="Map of the United States with GTR Freight locations" width="722" height="454">
      {pins_html}
    </div>
  </div>
</section>
<section class="section" id="services">
  <div class="container">
    <div class="services-head"><h2 class="section-title">Freight <span class="accent">services</span> we offer</h2></div>
    <div class="cards cards-3">{home_cards}</div>
    <div class="services-foot"><a class="btn btn-primary" href="freight-brokerage.html">Explore all our services</a></div>
  </div>
</section>
""" + testimonials() + cta("Ready for less risk &amp; More Savings?", "Request a quote", "contacts.html#form") + FOOTER

# ---------------- ABOUT ----------------
values = [
    ("We always act with integrity", "We build trust through honest, transparent, and ethical practices in everything we do"),
    ("You can rely on us every time", "Dependable services you can count on to deliver results, every time without fail"),
    ("We innovate for smarter solutions", "We embrace technology to provide cutting-edge solutions for modern logistics"),
    ("Your needs are our top priority", "Your success is our priority, with tailored support to meet your unique needs"),
]
values_html = "".join(
    f'<li class="value-item"><span class="value-num">{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(values))
stats = [("255K", "Loads shipped in 2024"), ("1,500", "Satisfied clients"), ("250M", "Miles Traveled in 2024"), ("99.5%", "On-time delivery")]
stats_html = "".join(f'<div class="stat"><strong>{n}<sup>+</sup></strong><span>{l}</span></div>' for n, l in stats)
pages["about.html"] = head("About us — GTR Freight", "Discover who we are, our journey in the freight industry, and how our dedicated team delivers efficient and reliable logistics solutions.") \
    + header("about") \
    + hero("About us", "Discover who we are, our journey in the freight industry, and how our dedicated team is committed to delivering efficient and reliable logistics solutions", "hero-about.jpg") \
    + f"""<section class="mission" id="mission">
  <div class="container">
    <div class="mission-grid">
      <h2 class="section-title">Our mission is to <span class="accent">drive your success</span> across the country</h2>
      <div class="mission-text">
        <p>At GTR Freight, we are committed to fueling the growth and success of businesses across the nation. With decades of expertise in the logistics industry, our mission is to drive your success by ensuring timely and cost-effective delivery solutions.</p>
        <p>We understand that the backbone of your business relies on the seamless transportation of goods, which is why we leverage cutting-edge technology and extensive carrier networks to meet your freight needs efficiently.</p>
      </div>
    </div>
    <div class="stats">{stats_html}</div>
  </div>
</section>
<section class="values">
  <div class="container">
    <span class="eyebrow">Our values</span>
    <h2 class="section-title">Our values reflect both <span class="accent">who we are</span> and <span class="accent">who we strive to be</span></h2>
    <ul class="values-list">{values_html}</ul>
  </div>
</section>
""" + cta("Ready for less risk &amp; More Savings?", "Get Started", "become-shipper.html") + FOOTER

# ---------------- TEAM ----------------
team = [
    ("john-doe", "John Doe", "Chief Financial Advisor", "#e8d6d2"),
    ("lucas-graham", "Lucas Graham", "Investment Specialist", "#d9e3c7"),
    ("will-mitchell", "Will Mitchell", "Retirement Specialist", "#d4e1ec"),
    ("mia-torres", "Mia Torres", "Client Relations", "#eadccb"),
    ("aiden-lee", "Aiden Lee", "Wealth Manager", "#dbe7cf"),
    ("alian-lane", "Alian Lane", "Head of HR", "#e6d8ec"),
]
team_html = "".join(
    f'<li class="member"><div class="member-photo" style="background:{bg}"><img src="assets/img/team/{f}.png" alt="{n}" width="320" height="320" loading="lazy"></div><h3>{n}</h3><p>{r}</p></li>'
    for f, n, r, bg in team)
pages["team.html"] = head("Our team — GTR Freight", "Meet the minds behind the movement: the dedicated professionals driving success at GTR Freight.") \
    + header("about") \
    + hero("Our team", "Discover who we are, our journey in the freight industry, and how our dedicated team is committed to delivering efficient and reliable logistics solutions", "hero-team.jpg") \
    + f"""<section class="team">
  <div class="container">
    <h2 class="section-title">Meet the minds behind the <span class="accent">movement</span>, dedicated professionals <span class="accent">driving success</span></h2>
    <ul class="team-grid">{team_html}</ul>
  </div>
</section>
""" + BAND + cta("Ready for less risk &amp; More Savings?", "Get Started", "become-shipper.html") + FOOTER

# ---------------- BECOME CARRIER ----------------
reqs = [
    "<strong>Owner ID</strong> – Required for all new onboarding carriers.",
    "<strong>Inspection History</strong> – If you have no inspection history with FMCSA, we require a cab card and photo of your truck with company name and MC or DOT visible on the truck.",
    "<strong>Certificate of Insurance</strong> – Must have a minimum of $1 million in Auto coverage and $100,000 in Cargo coverage.",
    "<strong>ELD Connection in Highway profile</strong> — if you are legally exempt, you must provide a cab card and title for a customer service representative to bypass.",
]
reqs_html = "".join(f'<li>{I["check"]}<span>{r}</span></li>' for r in reqs)
pages["become-carrier.html"] = head("Become a carrier — GTR Freight", "Partner with GTR Freight to access reliable loads, streamlined processes, and consistent support for your business.") \
    + header("carriers") \
    + hero("Become carrier", "Partner with GTR Freight to access reliable loads, streamlined processes, and consistent support for your business.", "hero-carrier.jpg") \
    + f"""<section class="dots">
  <div class="container">
    <h2 class="section-title">Interested in joining our network of freight carriers?</h2>
    <p class="section-lead">Partner with GTR Freight to access reliable loads, streamlined processes, and consistent support for your business.</p>
    <a class="btn btn-primary" href="contacts.html#form">Contact us</a>
  </div>
</section>
<section class="section" id="requirements">
  <div class="container">
    <div class="split">
      <img src="assets/img/carriers-talking.jpg" alt="Two carriers talking in front of their trucks" width="450" height="300" loading="lazy">
      <div>
        <h2>Requirements for New Carriers:</h2>
        <ul class="check-list">{reqs_html}</ul>
      </div>
    </div>
  </div>
</section>
""" + cta("Ready for less risk &amp; More Savings?", "Get Started", "contacts.html#form") + FOOTER

# ---------------- CAREERS ----------------
career_cards = [
    ("Growth", "Advance your career with learning opportunities and professional development."),
    ("Innovation", "Work with cutting-edge technology shaping the future of freight logistics."),
    ("Support", "Join a team that values collaboration and provides tools for success."),
    ("Impact", "Make a difference in an industry by driving meaningful, lasting change."),
]
career_html = "".join(f'<article class="card"><h3>{t}</h3><p>{d}</p></article>' for t, d in career_cards)
pages["careers.html"] = head("Careers — GTR Freight", "Join GTR Freight and be part of a team transforming logistics with innovation, reliability, and unmatched customer focus.") \
    + header("careers") \
    + hero("Careers", "Join GTR Freight and be part of a team transforming logistics with innovation, reliability, and unmatched customer focus.", "hero-careers.jpg") \
    + f"""<section class="careers-intro">
  <div class="container">
    <div class="careers-grid">
      <h2 class="section-title">We’re <span class="accent">leading</span> the pace of <span class="accent">logistics</span> to move the world’s goods</h2>
      <p class="careers-copy">At GTR Freight, we believe in building a workplace where innovation meets opportunity, empowering individuals to grow, lead, and make a lasting impact in logistics.</p>
      <div class="careers-cards">{career_html}</div>
    </div>
  </div>
</section>
""" + cta("Become a part of our team today", "View job opportunities", "contacts.html#form") + FOOTER

# ---------------- FREIGHT BROKERAGE ----------------
features = [
    ("target", "Efficient shipping solutions", "Maximize efficiency with tailored shipping solutions designed to save time, reduce costs, and streamline your logistics operations."),
    ("cursor", "Reliable carrier network", "Gain access to a vast network of trusted carriers, ensuring your freight is delivered safely and on time, every time."),
    ("thumb", "Customer support", "Rely on our dedicated 24/7 support team, always ready to assist you and address any challenges for seamless freight management."),
]
features_html = "".join(f'<div class="feature">{I[ic]}<h3>{t}</h3><p>{d}</p></div>' for ic, t, d in features)
covered = [
    ("van", "Dry Van", "Reliable, secure shipping for dry goods, retail, and general freight, protected from the elements."),
    ("flatbed", "Open Deck", "Flatbeds and step decks for oversized, heavy, or irregular cargo with expert handling."),
    ("reefer", "Temperature Controlled", "Refrigerated transport for perishable goods, ensuring precise temperature control."),
    ("heavyhaul", "Heavy Haul/Specialized", "Safe transport for oversized and overweight loads with expert routing and permits."),
    ("ltl", "Less-Than-Truckload", "Cost-effective shipping for smaller loads, combining freight for efficiency."),
    ("expedited", "Expedited/High Value", "Fast, secure delivery for urgent or high-value shipments with real-time tracking."),
    ("international", "International Shipping", "Hassle-free cross-border and global shipping with customs and compliance support."),
]
covered_html = "".join(
    f'<article class="card card--white card--media"><img src="assets/img/services/{f}.jpg" alt="{t}" width="112" height="84" loading="lazy"><div class="card-body"><h3>{t}</h3><p>{d}</p></div></article>'
    for f, t, d in covered)
pages["freight-brokerage.html"] = head("Freight brokerage — GTR Freight", "GTR Freight responds to your most challenging domestic and international transportation requirements with multimodal freight brokerage solutions.") \
    + header("shippers") \
    + hero("Freight brokerage", "GTR Freight responds to your most challenging domestic and international transportation requirements with our multimodal freight brokerage solutions.", "hero-freight.jpg") \
    + f"""<section class="features">
  <div class="container"><div class="features-panel">{features_html}</div></div>
</section>
<section class="covered" id="services">
  <div class="container">
    <h2 class="section-title">We <span class="accent">have you</span> covered</h2>
    <div class="cards cards-2">{covered_html}</div>
  </div>
</section>
""" + testimonials() + cta("Ready to move forward?", "Get in touch", "contacts.html#form") + FOOTER

# ---------------- MANAGED TRANSPORTATION ----------------
steps = [
    ("Planning &amp; Optimization", "We start by analyzing your shipping requirements, freight volume, and preferred routes. Using advanced logistics technology and industry expertise, we optimize transportation strategies to reduce costs, improve delivery times, and maximize efficiency. This includes selecting the best carriers, consolidating shipments when possible, and ensuring compliance with regulations.", "managed-planning.jpg", "Team planning routes on a whiteboard"),
    ("Execution &amp; Tracking", "Once the plan is in place, our team manages the entire shipment process from pickup to final delivery. We coordinate with carriers, schedule shipments, and oversee loading and transit. Real-time tracking and visibility allow us to monitor progress, address any delays, and ensure on-time delivery, keeping you informed every step of the way.", "managed-tracking.jpg", "Tracking shipments on a planning board"),
    ("Performance &amp; Reporting", "We continuously monitor shipment performance, tracking key metrics such as transit times, carrier reliability, and freight costs. Our detailed reports provide insights into shipping trends, identify inefficiencies, and help optimize future transportation strategies. Data-driven decision-making ensures your supply chain remains efficient and cost-effective.", "managed-reporting.jpg", "Team reviewing performance reports"),
    ("Continuous Improvement", "Logistics is an evolving process, and we are committed to continuous improvement. By leveraging analytics and industry best practices, we refine transportation strategies, negotiate better carrier rates, and implement process enhancements. Our goal is to adapt to changing business needs and keep your supply chain running smoothly with long-term cost savings and efficiency.", "managed-tracking.jpg", "Refining logistics processes"),
]
steps_html = "".join(
    f'<div class="step"><div class="step-text"><h3>{t}</h3><p>{d}</p></div><div class="step-img"><img src="assets/img/{img}" alt="{alt}" loading="lazy"></div></div>'
    for t, d, img, alt in steps)
pages["managed-transportation.html"] = head("Managed transportation — GTR Freight", "Take control of your supply chain without the hassle of managing logistics in-house.") \
    + header("shippers") \
    + hero("Managed transportation", "Take control of your supply chain without the hassle of managing logistics in-house.", "hero-managed.jpg") \
    + f"""<section class="approach">
  <div class="container">
    <div class="section-head">
      <h2 class="section-title">Our <span class="accent">approach</span></h2>
      <p class="section-lead">We take a strategic, data-driven approach to freight management, ensuring efficiency, cost savings, and reliability.</p>
    </div>
    <div class="timeline"><span class="timeline-dot"></span>{steps_html}</div>
  </div>
</section>
""" + testimonials() + cta("Ready to move forward?", "Get in touch", "contacts.html#form") + FOOTER

# ---------------- WAREHOUSING ----------------
wh_cards = [
    ("Pick &amp; Pack", "Fast, accurate order picking and packaging to ensure seamless fulfillment.", ""),
    ("Order Consolidation", "Combine multiple shipments to reduce costs and improve delivery efficiency.", " card--active"),
    ("Cross-Docking", "Reduce storage time by moving shipments from inbound to outbound transport.", ""),
    ("Kitting &amp; Sequencing", "Pre-assemble product kits or arrange parts in precise sequences.", ""),
    ("Inbound &amp; Outbound Logistics", "Streamlined freight management for receiving, storing, and shipping goods.", ""),
    ("Returns Management", "Efficient handling of product returns to maintain inventory accuracy.", ""),
]
wh_html = "".join(f'<article class="card{c}"><h3>{t}</h3><p>{d}</p></article>' for t, d, c in wh_cards)
pages["warehousing.html"] = head("Warehousing and Fulfillment — GTR Freight", "Streamline your supply chain with Warehousing and Fulfillment solutions designed to optimize storage, inventory management, and order processing.") \
    + header("shippers") \
    + hero("Warehousing and Fulfillment", "Streamline your supply chain with our Warehousing and Fulfillment solutions, designed to optimize storage, inventory management, and order processing.", "hero-warehousing.jpg") \
    + f"""<section class="intro">
  <div class="container">
    <div class="intro-grid">
      <div>
        <h2>Efficient warehousing and fulfillment are key to a smooth supply chain and satisfied customers</h2>
        <p>Our Warehousing &amp; Fulfillment services provide secure storage, real-time inventory management, and seamless order processing to keep your business running efficiently. Whether you need short-term storage, e-commerce fulfillment, or large-scale distribution, we offer tailored solutions designed to reduce costs, improve accuracy, and speed up delivery times. With advanced technology and a network of strategic warehouse locations, we handle everything from receiving and storage to picking, packing, and shipping—so you can focus on growing your business.</p>
      </div>
      <img src="assets/img/warehouse-worker.jpg" alt="Warehouse worker checking inventory beside stacked pallets" width="512" height="288" loading="lazy">
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="services-head"><h2 class="section-title">Comprehensive <span class="accent">warehousing solutions</span></h2></div>
    <div class="cards cards-3">{wh_html}</div>
  </div>
</section>
""" + testimonials() + cta("Ready to move forward?", "Get in touch", "contacts.html#form") + FOOTER

# ---------------- CROSS-BORDER ----------------
cb_cards = [
    ("Customs clearance", "Fast and efficient processing of duties, tariffs, and compliance requirements."),
    ("Documentation management", "Accurate paperwork to prevent delays and ensure smooth border crossings."),
    ("Carrier coordination", "Reliable transportation by road, air, or ocean to meet your shipping needs."),
    ("Duty &amp; Tax Optimization", "Minimize costs with expert guidance on trade regulations and tax strategies."),
    ("Real-Time tracking", "Full visibility of your shipment with updates at every stage."),
    ("Risk Management", "Compliance with international trade laws to ensure secure, hassle-free shipping."),
]
cb_html = "".join(f'<article class="card"><h3>{t}</h3><p>{d}</p></article>' for t, d in cb_cards)
pages["cross-border.html"] = head("Cross-Border Logistics — GTR Freight", "Seamlessly move your freight across international borders with GTR Freight's Cross-Border Logistics solutions.") \
    + header("shippers") \
    + hero("Cross-Border Logistics", "Seamlessly move your freight across international borders with our Cross-Border Logistics solutions.", "hero-crossborder.jpg") \
    + f"""<section class="intro">
  <div class="container">
    <div class="intro-grid">
      <div>
        <h2>Shipping across international borders can be complex, but we make it simple, fast, and hassle-free.</h2>
        <p>Our Cross-Border Logistics services ensure smooth transportation by handling customs clearance, documentation, compliance, and carrier coordination for you. Whether you’re shipping between the U.S., Canada, Mexico, or globally, we optimize routes, reduce transit times, and minimize costs. With real-time tracking, expert customs management, and a trusted carrier network, we help your freight move seamlessly across borders—so you can focus on growing your business.</p>
      </div>
      <img src="assets/img/border-crossing.jpg" alt="Trucks passing through a border crossing" width="360" height="203" loading="lazy">
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="services-head"><h2 class="section-title">End-to-end <span class="accent">cross-border solutions</span></h2></div>
    <div class="cards cards-3">{cb_html}</div>
  </div>
</section>
""" + testimonials() + cta("Ready to move forward?", "Get in touch", "contacts.html#form") + FOOTER

# ---------------- CONTACTS ----------------
contact_form = f"""<form class="form-card" id="form" data-static action="#" method="post" novalidate>
  <div class="form-grid">
    {field("Full name", "name", "Your full name")}
    {select_field("Choose logistics service", "service", SERVICES_LIST)}
    {field("Email", "email", "example@gmail.com", "email")}
    {phone_field()}
    <div class="field full"><label for="message">Message</label><textarea id="message" name="message" placeholder="Leave us a message..." required></textarea></div>
  </div>
  <label class="check"><input type="checkbox" name="privacy" required> You agree to our friendly privacy policy</label>
  <button class="btn btn-primary btn-block btn-lg" type="submit">Send Message</button>
  <p class="form-note" role="status">Thanks! Your message has been received. We’ll get back to you shortly.</p>
</form>"""
pages["contacts.html"] = head("Contacts — GTR Freight", "Reach out to GTR Freight for a personalized quote, consultation, or more information on how we can streamline your supply chain.") \
    + header("contacts") \
    + hero("Contacts", "Reach out to us today for a personalized quote, consultation, or more information on how we can streamline your supply chain.", "hero-carrier.jpg") \
    + f"""<section class="contact-wrap">
  <div class="container">
    <div class="section-head" style="margin-bottom:0">
      <h2 class="section-title">We’d love to <span class="accent">hear from you</span></h2>
      <p class="section-lead">If you have any inquiries or need support regarding our services, please fill out the form on this page or use the email address and phone number provided to contact us directly.</p>
    </div>
    <div class="contact-grid">
      {contact_form}
      {info_cards("info@gtrfreight.com")}
    </div>
  </div>
</section>
""" + cta("Ready for less risk &amp; More Savings?", "Get in touch", "#form") + FOOTER

# ---------------- SHIP INTERNATIONAL ----------------
intl_form = f"""<form class="form-card" id="form" data-static action="#" method="post" novalidate>
  <div class="form-grid">
    {field("First name", "first_name", "Your first name")}
    {field("Last name", "last_name", "Your last name")}
    {field("Email", "email", "example@gmail.com", "email")}
    {phone_field()}
    <div class="field full"><label for="requirements">Special requirement</label><textarea id="requirements" name="requirements" placeholder="Any special requirements?"></textarea></div>
  </div>
  <label class="check"><input type="checkbox" name="privacy" required> You agree to our friendly privacy policy</label>
  <button class="btn btn-primary btn-block btn-lg" type="submit">Get a quote</button>
  <p class="form-note" role="status">Thanks! Your request has been received. Our international team will be in touch shortly.</p>
</form>"""
pages["ship-international.html"] = head("Ship international — GTR Freight", "With 20+ strategically situated facilities across North America and a dedicated team of international shipping experts, GTR Freight has you covered.") \
    + header("shippers") \
    + hero("Ship international", "Move your freight across borders and oceans with GTR Freight’s international shipping network and dedicated logistics experts.", "hero-ship-intl.jpg") \
    + f"""<section class="contact-wrap">
  <div class="container">
    <div class="section-head" style="margin-bottom:0">
      <h2 class="section-title">Seamless <span class="accent">international shipping</span></h2>
      <p class="section-lead">With 20+ strategically situated facilities across North America and a dedicated team of International Shipping logistics experts, GTR Freight has you covered.</p>
    </div>
    <div class="contact-grid">
      {intl_form}
      {info_cards("international@gtrfreight.com")}
    </div>
  </div>
</section>
""" + cta("Ready for less risk &amp; More Savings?", "Get in touch", "contacts.html#form") + FOOTER

# ---------------- BECOME A SHIPPER ----------------
countries = ["United states", "Canada", "Mexico"]
shipper_form = f"""<form class="shipper-form" data-static action="#" method="post" novalidate>
  <div class="shipper-grid">
    <div>
      <h2>Company Information</h2>
      <div class="form-card">
        <div class="form-grid">
          {field("Company name", "company", "Your company name", cls="full")}
          {field("Address", "company_address", "Company address", cls="full")}
          {field("Zip code", "company_zip", "Zip")}
          {select_field("Choose country", "company_country", countries)}
          {field("Website", "website", "Website url", "url", cls="full", required=False)}
        </div>
      </div>
    </div>
    <div>
      <h2>Accounts payable information</h2>
      <div class="form-card">
        <div class="form-grid">
          {field("Address", "ap_address", "Address", cls="full")}
          {field("Zip code", "ap_zip", "Zip")}
          {select_field("Choose country", "ap_country", countries)}
          {field("Name", "ap_name", "Name", cls="full")}
          {field("Email", "ap_email", "Email", "email")}
          {field("Phone", "ap_phone", "Phone number", "tel")}
        </div>
      </div>
    </div>
    <div>
      <h2>Contact information</h2>
      <div class="form-card">
        <div class="form-grid">
          {field("Name", "contact_name", "Your name", cls="full")}
          {field("Email", "contact_email", "Email address", "email")}
          {field("Phone", "contact_phone", "Your phone number", "tel")}
        </div>
      </div>
    </div>
    <div>
      <h2>Alternate contact</h2>
      <div class="form-card">
        <div class="form-grid">
          {field("Name", "alt_name", "Your name", cls="full", required=False)}
          {field("Email", "alt_email", "Email address", "email", required=False)}
          {field("Phone", "alt_phone", "Your phone number", "tel", required=False)}
        </div>
      </div>
    </div>
  </div>
  <div class="payment">
    <h2 style="margin-top:40px">Payment information</h2>
    <div class="radio-group">
      <h3>Will you accept an email or scanned copy of billing?</h3>
      <label><input type="radio" name="billing_copy" value="yes" checked> Yes, an email or scanned copy is acceptable</label>
      <label><input type="radio" name="billing_copy" value="no"> No, an email or scanned copy is NOT acceptable</label>
      <h3>Will you require the original Proof of Delivery?</h3>
      <label><input type="radio" name="pod" value="yes" checked> Yes, original Proof of Delivery is required</label>
      <label><input type="radio" name="pod" value="no"> No, original Proof of Delivery is NOT required</label>
      <h3>Preferred invoicing method</h3>
      <label><input type="radio" name="invoicing" value="email" checked> Email</label>
      <label><input type="radio" name="invoicing" value="fax"> Fax</label>
    </div>
    {select_field("Service required", "service", SERVICES_LIST)}
  </div>
  <div class="submit form-card" style="background:none;padding:0">
    <button class="btn btn-primary btn-block btn-lg" type="submit">Become a shipper</button>
    <p class="form-note" role="status">Thanks! Your shipper application has been received. We’ll be in touch shortly.</p>
  </div>
</form>"""
pages["become-shipper.html"] = head("Become a shipper — GTR Freight", "Partner with GTR Freight for hassle-free freight management, flexible shipping options, and dedicated customer support.") \
    + header("shippers") \
    + hero("Become a shipper", "Partner with us for hassle-free freight management, flexible shipping options, and dedicated customer support.", "hero-carrier.jpg") \
    + f"""<section class="shipper">
  <div class="container">{shipper_form}</div>
</section>
""" + cta("Ready for less risk &amp; More Savings?", "Get in touch", "contacts.html#form") + FOOTER

# ---------------- write ----------------
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, len(html))

with open(os.path.join(OUT, "favicon.svg"), "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#254be0"/>'
            '<text x="32" y="44" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" font-weight="700" font-size="36" fill="#fff">G</text></svg>')
print("wrote favicon.svg")
