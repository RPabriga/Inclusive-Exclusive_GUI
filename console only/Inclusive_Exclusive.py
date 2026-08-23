def count_two_sets(first_size, second_size, shared_size):
    """Return the number of unique members in two sets."""
    return first_size + second_size - shared_size

def count_three_sets(
    first_size,
    second_size,
    third_size,
    first_second_size,
    first_third_size,
    second_third_size,
    all_three_size
):
    """Return the number of unique members in three sets."""

    return (
        first_size
        + second_size
        + third_size
        - first_second_size
        - first_third_size
        - second_third_size
        + all_three_size
    )
# Checks whether the membership totals and overlaps are valid.
def validate_values(values, mode):

    # Check the Math and Science overlap.
    if values["math_science"] > min(
        values["math"],
        values["science"]
    ):
        raise ValueError(
            "The Math and Science overlap cannot exceed either club total."
        )

    # Validation for two clubs.
    if mode == "2 clubs":

        total = count_two_sets(
            values["math"],
            values["science"],
            values["math_science"]
        )

        if total < 0:
            raise ValueError(
                "The two-club total cannot be negative."
            )

    # Validation for three clubs.
    if mode == "3 clubs":

        # Check the Math and Literature overlap.
        if values["math_literature"] > min(
            values["math"],
            values["literature"]
        ):
            raise ValueError(
                "The Math and Literature overlap cannot exceed either club total."
            )

        # Check the Science and Literature overlap.
        if values["science_literature"] > min(
            values["science"],
            values["literature"]
        ):
            raise ValueError(
                "The Science and Literature overlap cannot exceed either club total."
            )

        # Check the overlap shared by all three clubs.
        if values["all_three"] > min(
            values["math_science"],
            values["math_literature"],
            values["science_literature"]
        ):
            raise ValueError(
                "The all-three intersection cannot exceed any pairwise intersection."
            )

        # Calculate students belonging to only one club.
        math_only = (
            values["math"]
            - values["math_science"]
            - values["math_literature"]
            + values["all_three"]
        )

        science_only = (
            values["science"]
            - values["math_science"]
            - values["science_literature"]
            + values["all_three"]
        )

        literature_only = (
            values["literature"]
            - values["math_literature"]
            - values["science_literature"]
            + values["all_three"]
        )

        # A club-only count cannot be negative.
        if math_only < 0:
            raise ValueError(
                "Math-only students would be negative; "
                "check Math Club and its overlaps."
            )

        if science_only < 0:
            raise ValueError(
                "Science-only students would be negative; "
                "check Science Club and its overlaps."
            )

        if literature_only < 0:
            raise ValueError(
                "Literature-only students would be negative; "
                "check Literature Club and its overlaps."
            )

        # Calculate the total number of unique students.
        total = count_three_sets(
            values["math"],
            values["science"],
            values["literature"],
            values["math_science"],
            values["math_literature"],
            values["science_literature"],
            values["all_three"]
        )

        # The total number of students cannot be negative.
        if total < 0:
            raise ValueError(
                "The calculated union of the three clubs cannot be negative."
            )

# Gets membership counts from the user and makes sure they
# are valid non-negative whole numbers.
def read_values(field_names):

    values = {}

    for key, label in field_names:

        # Keep asking until the user enters a valid value.
        while True:
            text = input(f"{label}: ").strip()

            try:
                value = int(text)
            except ValueError:
                print(
                    "Membership counts must be whole numbers. "
                    "Try again."
                )
                continue

            if value < 0:
                print(
                    "Membership counts cannot be negative. "
                    "Try again."
                )
                continue

            values[key] = value
            break

    return values

# Validates the values, calculates the union, and displays
# the result together with the Inclusion-Exclusion formula.
def calculate_and_print(mode, values):

    # Validate the entered values.
    try:
        validate_values(values, mode)
    except ValueError as error:
        print(f"\nCheck your inputs: {error}")
        return

    # Calculate the result for two clubs.
    if mode == "2 clubs":

        total = count_two_sets(
            values["math"],
            values["science"],
            values["math_science"]
        )

        formula = (
            f"{values['math']} + "
            f"{values['science']} - "
            f"{values['math_science']} = {total}"
        )

    # Calculate the result for three clubs.
    else:

        total = count_three_sets(
            values["math"],
            values["science"],
            values["literature"],
            values["math_science"],
            values["math_literature"],
            values["science_literature"],
            values["all_three"]
        )

        formula = (
            f"{values['math']} + "
            f"{values['science']} + "
            f"{values['literature']} - "
            f"{values['math_science']} - "
            f"{values['math_literature']} - "
            f"{values['science_literature']} + "
            f"{values['all_three']} = {total}"
        )

    # Display the result.
    print(f"\nTOTAL UNIQUE STUDENTS: {total} students")
    print(f"Inclusion-Exclusion: {formula}")

# Runs the main menu and controls the calculator.
def main():

    # Input fields for two clubs.
    two_club_fields = [
        ("math", "Math Club total"),
        ("science", "Science Club total"),
        ("math_science", "Math and Science overlap")
    ]

    # Input fields for three clubs.
    three_club_fields = two_club_fields + [
        ("literature", "Literature Club total"),
        ("math_literature", "Math and Literature overlap"),
        ("science_literature", "Science and Literature overlap"),
        ("all_three", "All three clubs overlap")
    ]

    print("-----------------------------------------------")
    print("😍😍😍 INCLUSION-EXCLUSION PRINCIPLE 😍😍😍")
    print("        Club Membership Calculator")
    print("-----------------------------------------------")
    print(
        "Calculate the number of unique students "
        "when memberships overlap."
    )
    # Main menu.
    while True:
        print("\n1. Calculate for two clubs")
        print("2. Calculate for three clubs")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            values = read_values(two_club_fields)
            calculate_and_print("2 clubs", values)

        elif choice == "2":
            values = read_values(three_club_fields)
            calculate_and_print("3 clubs", values)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please choose an option from 1 to 3.")

# PROGRAM START
if __name__ == "__main__":
    main()
