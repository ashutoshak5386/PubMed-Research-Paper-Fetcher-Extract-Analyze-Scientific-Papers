# PubMed Research Paper Fetcher

## Overview

This Python application fetches research papers from PubMed based on a user-defined query. It identifies papers with at least one author affiliated with a pharmaceutical or biotech company and outputs the results as a CSV file.

## Features

- Fetches research papers using the **PubMed API**
- Filters papers that include at least one **non-academic author** (from pharmaceutical or biotech companies)
- Extracts **corresponding author emails**
- Supports **command-line options** for queries, output files, and debug mode
- Saves results to a **CSV file** or prints them to the console
- Uses **Poetry** for dependency management

---

## Installation

### Prerequisites

- Python **3.8+**
- Poetry (**recommended for dependency management**)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/pubmed-fetcher.git
   cd pubmed-fetcher
   ```
2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```
3. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

---

## Usage

### Command-line Arguments

```bash
python get_papers_list.py "your query here" -f output.csv -d
```

| Option        | Description                                          |
| ------------- | ---------------------------------------------------- |
| `query`       | Search query for PubMed (supports full query syntax) |
| `-f, --file`  | Output CSV file name (optional)                      |
| `-d, --debug` | Enable debug mode (optional)                         |
| `-h, --help`  | Display help message                                 |

### Example Usage

Fetch research papers related to **"cancer treatment"** and save them to `results.csv`:

```bash
python get_papers_list.py "cancer treatment" -f results.csv
```

Fetch and print results to console:

```bash
python get_papers_list.py "AI in healthcare"
```

Enable debug mode:

```bash
python get_papers_list.py "biotechnology research" -d
```

---

## Project Structure

```
📂 pubmed-fetcher
│── 📄 get_papers_list.py    # Main script
│── 📄 pubmed_module.py      # Module for fetching and processing papers
│── 📄 pyproject.toml        # Poetry configuration file
│── 📄 README.md             # Documentation
│── 📄 .gitignore            # Ignore unnecessary files
```

---

## API Details

The script uses **NCBI's PubMed API**:

- **Search Papers:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`
- **Fetch Details:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi`

For more details, check [NCBI API Documentation](https://www.ncbi.nlm.nih.gov/books/NBK25499/).

---

## Publishing as a Python Package (Bonus)

To publish the module on **TestPyPI**:

```bash
poetry build
poetry publish -r testpypi
```

To install from **TestPyPI**:

```bash
pip install --index-url https://test.pypi.org/simple/ pubmed-fetcher
```

---

## Tools & Technologies Used

- **Python 3.8+**
- **Poetry** for dependency management
- **Requests** for API calls
- **CSV** for file handling
- **Argparse** for command-line support
- **Git & GitHub** for version control

---

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit changes and push to GitHub.
4. Submit a pull request.

---

## License

This project is licensed under the **MIT License**.

---

## Contact

For any questions, reach out via GitHub Issues or email at [[ashutoshak5386@gmail.com](mailto\:ashutoshak5386@gmail.com)].

