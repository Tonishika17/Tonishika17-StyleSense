import kagglehub
from kagglehub import KaggleDatasetAdapter
from body_analysis.body_type import determine_body_type


DATASET_HANDLE = "zara2099/personalized-clothing-and-body-measurements-data"
DATASET_FILE = "personalized_clothing_dataset.csv"

def main():

    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        DATASET_HANDLE,
        DATASET_FILE,
        pandas_kwargs={"nrows": 500},
    )
    print(df.columns.tolist())
    # Generate predictions using actual dataset column names
    def _get_val(row, col_names):
        for c in col_names:
            if c in row and not (row[c] is None):
                return row[c]
        return 0

    df["predicted_body_type"] = df.apply(
        lambda row: determine_body_type(
            shoulder=_get_val(row, ["ShoulderWidth_cm", "ShoulderWidth"]),
            bust=_get_val(row, ["Chest_cm", "Chest", "bust"]),
            waist=_get_val(row, ["Waist_cm", "Waist", "waist"]),
            hip=_get_val(row, ["Hip_cm", "Hip", "hip"]),
        ),
        axis=1,
    )

    # Preview results (use existing dataset column names)
    preview_cols = [c for c in ["UserID", "Chest_cm", "Waist_cm", "Hip_cm", "predicted_body_type"] if c in df.columns]
    print(df[preview_cols].head(10))

    # If the dataset contains an expected label column, compute accuracy
    if "expected_type" in df.columns:
        correct = (
            df["expected_type"].str.strip().str.lower()
            ==
            df["predicted_body_type"].str.strip().str.lower()
        ).sum()

        total = len(df)
        accuracy = (correct / total) * 100

        print(f"\nCorrect Predictions: {correct}")
        print(f"Total Samples: {total}")
        print(f"Accuracy: {accuracy:.2f}%")
    else:
        print("\nNo `expected_type` column in dataset — skipping accuracy check.")

    # Show prediction distribution
    print("\nPredicted Body Types:")
    print(df["predicted_body_type"].value_counts())

    # Show incorrect predictions if expected labels exist
    if "expected_type" in df.columns:
        incorrect = df[
            df["expected_type"].str.strip().str.lower()
            !=
            df["predicted_body_type"].str.strip().str.lower()
        ]

        print(f"\nIncorrect Predictions: {len(incorrect)}")

        inc_cols = [c for c in ["UserID", "Chest_cm", "Waist_cm", "Hip_cm", "expected_type", "predicted_body_type"] if c in incorrect.columns]
        print(incorrect[inc_cols].head(20))


if __name__ == "__main__":
    main()