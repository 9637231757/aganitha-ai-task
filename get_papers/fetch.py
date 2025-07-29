import requests
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    """Fetch papers using combined search + summary fetch"""
    search_url = f"{BASE_URL}esearch.fcgi?db=pubmed&term={query}&retmode=json"
    if debug:
        print(f"Fetching: {search_url}")
    res = requests.get(search_url)
    res.raise_for_status()
    ids = res.json()["esearchresult"]["idlist"]

    papers = []
    for pmid in ids:
        summary_url = f"{BASE_URL}esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
        if debug:
            print(f"Fetching summary: {summary_url}")
        summary = requests.get(summary_url).json()
        paper_data = summary["result"][pmid]
        papers.append({
            "pmid": pmid,
            "title": paper_data.get("title", ""),
            "pubdate": paper_data.get("pubdate", ""),
            "authors": paper_data.get("authors", []),
        })
    return papers


def search_pubmed(query: str, debug: bool = False) -> List[str]:
    """Only search PubMed and return list of PMIDs"""
    search_url = f"{BASE_URL}esearch.fcgi?db=pubmed&term={query}&retmode=json"
    if debug:
        print(f"Fetching search results: {search_url}")
    res = requests.get(search_url)
    res.raise_for_status()
    return res.json()["esearchresult"]["idlist"]


def fetch_details(pmids: List[str], debug: bool = False) -> List[Dict]:
    """Fetch detailed info for a given list of PMIDs"""
    papers = []
    for pmid in pmids:
        summary_url = f"{BASE_URL}esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
        if debug:
            print(f"Fetching summary: {summary_url}")
        summary = requests.get(summary_url).json()
        paper_data = summary["result"][pmid]
        papers.append({
            "pmid": pmid,
            "title": paper_data.get("title", ""),
            "pubdate": paper_data.get("pubdate", ""),
            "authors": paper_data.get("authors", []),
        })
    return papers
