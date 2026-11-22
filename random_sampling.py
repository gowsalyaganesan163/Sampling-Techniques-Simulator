from display_sample import display_sample


def random_sampling(dataset):

    print("\n" + "=" * 60)
    print("                 RANDOM SAMPLING")
    print("=" * 60)

    population_size = len(dataset)

    print(
        f"\nPopulation Size : {population_size}"
    )

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
                    "❌ Sample size must be smaller "
                    "than population size."
                )

            else:

                break

        except ValueError:

            print("❌ Enter a valid number.")

    # ------------------------------------------------
    # RANDOM SAMPLE
    # ------------------------------------------------

    sample = dataset.sample(
        n=sample_size
    )

    print("\n🎲 RANDOM SAMPLING COMPLETED")

    print(
        "\nEvery population record had an equal "
        "chance of being selected."
    )

    print(
        f"\nSample Size : {len(sample)}"
    )

    # ------------------------------------------------
    # NUMERICAL COLUMN
    # ------------------------------------------------

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns.tolist()

    if numerical_columns:

        print("\nAvailable Numerical Columns:")

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
                        "\nSelect a numerical column: "
                    )
                )

                if 1 <= choice <= len(numerical_columns):

                    selected_column = (
                        numerical_columns[choice - 1]
                    )

                    break

                print("❌ Invalid choice.")

            except ValueError:

                print("❌ Enter a valid number.")

        population_mean = dataset[
            selected_column
        ].mean()

        sample_mean = sample[
            selected_column
        ].mean()

        print("\n📊 STATISTICAL RESULT")
        print("-" * 50)

        print(
            f"Population Mean : {population_mean:.2f}"
        )

        print(
            f"Sample Mean     : {sample_mean:.2f}"
        )

    # ------------------------------------------------
    # SAMPLE DISPLAY
    # ------------------------------------------------

    display_sample(sample)

    return sample