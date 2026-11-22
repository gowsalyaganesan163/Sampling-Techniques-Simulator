import pandas as pd


def sampling_error_analysis(dataset):

    print("\n" + "=" * 65)
    print("                  SAMPLING ERROR")
    print("=" * 65)

    population_size = len(dataset)

    print(f"\nPopulation Size : {population_size}")

    # ------------------------------------------------
    # FIND NUMERICAL COLUMNS
    # ------------------------------------------------

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns.tolist()

    if not numerical_columns:

        print("\n❌ No numerical columns found.")
        print(
            "Sampling error calculation requires "
            "a numerical column."
        )
        return None

    # ------------------------------------------------
    # SELECT NUMERICAL COLUMN
    # ------------------------------------------------

    print("\nAvailable Numerical Columns:")
    print("-" * 45)

    for index, column in enumerate(
        numerical_columns,
        start=1
    ):
        print(f"{index}. {column}")

    while True:

        try:

            column_choice = int(
                input("\nSelect a numerical column: ")
            )

            if 1 <= column_choice <= len(numerical_columns):

                analysis_column = numerical_columns[
                    column_choice - 1
                ]

                break

            else:

                print(
                    "❌ Please select a valid column number."
                )

        except ValueError:

            print(
                "❌ Please enter a valid number."
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
                    f"❌ Sample size must be smaller than "
                    f"population size ({population_size})."
                )

            else:

                break

        except ValueError:

            print(
                "❌ Please enter a valid number."
            )

    # ------------------------------------------------
    # SELECT RANDOM SAMPLE
    # ------------------------------------------------

    sample = dataset.sample(
        n=sample_size
    )

    # ------------------------------------------------
    # CALCULATE MEANS
    # ------------------------------------------------

    population_mean = dataset[
        analysis_column
    ].mean()

    sample_mean = sample[
        analysis_column
    ].mean()

    # ------------------------------------------------
    # SAMPLING ERROR
    # ------------------------------------------------

    sampling_error = abs(
        population_mean - sample_mean
    )

    # ------------------------------------------------
    # PERCENTAGE ERROR
    # ------------------------------------------------

    if population_mean != 0:

        percentage_error = (
            sampling_error
            / abs(population_mean)
        ) * 100

    else:

        percentage_error = 0

    # ------------------------------------------------
    # DISPLAY RESULT
    # ------------------------------------------------

    print("\n" + "=" * 65)
    print("              SAMPLING ERROR RESULT")
    print("=" * 65)

    print(
        f"\nVariable          : {analysis_column}"
    )

    print(
        f"Population Size   : {population_size}"
    )

    print(
        f"Sample Size       : {sample_size}"
    )

    print(
        f"\nPopulation Mean   : "
        f"{population_mean:.2f}"
    )

    print(
        f"Sample Mean       : "
        f"{sample_mean:.2f}"
    )

    print(
        f"\nSampling Error    : "
        f"{sampling_error:.2f}"
    )

    print(
        f"Percentage Error  : "
        f"{percentage_error:.2f}%"
    )

    # ------------------------------------------------
    # INTERPRETATION
    # ------------------------------------------------

    print("\n" + "-" * 65)
    print("                 INTERPRETATION")
    print("-" * 65)

    print(
        "\nSampling Error = "
        "| Population Mean - Sample Mean |"
    )

    print(
        f"                  = "
        f"| {population_mean:.2f} - "
        f"{sample_mean:.2f} |"
    )

    print(
        f"                  = "
        f"{sampling_error:.2f}"
    )

    if sampling_error == 0:

        print(
            "\n✅ No difference between the "
            "population mean and sample mean."
        )

    elif percentage_error <= 5:

        print(
            "\n✅ The sample mean is very close "
            "to the population mean."
        )

    elif percentage_error <= 10:

        print(
            "\n⚠ The sample mean shows a moderate "
            "difference from the population mean."
        )

    else:

        print(
            "\n❌ The sample mean shows a relatively "
            "large difference from the population mean."
        )

    print("\n📌 NOTE")

    print(
        "Sampling error is expected when a sample "
        "is used instead of the entire population."
    )

    print(
        "A smaller sampling error means the sample "
        "statistic is closer to the population parameter."
    )

    print("\n" + "=" * 65)

    return {
        "population_mean": population_mean,
        "sample_mean": sample_mean,
        "sampling_error": sampling_error,
        "percentage_error": percentage_error
    }