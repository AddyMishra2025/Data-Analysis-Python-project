import argparse
from pathlib import Path
import pandas as pd

def summarize_csv(path: Path, sep: str = ",", encoding: str = "utf-8", nrows: int | None = None):
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path, sep=sep, encoding=encoding, nrows=nrows)

    print("File:", path)
    print("Rows x Cols:", df.shape, "\n")
    print("Dtypes:\n", df.dtypes, "\n")
    print("Missing per column:\n", df.isna().sum().sort_values(ascending=False), "\n")

    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        print("Numeric describe():\n", numeric.describe().T, "\n")

    print("Head:\n", df.head(5))

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Quick CSV summary")
    p.add_argument("csv_path", type=Path)
    p.add_argument("--sep", default=",")
    p.add_argument("--encoding", default="utf-8")
    p.add_argument("--nrows", type=int, default=None)
    args = p.parse_args()
    summarize_csv(args.csv_path, args.sep, args.encoding, args.nrows)
