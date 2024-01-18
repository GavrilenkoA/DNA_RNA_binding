import requests
import re
import pandas as pd
import logging
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=f"parse_fasta_rcsb.log",
)


def make_request_fasta(entry, chain):
    url = f"https://www.rcsb.org/fasta/entry/{entry}/display"
    response = requests.get(url)
    if response.status_code == 200:
        fasta = response.text
        chunks = fasta.split(">")[1:]
        for item in chunks:
            match = pattern.search(item)
            chains = match.group(1)
            if chain in chains:
                seq = item.split("\n")[-2]
                sequences.append(seq)
                break
        return "found"
    elif response.status_code == 404:
        return "not_found"


def parse_fasta(df):
    for id_ in df["identifier"].to_list():
        entry = id_[:-1]
        chain = id_[-1]

        answer = make_request_fasta(entry, chain)

        if answer == "not_found":
            url = f"https://www.rcsb.org/structure/{entry}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            all_paragraphs = soup.div.find_all("li")

            for paragraph in all_paragraphs:
                if "It has been replaced (superseded) by" in paragraph.text:
                    new_entry = paragraph.text.split()[-1].replace(".", "")
                    make_request_fasta(new_entry, chain)
                    break


pattern = re.compile(r'\|(Chain.*?)\|')
sequences = []
input_csv = input()


def main():
    df = pd.read_csv(input_csv)
    parse_fasta(df)
    logging.info(f"{len(sequences)} - count sequences")
    df.loc[:, "sequence"] = sequences
    df.to_csv(input_csv, index=False)


if __name__ == "__main__":
    main()
