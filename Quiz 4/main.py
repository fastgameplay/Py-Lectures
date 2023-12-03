import csv,time,re,os,requests,random
from bs4 import BeautifulSoup

def validate(tag):
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z-]*[a-zA-Z]$')
    return bool(pattern.match(tag))

def scrape_quotes(tag):
    url = f'http://quotes.toscrape.com/tag/{tag}'
    quotes = []

    page_number = 1
    while True:
        response = requests.get(f'{url}/page/{page_number}')
        soup = BeautifulSoup(response.text, 'html.parser')

        quote_elements = soup.find_all('span', class_='text')
        author_elements = soup.find_all('small', class_='author')

        if not quote_elements:
            break  # No more quotes

        for quote, author in zip(quote_elements, author_elements):
            quotes.append({'quote': quote.get_text(), 'author': author.get_text()})

        print(f'Page {page_number} scraped successfully.')

        next_button = soup.find('li', class_='next')
        if not next_button:
            print("\n")
            break  # No more pages

        page_number += 1
        sleep_interval = random.uniform(40, 50) # მინი ანტი ბოტუნია
        print(f'💤(｡-‿-｡)💤 \n Sleeping For {sleep_interval:.2f} seconds...')
        time.sleep(sleep_interval)

    return quotes

def save_to_csv(tag, quotes):
    folder_name = 'Quotes'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    filename = f'{folder_name}/{tag}_quotes.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['quote', 'author']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for quote in quotes:
            writer.writerow(quote)

    print(f'CSV file successfully created: {filename}')

def main():
    user_tag = input('Enter the desired tag: ').strip()

    if not validate(user_tag):
        print('Invalid tag. Tag must start and end with a letter and can only contain letters and dashes.')
        return

    quotes = scrape_quotes(user_tag)

    if not quotes:
        print(f'No quotes were found for the tag: {user_tag}')
        return

    save_to_csv(user_tag, quotes)

if __name__ == '__main__':
    main()