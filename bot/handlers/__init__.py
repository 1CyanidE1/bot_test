from . import start, lang_changer, links, whois


user_handlers = [
    start.router,
    lang_changer.router,
    links.router,
    whois.router,
]
