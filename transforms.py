import whois
import dns.resolver
import requests
from bs4 import BeautifulSoup

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"WHOIS lookup failed: {e}"

def dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [str(r) for r in answers]
    except Exception as e:
        return f"DNS lookup failed: {e}"

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True) if "http" in a["href"]]
    return links[:5]  # Return top 5 links
