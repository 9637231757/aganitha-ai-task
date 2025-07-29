# filter.py

from typing import List, Dict


def is_company_affiliation(affiliation: str) -> bool:
    """Check if affiliation looks like a company."""
    if not affiliation:
        return False
    keywords = ["Inc", "Ltd", "LLC", "Corporation", "Company", "Biotech", "Pharma"]
    return any(word.lower() in affiliation.lower() for word in keywords)


def filter_company_authors(papers: List[Dict]) -> List[Dict]:
    """Return only authors with company affiliation from each paper."""
    results = []
    for paper in papers:
        # Safely get authors list
        authors = paper.get("authors", [])
        company_authors = [
            a for a in authors
            if a.get("affiliation") and is_company_affiliation(a["affiliation"])
        ]
        if company_authors:
            results.append({
                "pmid": paper.get("pmid", ""),
                "title": paper.get("title", ""),
                "pubdate": paper.get("pubdate", ""),
                "company_authors": company_authors
            })
    return results
