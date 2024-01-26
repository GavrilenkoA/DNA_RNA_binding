import pandas as pd
from utils import process_csv, write_fasta, add_clusters
import subprocess


SEED = 42


df_biolip = pd.read_csv("../data/biolip/dna_binders_biolip.csv")


df = process_csv("../data/DBP_papers_data/train-17151+50000-unbalance.csv")
df = df.drop_duplicates(subset=["sequence"])
df = df[df.class_binder == 0]
df = df.sample(n=len(df_biolip), random_state=SEED)


df = pd.concat([df_biolip, df])

# Prepare fasta before clustering
write_fasta(df, "biolip.fasta")

# Clustering
fasta_input = "../data/fasta/biolip.fasta"
output_dir = "../data/clusters/biolip"

subprocess.run(f"mmseqs easy-cluster {fasta_input} {output_dir} tmp --min-seq-id 0.5 -c 0.6 --cov-mode 0", shell=True)

# Prepare df with clusters before merge
output_mmseqs = pd.read_csv("../data/clusters/biolip_cluster.tsv", sep="\t", header=None)
output_mmseqs = add_clusters(output_mmseqs)
output_mmseqs = output_mmseqs.loc[:, ["identifier", "clusters"]]


output_df = df.merge(output_mmseqs, on="identifier")
assert len(output_df) == len(df)
output_df.to_csv("../data/output_df.csv", index=False)





