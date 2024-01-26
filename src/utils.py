import pandas as pd


def process_csv(path_csv):
    df = pd.read_csv(path_csv, header=None)

    new_column_names = {0: "identifier", 1: "sequence", 2: "class_binder"}
    df = df.rename(columns=new_column_names)

    def process_id(x):
        if len(x) > 5:
            id_ = x.split("|")[1]
            return id_
        else:
            return x

    df["identifier"] = df["identifier"].apply(process_id)
    return df


def write_fasta(df, name_file: str) -> None:
    def pull_data(x):
        id_ = x["identifier"]
        seq = x["sequence"]
        return id_, seq

    data = df.apply(lambda x: pull_data(x), axis=1).tolist()

    with open(f"../data/fasta/{name_file}", "w") as file:
        for item in data:
            file.write(">" + f"{item[0]}")
            file.write("\n")
            file.write(f"{item[1]}")
            file.write("\n")


def add_clusters(df):
    df.columns = ["repr", "identifier"]

    reprs = df["repr"].to_list()
    clusters = []
    count = 0
    name = ""
    for item in reprs:
        if item != name:
            count += 1
            name = item
        clusters.append(count)

    df["clusters"] = clusters
    return df