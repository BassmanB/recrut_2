import pandas as pd
from glob import glob
from os import path


class FileParser:

    def __init__(self, src="sources"):
        self.src_dir = src
        self.full_paths = []

    def get_files_names(self):
        for src in glob(self.src_dir + "/*/*", recursive=True):
            if path.isfile(src):
                self.full_paths.append(src)

    @staticmethod
    def read_data(file):
        try:
            print(f"Read the {file} source")
            df = pd.read_csv(file)
            print(f"{file} successfully processed")
            return df
        except Exception as e:
            print(f"Failed to read {file}: Code error: {e}")
            return None
