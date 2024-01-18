import pandas as pd
import requests
import logging


def valid_sequence(sequence: str) -> bool:
    valid_amino_acids = "SNYLRQDPMFCEWGTKIVAH"
    return all(char in valid_amino_acids for char in sequence)


def check_protein_sequence(item: str) -> None | list[str]:
    chunks = item.split()

    head = " ".join(chunks[:-1])
    sequence = chunks[-1]

    if valid_sequence(sequence):
        return [head, sequence]


def main():
    input_csv = input()
    output_file = input()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=f"{output_file}.log",
    )

    df = pd.read_csv(input_csv)

    protein_names = []
    chain_heads = []
    sequences = []

    for id_ in df["ID"].tolist():
        url = f"https://www.rcsb.org/fasta/entry/{id_}/display"

        response = requests.get(url)

        if response.status_code == 200:
            fasta = response.text

            fasta_data = fasta.split(">")[1:]

            protein_fasta = []
            for item in fasta_data:
                output = check_protein_sequence(item)
                if output is not None:
                    protein_fasta.extend(output)

            for i in range(1, len(protein_fasta), 2):
                protein_names.append(id_)
                chain_heads.append(protein_fasta[i - 1])
                sequences.append(protein_fasta[i])

        logging.info(f"{id_} - processed")

    df = pd.DataFrame({'protein_names': protein_names, 'chain_heads': chain_heads, 'sequences': sequences})
    df.to_csv(output_file + ".csv", index=False)


if __name__ == '__main__':
    main()
