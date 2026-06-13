import kagglehub
from kagglehub import KaggleDatasetAdapter
from body_type import determine_body_type


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
    # Generate predictions
    df["predicted_body_type"] = df.apply(
        lambda row: determine_body_type(
            shoulder=0,  # dataset doesn't contain shoulder
            bust=row["bust"],
            waist=row["waist"],
            hip=row["hip"],
        ),
        axis=1,
    )

    # Preview results
    print(
        df[
            [
                "id",
                "bust",
                "waist",
                "hip",
                "expected_type",
                "predicted_body_type",
            ]
        ].head(10)
    )

    # Accuracy
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

    # Show prediction distribution
    print("\nPredicted Body Types:")
    print(df["predicted_body_type"].value_counts())

    # Show incorrect predictions
    incorrect = df[
        df["expected_type"].str.strip().str.lower()
        !=
        df["predicted_body_type"].str.strip().str.lower()
    ]

    print(f"\nIncorrect Predictions: {len(incorrect)}")

    print(
        incorrect[
            [
                "id",
                "bust",
                "waist",
                "hip",
                "expected_type",
                "predicted_body_type",
            ]
        ].head(20)
    )


if __name__ == "__main__":
    main()