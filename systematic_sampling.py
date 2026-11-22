import random
from display_sample import display_sample


def systematic_sampling(dataset):

    print("\n" + "=" * 60)
    print("               SYSTEMATIC SAMPLING")
    print("=" * 60)

    population_size = len(dataset)

    print(
        f"\nPopulation Size (N) : "
        f"{population_size}"
    )

    # -----------------------------------------------------
    # SAMPLE SIZE
    # -----------------------------------------------------

    while True:

        try:

            sample_size = int(
                input(
                    "\nEnter sample size (n): "
                )
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
    # SAMPLING INTERVAL
    # -----------------------------------------------------

    interval = population_size // sample_size

    if interval < 1:

        print(
            "\n❌ Invalid sampling interval."
        )

        return None

    print("\n📐 SAMPLING INTERVAL")
    print("-" * 50)

    print(
        "Formula: k = N / n"
    )

    print(
        f"k = {population_size} / "
        f"{sample_size}"
    )

    print(
        f"k = {interval}"
    )

    # -----------------------------------------------------
    # RANDOM START
    # -----------------------------------------------------

    start = random.randint(
        0,
        interval - 1
    )

    print(
        f"\nRandom Starting Position : "
        f"{start + 1}"
    )

    # -----------------------------------------------------
    # EVERY KTH RECORD
    # -----------------------------------------------------

    indices = []

    current = start

    while (
        current < population_size
        and len(indices) < sample_size
    ):

        indices.append(
            current
        )

        current += interval

    sample = dataset.iloc[
        indices
    ].copy()

    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("           SYSTEMATIC SAMPLE RESULT")
    print("=" * 60)

    print(
        f"\nSampling Interval (k) : "
        f"{interval}"
    )

    print(
        f"Sample Size : "
        f"{len(sample)}"
    )

    print("\nSelected Positions:")

    print(
        [
            index + 1
            for index in indices[:20]
        ]
    )

    if len(indices) > 20:

        print(
            "... showing first 20 positions"
        )

    # -----------------------------------------------------
    # DISPLAY SAMPLE
    # -----------------------------------------------------

    display_sample(sample)

    return sample