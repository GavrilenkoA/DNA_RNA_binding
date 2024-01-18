import pandas as pd


def parse_txt(input_txt, source_name, output_csv):
    pdb_ids = []
    seqs = []

    with open(input_txt) as f:
        for line in f:
            line = line.strip()
            if line:
                line_data = line.split("\t")

                pdb_ids.append("".join(line_data[0:2]))
                seqs.append(line_data[-1])

    class_binders = [1] * len(pdb_ids)
    sources = [source_name] * len(pdb_ids)

    df = pd.DataFrame({"identifier": pdb_ids, "class_binder": class_binders, "sequence": seqs, "source": sources})
    df.to_csv(output_csv, index=False)


input_txt = input()
source_name = input()
output_csv = input()

if __name__ == "__main__":
    parse_txt(input_txt, source_name, output_csv)
