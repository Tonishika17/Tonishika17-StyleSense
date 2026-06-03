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

    # The dataset uses Chest_cm for bust, Waist_cm for waist, Hip_cm for hip,
    # and ShoulderWidth_cm for shoulder.
    df["BodyType"] = df.apply(
        lambda row: determine_body_type(
            shoulder=row["ShoulderWidth_cm"],
            bust=row["Chest_cm"],
            waist=row["Waist_cm"],
            hip=row["Hip_cm"],
        ),
        axis=1,
    )

    print(df[["UserID", "Chest_cm", "Waist_cm", "Hip_cm", "ShoulderWidth_cm", "BodyType"]].head())
    print("\nBody type counts:")
    print(df["BodyType"].value_counts())


if __name__ == "__main__":
    main()
