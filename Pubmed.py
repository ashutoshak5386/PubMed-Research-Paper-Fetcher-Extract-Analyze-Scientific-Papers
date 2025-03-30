import requests
import csv
import argparse
import re
from typing import List, Dict, Optional

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query: str) -> List[Dict]:
    """Fetches PubMed papers based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10,
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception("Error fetching PubMed data")
    
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetches details of PubMed papers."""
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json",
    }
    response = requests.get(FETCH_URL, params=params)
    if response.status_code != 200:
        raise Exception("Error fetching PubMed details")
    
    papers = response.json().get("result", {})
    return process_papers(papers)

def process_papers(papers: Dict) -> List[Dict]:
    """Extracts required fields from PubMed response."""
    results = []
    for pid, paper in papers.items():
        if not isinstance(paper, dict) or "title" not in paper:
            continue
        
        title = paper.get("title", "")
        pub_date = paper.get("pubdate", "")
        authors = paper.get("authors", [])
        
        non_academic_authors, company_affiliations = filter_non_academic_authors(authors)
        corresponding_email = extract_email(paper.get("source", ""))
        
        results.append({
            "PubmedID": pid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email,
        })
    return results

def filter_non_academic_authors(authors: List[Dict]) -> (List[str], List[str]):
    """Identifies non-academic authors based on affiliations."""
    company_keywords = ["Pharma", "Biotech", "Inc.", "Ltd.", "Corporation"]
    non_academic = []
    companies = []
    
    for author in authors:
        name = author.get("name", "")
        affiliation = author.get("affiliation", "")
        if any(keyword in affiliation for keyword in company_keywords):
            non_academic.append(name)
            companies.append(affiliation)
    
    return non_academic, companies

def extract_email(text: str) -> Optional[str]:
    """Extracts an email address from text."""
    match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return match.group(0) if match else None

def save_to_csv(results: List[Dict], filename: str):
    """Saves results to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="PubMed query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    
    results = fetch_pubmed_papers(args.query)
    if args.file:
        save_to_csv(results, args.file)
        print(f"Results saved to {args.file}")
    else:
        print(results)

if __name__ == "__main__":
    import sys
    sys.argv = ["script_name", "your query here", "-f", "output.csv"]  # Replace with actual query and filename
    main()

