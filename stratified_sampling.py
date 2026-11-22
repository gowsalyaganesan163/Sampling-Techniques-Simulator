import pandas as pd
from display_sample import display_sample


def stratified_sampling(dataset):

    print("\n" + "=" * 60)
    print("                STRATIFIED SAMPLING")
    print("=" * 60)

    population_size = len(dataset)

    print(
        f"\nPopulation Size : {population_size}"
    )

    # -----------------------------------------------------
    # FIND SUITABLE CATEGORICAL COLUMNS
    # -----------------------------------------------------

    categorical_columns = []

    for column in dataset.select_dtypes(
        include=["object", "category", "bool"]
    ).columns:

        unique_count = dataset[
            column
        ].nunique(dropna=True)

        if 1 < unique_count <= 20:

            categorical_columns.append(
                column
            )

    if not categorical_columns:

        print(
            "\n❌ No suitable stratification "
            "columns found."
        )

        return None

    print(
        "\nAvailable Stratification Columns:"
    )

    print("-" * 50)

    for index, column in enumerate(
        categorical_columns,
        start=1
    ):

        print(
            f"{index}. {column}"
        )

    # -----------------------------------------------------
    # SELECT STRATIFICATION COLUMN
    # -----------------------------------------------------

    while True:

        try:

            choice = int(
                input(
                    "\nSelect stratification column: "
                )
            )

            if 1 <= choice <= len(
                categorical_columns
            ):

                stratification_column = (
                    categorical_columns[
                        choice - 1
                    ]
                )

                break

            print(
                "❌ Invalid choice."
            )

        except ValueError:

            print(
                "❌ Enter a valid number."
            )

    # -----------------------------------------------------
    # SHOW STRATA
    # -----------------------------------------------------

    strata_counts = dataset[
        stratification_column
    ].value_counts()

    print("\n📊 POPULATION STRATA")
    print("-" * 60)

    for stratum, count in (
        strata_counts.items()
    ):

        proportion = (
            count / population_size
        ) * 100

        print(
            f"{stratum}: "
            f"{count} records "
            f"({proportion:.2f}%)"
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
                    "❌ Sample size must be smaller "
                    "than population size."
                )

            else:

                break

        except ValueError:

            print(
                "❌ Enter a valid number."
            )

    # -----------------------------------------------------
    # PROPORTIONAL ALLOCATION
    # -----------------------------------------------------

    print(
        "\n📐 PROPORTIONAL SAMPLE ALLOCATION"
    )

    print("-" * 60)

    allocations = {}

    for stratum, count in (
        strata_counts.items()
    ):

        allocation = round(
            (count / population_size)
            * sample_size
        )

        allocations[stratum] = allocation

        print(
            f"{stratum}: "
            f"{allocation} sample records"
        )

    # -----------------------------------------------------
    # RANDOM SELECTION WITHIN EACH STRATUM
    # -----------------------------------------------------

    sample_parts = []

    for stratum, allocation in (
        allocations.items()
    ):

        if allocation <= 0:

            continue

        group = dataset[
            dataset[
                stratification_column
            ] == stratum
        ]

        selected = group.sample(
            n=min(
                allocation,
                len(group)
            )
        )

        sample_parts.append(
            selected
        )

    if not sample_parts:

        print(
            "\n❌ Could not create sample."
        )

        return None

    sample = pd.concat(
        sample_parts
    )

    # -----------------------------------------------------
    # ADJUST FOR ROUNDING
    # -----------------------------------------------------

    if len(sample) < sample_size:

        remaining = dataset.drop(
            sample.index
        )

        extra_count = (
            sample_size - len(sample)
        )

        if extra_count <= len(
            remaining
        ):

            extra = remaining.sample(
                n=extra_count
            )

            sample = pd.concat(
                [sample, extra]
            )

    elif len(sample) > sample_size:

        sample = sample.sample(
            n=sample_size
        )

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("             STRATIFIED SAMPLE")
    print("=" * 60)

    print(
        f"\nStratification Column : "
        f"{stratification_column}"
    )

    print(
        f"Population Size       : "
        f"{population_size}"
    )

    print(
        f"Sample Size           : "
        f"{len(sample)}"
    )

    print(
        "\nRandom selection was performed "
        "within each stratum."
    )

    # -----------------------------------------------------
    # DISPLAY SAMPLE
    # -----------------------------------------------------

    display_sample(
        sample,
        stratification_column
    )

    return sample