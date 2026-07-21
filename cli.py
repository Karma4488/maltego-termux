from core.entities import Person, Domain
from core.transforms import whois_lookup, dns_lookup, google_search
from core.graph import create_graph, visualize_graph

def main():
    # Example: Create entities
    person = Person("John Doe")
    domain = Domain("example.com")

    # Example: Run transforms
    whois_info = whois_lookup(domain.value)
    dns_info = dns_lookup(domain.value)
    search_results = google_search(f"John Doe site:linkedin.com")

    # Add properties
    domain.add_property("WHOIS", str(whois_info))
    domain.add_property("DNS", str(dns_info))
    person.add_property("LinkedIn", str(search_results))

    # Create relationships
    relationships = [
        (person, domain, "owns"),
    ]

    # Create and visualize graph
    entities = [person, domain]
    G = create_graph(entities, relationships)
    visualize_graph(G)

if __name__ == "__main__":
    main()
