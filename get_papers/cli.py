import argparse
import csv
from get_papers.fetch import search_pubmed, fetch_details
from get_papers.filter import filter_company_authors

def main():
    # Command-line arguments
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma/biotech authors")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="CSV output filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    if args.debug:
        print(f"Searching for: {args.query}")

    # Fetch IDs
    ids = search_pubmed(args.query)
    if args.debug:
        print(f"Found {len(ids)} IDs: {ids}")

    # Fetch paper details
    papers = fetch_details(ids)

    # Filter for company authors
    results = filter_company_authors(papers)

    # Save or print results
    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                "PubmedID", "Title", "PublicationDate",
                "NonAcademicAuthors", "CompanyAffiliations", "CorrespondingEmail"
            ])
            writer.writeheader()
            for r in results:
                writer.writerow(r)
        print(f"Results saved to {args.file}")
    else:
        for r in results:
            print(r)

if __name__ == "__main__":
    main()
