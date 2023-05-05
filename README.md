# Password Scraper

This is a Python script that scrapes passwords from a combolist file and writes them to a result file.

## Modules Used

This script uses the following Python modules:

- os
- sys
- tqdm

## Getting Started

### Prerequisites

This script requires Python 3 and the `tqdm` module to display a progress bar. You can install the `tqdm` module using `pip`.

 - You need a valid combolist : `email:password`

```bash
pip install tqdm
```

### Usage
```bash
python3 bot.py ./combolist/combo.txt
```

### Output

The passwords scraped from the combolist file will be written to a file named `final.txt` in the results directory.
