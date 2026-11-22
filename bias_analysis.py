import pandas as pd


def sampling_bias_analysis(dataset):

    print("\n" + "=" * 65)
    print("                 SAMPLING BIAS ANALYSIS")
    print("=" * 65)

    population_size = len(dataset)

    print(f"\nPopulation Size : {population_size}")

    # ------------------------------------------------
    # FIND CATEGORICAL COLUMNS
    # ------------------------------------------------

    categorical_columns = dataset.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    if not categorical_columns:

        print("\n❌ No categorical columns found.")
        print(
            "Bias analysis requires a categorical column "
            "to compare population and sample distributions."
        )
        return None

    # ------------------------------------------------
    # SELECT COLUMN
    # ------------------------------------------------

    print("\nAvailable Columns for Bias Analysis:")
    print("-" * 45)

    for index, column in enumerate(
        categorical_columns,
        start=1
    ):
        print(f"{index}. {column}")

    while True:

        try:

            column_choice = int(
                input("\nSelect a column: ")
            )

            if 1 <= column_choice <= len(categorical_columns):

                analysis_column = categorical_columns[
                    column_choice - 1
                ]

                break

            else:

                print("❌ Please select a valid column number.")

        except ValueError:

            print("❌ Please enter a valid number.")

    # ------------------------------------------------
    # SAMPLE SIZE
    # ------------------------------------------------

    while True:

        try:

            sample_size = int(
                input("\nEnter sample size: ")
            )

            if sample_size <= 0:

                print(
                    "❌ Sample size must be greater than 0."
                )

            elif sample_size >= population_size:

                print(
                    f"❌ Sample size must be smaller than "
                    f"population size ({population_size})."
                )

            else:

                break

        except ValueError:

            print("❌ Please enter a valid number.")

    # ------------------------------------------------
    # RANDOM SAMPLE
    # ------------------------------------------------

    sample = dataset.sample(
        n=sample_size
    )

    # ------------------------------------------------
    # POPULATION DISTRIBUTION
    # ------------------------------------------------

    population_distribution = (
        dataset[analysis_column]
        .value_counts(normalize=True, dropna=False)
        * 100
    )

    # ------------------------------------------------
    # SAMPLE DISTRIBUTION
    # ------------------------------------------------

    sample_distribution = (
        sample[analysis_column]
        .value_counts(normalize=True, dropna=False)
        * 100
    )

    # ------------------------------------------------
    # COMPARISON
    # ------------------------------------------------

    comparison = pd.DataFrame({
        "Population %": population_distribution,
        "Sample %": sample_distribution
    }).fillna(0)

    comparison["Difference %"] = (
        comparison["Population %"]
        - comparison["Sample %"]
    ).abs()

    # ------------------------------------------------
    # DISPLAY RESULT
    # ------------------------------------------------

    print("\n" + "=" * 65)
    print("              POPULATION VS SAMPLE")
    print("=" * 65)

    print(
        f"\nAnalysis Column : {analysis_column}"
    )

    print(
        f"Population Size : {population_size}"
    )

    print(
        f"Sample Size : {sample_size}"
    )

    print("\n")
    print(
        comparison.round(2).to_string()
    )

    # ------------------------------------------------
    # CALCULATE OVERALL DISTRIBUTION DIFFERENCE
    # ------------------------------------------------

    total_difference = (
        comparison["Difference %"].sum()
    )

    average_difference = (
        comparison["Difference %"].mean()
    )

    print("\n" + "-" * 65)
    print("                 BIAS ANALYSIS")
    print("-" * 65)

    print(
        f"\nAverage Distribution Difference : "
        f"{average_difference:.2f}%"
    )

    # ------------------------------------------------
    # BIAS INTERPRETATION
    # ------------------------------------------------

    if average_difference <= 5:

        print("\n✅ LOW POTENTIAL SAMPLING BIAS")

        print(
            "\nThe sample distribution is reasonably "
            "similar to the population distribution."
        )

    elif average_difference <= 10:

        print("\n⚠ MODERATE POTENTIAL SAMPLING BIAS")

        print(
            "\nThere is some difference between the "
            "sample and population distributions."
        )

    else:

        print("\n❌ HIGH POTENTIAL SAMPLING BIAS")

        print(
            "\nThe sample distribution differs considerably "
            "from the population distribution."
        )

    # ------------------------------------------------
    # IMPORTANT NOTE
    # ------------------------------------------------

    print("\n📌 NOTE")

    print(
        "This analysis indicates potential sampling bias "
        "based on distribution differences."
    )

    print(
        "A distribution difference alone does not prove "
        "that bias exists."
    )

    print("\n" + "=" * 65)

    return comparison