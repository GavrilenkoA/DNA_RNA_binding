import logging
import ankh
import numpy as np
import torch
import pandas as pd
import pickle


def save_picle(obj, filename):
    filename = "../data/" + filename + ".pkl"
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def calculate_embed(seq: str) -> np.ndarray:
    model.to(torch.device("cuda"))

    # Encode the sequence using the tokenizer
    with torch.no_grad():
        inputs = tokenizer(
            [seq],
            add_special_tokens=False,
            padding=False,
            is_split_into_words=True,
            return_tensors="pt"
        )
        inputs.to(torch.device("cuda"))

        embeddings = model(**inputs)

    # Move the embeddings back to CPU before converting to numpy array
    embed = embeddings.last_hidden_state.mean(axis=1).view(-1).cpu().numpy()

    return embed


def process_data(csv_input: str, name_data: str) -> None:
    def pull_data(x):
        id_ = x["identifier"]
        seq = x["sequence"]
        return id_, seq

    input_df = pd.read_csv(csv_input)
    data = input_df.apply(lambda x: pull_data(x), axis=1).tolist()
    outputs = {}

    for item in data:
        id_, seq = item
        embed = calculate_embed(seq)
        outputs[id_] = embed
        logging.info(f"{id_} - ok")

    save_picle(outputs, name_data)


if __name__ == "__main__":
    csv_input = input()
    name_data = input()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=f"{name_data}.log",
    )

    model, tokenizer = ankh.load_large_model()
    model.eval()

    process_data(csv_input, name_data)
