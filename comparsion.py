import pandas as pd
import random
import matplotlib.pyplot as plt


def compare_sampling_techniques(dataset):

    print("\n" + "=" * 65)
    print("              COMPARE SAMPLING TECHNIQUES")
    print("=" * 65)

    population_size = len(dataset)

    print(f"\nPopulation Size : {population_size}")

    # ------------------------------------------------
    # FIND NUMERICAL COLUMN
    # ------------------------------------------------

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns.tolist()

    if not numerical_columns:

        print("\n❌ No numerical columns found.")
        print("Comparison requires at least one numerical column.")

        return None

    print("\nAvailable Numerical Columns:")
    print("-" * 40)

    for index, column in enumerate(
        numerical_columns,
        start=1
    ):
        print(f"{index}. {column}")

    # ------------------------------------------------
    # SELECT NUMERICAL COLUMN
    # ------------------------------------------------

    while True:

        try:

            column_choice = int(
                input("\nSelect column for comparison: ")
            )

            if 1 <= column_choice <= len(numerical_columns):

                analysis_column = numerical_columns[
                    column_choice - 1
                ]

                break

            else:

                print("❌ Please select a valid column number.")

        except ValueError:

            print("❌ Please enter a valid number.")

    population_mean = dataset[
        analysis_column
    ].mean()

    print(
        f"\nSelected Column : {analysis_column}"
    )

    print(
        f"Population Mean : {population_mean:.2f}"
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

    # =================================================
    # 1. RANDOM SAMPLING
    # =================================================

    random_sample = dataset.sample(
        n=sample_size
    )

    random_mean = random_sample[
        analysis_column
    ].mean()

    random_error = abs(
        population_mean - random_mean
    )

    # =================================================
    # 2. STRATIFIED SAMPLING
    # =================================================

    categorical_columns = dataset.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    stratified_sample = None

    if categorical_columns:

        print("\nAvailable Stratification Columns:")

        for index, column in enumerate(
            categorical_columns,
            start=1
        ):
            print(f"{index}. {column}")

        while True:

            try:

                column_choice = int(
                    input(
                        "\nSelect column for "
                        "Stratified Sampling: "
                    )
                )

                if 1 <= column_choice <= len(categorical_columns):

                    stratified_column = categorical_columns[
                        column_choice - 1
                    ]

                    break

                else:

                    print(
                        "❌ Please select a valid column."
                    )

            except ValueError:

                print(
                    "❌ Please enter a valid number."
                )

        stratified_sample = pd.DataFrame()

        for stratum, group in dataset.groupby(
            stratified_column,
            dropna=False
        ):

            proportion = len(group) / population_size

            stratum_size = round(
                proportion * sample_size
            )

            stratum_size = min(
                stratum_size,
                len(group)
            )

            if stratum_size > 0:

                selected = group.sample(
                    n=stratum_size
                )

                stratified_sample = pd.concat(
                    [
                        stratified_sample,
                        selected
                    ]
                )

        # Adjust rounding difference
        difference = (
            sample_size
            - len(stratified_sample)
        )

        if difference > 0:

            remaining = dataset.drop(
                stratified_sample.index,
                errors="ignore"
            )

            if len(remaining) >= difference:

                extra = remaining.sample(
                    n=difference
                )

                stratified_sample = pd.concat(
                    [
                        stratified_sample,
                        extra
                    ]
                )

        elif difference < 0:

            stratified_sample = stratified_sample.sample(
                n=sample_size
            )

        stratified_mean = stratified_sample[
            analysis_column
        ].mean()

        stratified_error = abs(
            population_mean - stratified_mean
        )

    # =================================================
    # 3. SYSTEMATIC SAMPLING
    # =================================================

    interval = population_size // sample_size

    if interval >= 1:

        start = random.randint(
            0,
            interval - 1
        )

        indices = []

        current = start

        while (
            current < population_size
            and len(indices) < sample_size
        ):

            indices.append(current)

            current += interval

        # Fill remaining records if required
        if len(indices) < sample_size:

            remaining_indices = [
                i
                for i in range(population_size)
                if i not in indices
            ]

            indices.extend(
                remaining_indices[
                    :sample_size - len(indices)
                ]
            )

        systematic_sample = dataset.iloc[
            indices
        ]

        systematic_mean = systematic_sample[
            analysis_column
        ].mean()

        systematic_error = abs(
            population_mean - systematic_mean
        )

    else:

        systematic_sample = dataset.sample(
            n=sample_size
        )

        systematic_mean = systematic_sample[
            analysis_column
        ].mean()

        systematic_error = abs(
            population_mean - systematic_mean
        )

    # =================================================
    # 4. CLUSTER SAMPLING
    # =================================================

    cluster_sample = None

    cluster_mean = None
    cluster_error = None

    if categorical_columns:

        cluster_column = stratified_column

        clusters = dataset[
            cluster_column
        ].dropna().unique()

        if len(clusters) > 1:

            # Select approximately half the clusters
            number_of_clusters = max(
                1,
                len(clusters) // 2
            )

            selected_clusters = random.sample(
                list(clusters),
                number_of_clusters
            )

            cluster_sample = dataset[
                dataset[cluster_column].isin(
                    selected_clusters
                )
            ]

            cluster_mean = cluster_sample[
                analysis_column
            ].mean()

            cluster_error = abs(
                population_mean - cluster_mean
            )

    # =================================================
    # CREATE COMPARISON TABLE
    # =================================================

    results = []

    results.append({
        "Technique": "Random Sampling",
        "Sample Size": len(random_sample),
        "Sample Mean": random_mean,
        "Sampling Error": random_error
    })

    if stratified_sample is not None:

        results.append({
            "Technique": "Stratified Sampling",
            "Sample Size": len(stratified_sample),
            "Sample Mean": stratified_mean,
            "Sampling Error": stratified_error
        })

    if cluster_sample is not None:

        results.append({
            "Technique": "Cluster Sampling",
            "Sample Size": len(cluster_sample),
            "Sample Mean": cluster_mean,
            "Sampling Error": cluster_error
        })

    results.append({
        "Technique": "Systematic Sampling",
        "Sample Size": len(systematic_sample),
        "Sample Mean": systematic_mean,
        "Sampling Error": systematic_error
    })

    comparison = pd.DataFrame(results)

    # ------------------------------------------------
    # DISPLAY RESULTS
    # ------------------------------------------------

    print("\n" + "=" * 65)
    print("                 COMPARISON RESULT")
    print("=" * 65)

    print(
        f"\nPopulation Mean ({analysis_column}) : "
        f"{population_mean:.2f}"
    )

    print("\n")
    print(
        comparison.round(2).to_string(
            index=False
        )
    )

    # =================================================
    # FIND BEST TECHNIQUE
    # =================================================

    best_row = comparison.loc[
        comparison["Sampling Error"].idxmin()
    ]
    print("\n" + "-" * 65)
    print("                    SIMULATION ANALYSIS")
    print("-" * 65)

    print("\n📊 CONCLUSION")

    print(
        f"\nFor this population, "
        f"{best_row['Technique']} performed best "
        f"among the sampling techniques tested."
    )

    print(
        f"\nReason:"
    )

    print(
        f"It produced the lowest sampling error "
        f"compared with the other sampling techniques."
    )

    print(
        f"\nSampling Error : "
        f"{best_row['Sampling Error']:.2f}"
    )

    print(
        "\nNote:"
    )

    print(
        "This conclusion is specific to the current "
        "population, sample size, and simulation."
    )
    # =================================================
    # VISUALIZATION
    # =================================================

    print("\n📊 Generating Sampling Error Chart...")

    plt.figure(figsize=(10, 6))

    plt.bar(
        comparison["Technique"],
        comparison["Sampling Error"]
    )

    plt.title("Sampling Error Comparison")

    plt.xlabel("Sampling Technique")

    plt.ylabel("Sampling Error")

    plt.xticks(
        rotation=20,
        ha="right"
    )

    plt.tight_layout()

    plt.show()

    print("\n" + "=" * 65)

    return comparison