"""
projekt_3.py: third project  
author: Vitalie Platon 
email: vitalieplaton@gmail.com
discord: Asterdo#0059
"""
 
import requests
from bs4 import BeautifulSoup
import csv
import sys
 
def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text
 
def parse_district_links(base_url, html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('td.cislo a')
    return [base_url + link['href'] for link in links]
 
def parse_voting_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select('table tr')
    header = ["kod_obce", "nazev_obce", "volici_v_seznamu", "vydane_obalky", "platne_hlasy"]
    parties = [party.text for party in rows[1].select('td')[2:]]
    header.extend(parties)
 
    results = []
    for row in rows[2:]:
        cols = row.select('td')
        if not cols:
            continue
        code = cols[0].text.strip()
        name = cols[1].text.strip()
        voters = cols[2].text.strip().replace('\xa0', '')
        envelopes = cols[3].text.strip().replace('\xa0', '')
        valid_votes = cols[4].text.strip().replace('\xa0', '')
        party_votes = [col.text.strip().replace('\xa0', '') for col in cols[5:]]
        results.append([code, name, voters, envelopes, valid_votes] + party_votes)
 
    return header, results
 
def save_to_csv(header, data, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
 
def main():
    if len(sys.argv) != 3:
        print("Usage: python projekt_3.py <url> <output_file>")
        sys.exit(1)
 
    url = sys.argv[1]
    output_file = sys.argv[2]
 
    try:
        base_url = url.rsplit('/', 1)[0] + '/'
        html = fetch_html(url)
        district_links = parse_district_links(base_url, html)
 
        all_results = []
        header = None
        for link in district_links:
            district_html = fetch_html(link)
            header, results = parse_voting_results(district_html)
            all_results.extend(results)
 
        save_to_csv(header, all_results, output_file)
        print(f"Data saved to {output_file}")
 
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
 
if __name__ == "__main__":
    main()
