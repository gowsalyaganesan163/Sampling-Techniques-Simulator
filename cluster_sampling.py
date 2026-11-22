import random
from display_sample import display_sample


def cluster_sampling(dataset):

    print("\n" + "=" * 60)
    print("                 CLUSTER SAMPLING")
    print("=" * 60)

    population_size = len(dataset)

    print(
        f"\nPopulation Size : {population_size}"
    )

    # -----------------------------------------------------
    # FIND CLUSTER COLUMNS
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
            "\n❌ No suitable cluster columns found."
        )

        return None

    print("\nAvailable Cluster Columns:")
    print("-" * 50)

    for index, column in enumerate(
        categorical_columns,
        start=1
    ):

        print(
            f"{index}. {column}"
        )

    # -----------------------------------------------------
    # SELECT CLUSTER COLUMN
    # -----------------------------------------------------

    while True:

        try:

            choice = int(
                input(
                    "\nSelect cluster column: "
                )
            )

            if 1 <= choice <= len(
                categorical_columns
            ):

                cluster_column = (
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
    # FIND CLUSTERS
    # -----------------------------------------------------

    clusters = dataset[
        cluster_column
    ].dropna().unique().tolist()

    print(
        f"\nNumber of Clusters : "
        f"{len(clusters)}"
    )

    print("\nClusters:")
    print("-" * 50)

    for cluster in clusters:

        count = len(
            dataset[
                dataset[
                    cluster_column
                ] == cluster
            ]
        )

        print(
            f"{cluster}: "
            f"{count} records"
        )

    if len(clusters) < 2:

        print(
            "\n❌ At least two clusters "
            "are required."
        )

        return None

    # -----------------------------------------------------
    # NUMBER OF CLUSTERS
    # -----------------------------------------------------

    while True:

        try:

            number_to_select = int(
                input(
                    "\nHow many clusters should be selected? "
                )
            )

            if (
                1 <= number_to_select
                < len(clusters)
            ):

                break

            print(
                f"❌ Enter a number between "
                f"1 and {len(clusters) - 1}."
            )

        except ValueError:

            print(
                "❌ Enter a valid number."
            )

    # -----------------------------------------------------
    # RANDOMLY SELECT CLUSTERS
    # -----------------------------------------------------

    selected_clusters = random.sample(
        clusters,
        number_to_select
    )

    print("\n🎲 SELECTED CLUSTERS")
    print("-" * 50)

    for cluster in selected_clusters:

        print(
            f"- {cluster}"
        )

    # -----------------------------------------------------
    # CREATE SAMPLE
    # -----------------------------------------------------

    sample = dataset[
        dataset[
            cluster_column
        ].isin(selected_clusters)
    ].copy()

    print("\n" + "=" * 60)
    print("              CLUSTER SAMPLE RESULT")
    print("=" * 60)

    print(
        f"\nCluster Column : "
        f"{cluster_column}"
    )

    print(
        f"Selected Clusters : "
        f"{len(selected_clusters)}"
    )

    print(
        f"Sample Size : "
        f"{len(sample)}"
    )

    print(
        "\nAll observations belonging to "
        "the selected clusters were included."
    )

    # -----------------------------------------------------
    # DISPLAY SAMPLE
    # -----------------------------------------------------

    display_sample(sample)

    return sample