# Thai Lottery Scraping Project
<img />
This project is a web scraper designed to collect Thai lottery results from a specified website. It uses Selenium with Microsoft Edge WebDriver to automate the data collection process and saves the results in a CSV format.

## Features

- Automated scraping of Thai lottery results
- Collects multiple types of lottery numbers:
  - First prize numbers
  - Front three digits
  - Back three digits
  - Back two digits
- Saves results in CSV format with dates and draw titles
- Headless browser operation for efficient scraping

## Prerequisites

- Python 3.x
- Microsoft Edge browser
- Edge WebDriver

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
cd thai-lotto-scraping
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your target URL:
```
URL=your_target_url_here
```

## Project Structure

```
thai-lotto-scraping/
├── main.py              # Main script to run the scraper
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
├── output/             # Directory for output files
│   └── lotto.csv      # Generated CSV file with results
└── src/
    └── utils/
        └── scraper.py  # Scraper implementation
```

## Usage

Run the main script:
```bash
python main.py
```

The script will:
1. Initialize a headless Edge browser
2. Navigate through multiple pages of lottery results
3. Extract lottery numbers and related information
4. Save the results to `output/lotto.csv`

## Output Format

The generated CSV file contains the following columns:
- `date`: Date of the lottery draw
- `title`: Title of the lottery draw
- `first_prize`: First prize winning number
- `front_three`: Front three digits winning numbers
- `back_three`: Back three digits winning numbers
- `back_two`: Back two digits winning number

## Notes

- The scraper uses headless browser mode for better performance
- Error handling is implemented to ensure continuous operation
- The script processes 22 pages of lottery results by default
