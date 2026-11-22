from display_sample import display_sample


def population_vs_sample(dataset):

    print("\n" + "=" * 60)
    print("              POPULATION VS SAMPLE")
    print("=" * 60)

    population_size = len(dataset)

    print(
        f"\nPopulation Size : {population_size}"
    )

    # -----------------------------------------------------
    # SAMPLE SIZE
    # -----------------------------------------------------

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
                    f"{population_size}."
                )

            else:

                break

        except ValueError:

            print(
                "❌ Enter a valid number."
            )

    # -----------------------------------------------------
    # CREATE SUBSET
    # -----------------------------------------------------

    sample = dataset.head(
        sample_size
    ).copy()

    print("\n📊 POPULATION VS SAMPLE")
    print("-" * 50)

    print(
        f"Population Size : {population_size}"
    )

    print(
        f"Sample Size     : {len(sample)}"
    )

    print(
        "\nPopulation = complete set of observations."
    )

    print(
        "Sample = subset of the population."
    )

    # -----------------------------------------------------
    # NUMERICAL COMPARISON
    # -----------------------------------------------------

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns.tolist()

    if numerical_columns:

        print(
            "\nAvailable Numerical Columns:"
        )

        print("-" * 50)

        for index, column in enumerate(
            numerical_columns,
            start=1
        ):

            print(
                f"{index}. {column}"
            )

        while True:

            try:

                choice = int(
                    input(
                        "\nSelect a column to compare: "
                    )
                )

                if 1 <= choice <= len(
                    numerical_columns
                ):

                    selected_column = (
                        numerical_columns[
                            choice - 1
                        ]
                    )

                    break

                print(
                    "❌ Invalid choice."
                )

            except ValueError:

                print(
                    "❌ Enter a number."
                )

        population_mean = dataset[
            selected_column
        ].mean()

        sample_mean = sample[
            selected_column
        ].mean()

        print("\n📈 MEAN COMPARISON")
        print("-" * 50)

        print(
            f"Population Mean : "
            f"{population_mean:.2f}"
        )

        print(
            f"Sample Mean     : "
            f"{sample_mean:.2f}"
        )

    else:

        print(
            "\n⚠ No numerical columns available."
        )

    # -----------------------------------------------------
    # DISPLAY SAMPLE
    # -----------------------------------------------------

    display_sample(sample)

    return sample