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

    # Use only female data for this MVP.
    female_df = df[df["Gender"] == "Female"].copy()

    female_df["BodyType"] = female_df.apply(
        lambda row: determine_body_type(
            shoulder=row["ShoulderWidth_cm"],
            bust=row["Chest_cm"],
            waist=row["Waist_cm"],
            hip=row["Hip_cm"],
        ),
        axis=1,
    )

    print(f"Female rows loaded: {len(female_df)}")
    print(female_df[["UserID", "Gender", "Chest_cm", "Waist_cm", "Hip_cm", "ShoulderWidth_cm", "BodyType"]].head())
    print("\nBody type counts for female subset:")
    print(female_df["BodyType"].value_counts())


if __name__ == "__main__":
    main()
