import csv
from src.utils.scraper import scraper
import os
import dotenv

dotenv.load_dotenv()

if __name__ == "__main__":
    csv_path = os.path.join('output', 'lotto.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'title', 'first_prize', 'front_three', 'back_three', 'back_two']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(22):
            results = scraper(os.getenv("URL"), i + 1)
            for result in results:
                result_copy = result.copy()
                result_copy['front_three'] = ','.join(result_copy['front_three'])
                result_copy['back_three'] = ','.join(result_copy['back_three'])
                writer.writerow(result_copy)

