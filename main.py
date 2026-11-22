from data_loader import load_dataset
from population import view_population
from population_sample import population_vs_sample
from random_sampling import random_sampling
from stratified_sampling import stratified_sampling
from cluster_sampling import cluster_sampling
from systematic_sampling import systematic_sampling
from comparsion import compare_sampling_techniques
from bias_analysis import sampling_bias_analysis
from sampling_error import sampling_error_analysis


def display_menu():

    print("\n" + "=" * 60)
    print("             SAMPLING TECHNIQUES SIMULATOR")
    print("=" * 60)

    print("\n1. Load Dataset")
    print("2. View Population")
    print("3. Population vs Sample")
    print("4. Random Sampling")
    print("5. Stratified Sampling")
    print("6. Cluster Sampling")
    print("7. Systematic Sampling")
    print("8. Compare Sampling Techniques")
    print("9. Sampling Bias Analysis")
    print("10. Sampling Error")
    print("0. Exit")

    print("\n" + "=" * 60)


def check_dataset(dataset):

    if dataset is None:

        print(
            "\n⚠ Please load a dataset first."
        )

        return False

    return True


def main():

    # ------------------------------------------------
    # DATASET STORAGE
    # ------------------------------------------------

    dataset = None

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # ------------------------------------------------
        # 1. LOAD DATASET
        # ------------------------------------------------

        if choice == "1":

            loaded_data = load_dataset()

            if loaded_data is not None:

                dataset = loaded_data

                print(
                    "\n✅ Dataset loaded successfully."
                )

        # ------------------------------------------------
        # 2. VIEW POPULATION
        # ------------------------------------------------

        elif choice == "2":

            if check_dataset(dataset):

                view_population(dataset)

        # ------------------------------------------------
        # 3. POPULATION VS SAMPLE
        # ------------------------------------------------

        elif choice == "3":

            if check_dataset(dataset):

                population_vs_sample(dataset)

        # ------------------------------------------------
        # 4. RANDOM SAMPLING
        # ------------------------------------------------

        elif choice == "4":

            if check_dataset(dataset):

                random_sampling(dataset)

        # ------------------------------------------------
        # 5. STRATIFIED SAMPLING
        # ------------------------------------------------

        elif choice == "5":

            if check_dataset(dataset):

                stratified_sampling(dataset)

        # ------------------------------------------------
        # 6. CLUSTER SAMPLING
        # ------------------------------------------------

        elif choice == "6":

            if check_dataset(dataset):

                cluster_sampling(dataset)

        # ------------------------------------------------
        # 7. SYSTEMATIC SAMPLING
        # ------------------------------------------------

        elif choice == "7":

            if check_dataset(dataset):

                systematic_sampling(dataset)

        # ------------------------------------------------
        # 8. COMPARE SAMPLING TECHNIQUES
        # ------------------------------------------------

        elif choice == "8":

            if check_dataset(dataset):

                compare_sampling_techniques(dataset)

        # ------------------------------------------------
        # 9. SAMPLING BIAS
        # ------------------------------------------------

        elif choice == "9":

            if check_dataset(dataset):

                sampling_bias_analysis(dataset)

        # ------------------------------------------------
        # 10. SAMPLING ERROR
        # ------------------------------------------------

        elif choice == "10":

            if check_dataset(dataset):

                sampling_error_analysis(dataset)

        # ------------------------------------------------
        # 0. EXIT
        # ------------------------------------------------

        elif choice == "0":

            print("\n" + "=" * 60)
            print(
                "     Thank you for using "
                "Sampling Techniques Simulator!"
            )
            print("=" * 60)

            break

        # ------------------------------------------------
        # INVALID CHOICE
        # ------------------------------------------------

        else:

            print("\n❌ Invalid choice.")
            print(
                "Please enter a number from 0 to 10."
            )


if __name__ == "__main__":

    main()