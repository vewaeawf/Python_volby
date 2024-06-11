# Projekt 3 - Scraper volebních výsledků z roku 2017

## Popis
Tento projekt obsahuje scraper, který stahuje volební výsledky z roku 2017 pro zvolený územní celek a ukládá je do CSV souboru.

## Instalace
1. Vytvořte a aktivujte virtuální prostředí:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Na Windows použijte `venv\Scripts\activate`
    ```
2. Nainstalujte potřebné knihovny:
    a) Nejprve vytvořte nový textový soubor `requirements.txt` a vložte do něj následující řádky:
    ```plaintext
    requests==2.26.0
    beautifulsoup4==4.10.0
    ```
    b) Poté nainstalujte knihovny pomocí příkazu:
    ```bash
    pip install -r requirements.txt
    ```

## Použití
1. Vytvořte Python skript pro scraping dat a uložení do CSV. Například, vytvořte soubor `projekt_3.py`

2. Spusťte skript s následujícími argumenty:
    ```bash
    python projekt_3.py <libovolné_URL> <output_file>
    ```
## Ukázka
Příklad spuštění skriptu pro oblast Benešov:
```bash
python projekt_3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_benesov.csv"
