def view_population(dataset):

    print("\n" + "=" * 60)
    print("                    POPULATION")
    print("=" * 60)

    population_size = len(dataset)

    print(f"\nPopulation Size : {population_size}")
    print(f"Number of Columns : {dataset.shape[1]}")

    print("\nColumns:")
    print("-" * 40)

    for column in dataset.columns:
        print(f"- {column}")

    print("\n📊 DATA TYPES")
    print("-" * 40)

    print(dataset.dtypes.to_string())

    print("\n❓ MISSING VALUES")
    print("-" * 40)

    missing = dataset.isnull().sum()

    print(missing.to_string())

    print("\n👀 POPULATION PREVIEW")
    print("-" * 40)

    print(
        dataset.head(10).to_string(index=False)
    )

    if population_size > 10:

        print(
            f"\nShowing 10 of {population_size} records."
        )

    numerical_columns = dataset.select_dtypes(
        include="number"
    ).columns

    if len(numerical_columns) > 0:

        print("\n📈 NUMERICAL SUMMARY")
        print("-" * 40)

        print(
            dataset[numerical_columns]
            .describe()
            .round(2)
            .to_string()
        )

    print("\n" + "=" * 60)