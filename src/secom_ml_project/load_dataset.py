
from pathlib import Path
import pandas as pd

#paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

#load original SECOM dataset
X = pd.read_csv(
    DATA_DIR / "secom.data",
    sep=r"\s+",
    header=None,
    na_values=["NaN"]
)

#load labels and timestamps
labels = pd.read_csv(
    DATA_DIR / "secom_labels.data",
    sep=r"\s+",
    header=None
)

#assign meaningful column names
X.columns = [f"sensor_{i:03d}" for i in range(X.shape[1])]
labels.columns = ["label", "date", "time"]

#extract target variable
y = labels["label"]

print("=" * 50)
print("SECOM DATASET")
print("=" * 50)

print("\nFeatures shape:", X.shape)
print("Labels shape:", y.shape)

print("\nFirst 5 samples (first 10 sensors):")
print(X.iloc[:5, :10].to_string())

print("\nTarget distribution:")
print(y.value_counts())

print("\nMissing values:", X.isna().sum().sum())

print("\nData types:")
print(X.dtypes.value_counts())
