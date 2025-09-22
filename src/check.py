import sys
import pandas as pd
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/check.py <path_to_csv>")
        raise SystemExit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        raise SystemExit(1)

    df = pd.read_csv(path)
    print("Rows x Cols:", df.shape)
    print("\nDtypes:\n", df.dtypes)
    print("\nMissing per column:\n", df.isna().sum())
    print("\nHead:\n", df.head())