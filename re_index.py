import datetime

import tqdm
from datasets import load_dataset
from floatdb import generate_hash

from db.connection import StringVec, DB
from model import StringToVec


class IndexFromFile:
    def __init__(self):
        self.model = StringToVec()
        DB()
        self.dataset = load_dataset("ag_news", split="train")

    def process_start(self):

        all_title = list()
        all_ids = list()
        for index, paper in tqdm.tqdm(enumerate(self.dataset)):
            all_title.append(paper.get("text"))
            all_ids.append(index)
        print("here")
        all_vec = self.model.get_vector_batch(all_title)
        print("hello 2")
        all_hash = []
        for i in tqdm.tqdm(all_vec):
            all_hash.append(generate_hash(i))

        for j in tqdm.tqdm(zip(all_title, all_vec, all_hash, all_ids)):
            StringVec.create(
                string_val=j[0],
                embedding=j[1],
                hash_of_embedding=j[2],
                created_at=datetime.datetime.now(),
                id=j[3]
            )


if __name__ == "__main__":
    obj = IndexFromFile()
    obj.process_start()
