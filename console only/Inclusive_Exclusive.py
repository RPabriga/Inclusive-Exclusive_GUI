


def count_two_sets(first_size, second_size, shared_size):
    """Return the number of unique members in two overlapping sets."""
    return first_size + second_size - shared_size    # Add the two club totals. Then subtract the students who belong to both clubs.

def count_three_sets(first_size, second_size, third_size, first_second_size,
                     first_third_size, second_third_size, all_three_size):
    """Return the number of unique members in three overlapping sets."""
    return (first_size + second_size + third_size - first_second_size  # Apply the Inclusion-Exclusion formula.
            - first_third_size - second_third_size + all_three_size)

def validate_values(values, mode):
    """Check whether membership totals and overlaps are possible."""
    if values["math_science"] > min(values["math"], values["science"]): # Check if the Math and Science overlap is larger than either of the two club totals.
        raise ValueError("The Math and Science overlap cannot exceed either club total.")
    if mode == "2 clubs" and count_two_sets(   # If we are working with two clubs, calculate the total. The result should never be negative
            values["math"], values["science"], values["math_science"]) < 0:
        raise ValueError("The two-club total cannot be negative.")

    if mode == "3 clubs": # VALIDATION FOR THREE CLUBS
        if values["math_literature"] > min(values["math"], values["literature"]): # Check the Math & Literature overlap.
            raise ValueError("The Math and Literature overlap cannot exceed either club total.")
        if values["science_literature"] > min(values["science"], values["literature"]): # Check the Science & Literature overlap.
            raise ValueError("The Science and Literature overlap cannot exceed either club total.")
        if values["all_three"] > min(values["math_science"],
                                      values["math_literature"],
                                      values["science_literature"]):
            raise ValueError("The all-three intersection cannot exceed any pairwise intersection.")

        math_only = (values["math"] - values["math_science"]  # Students who belong to Math only.
                     - values["math_literature"] + values["all_three"])
        science_only = (values["science"] - values["math_science"]  # Students who belong to Science only.
                        - values["science_literature"] + values["all_three"])
        literature_only = (values["literature"] - values["math_literature"] # Students who belong to Literature only.
                           - values["science_literature"] + values["all_three"])
        
         # A club-only count cannot be negative.
        if math_only < 0:
            raise ValueError("Math-only students would be negative; check Math Club and its two overlaps.")
        if science_only < 0: 
            raise ValueError("Science-only students would be negative; check Science Club and its two overlaps.")
        if literature_only < 0: 
            raise ValueError("Literature-only students would be negative; check Literature Club and its two overlaps.")

        total = count_three_sets( # Calculate the total number of unique students belonging to the three clubs.
            values["math"], values["science"], values["literature"],
            values["math_science"], values["math_literature"],
            values["science_literature"], values["all_three"])
        if total < 0:  # The total should never be negative.
            raise ValueError("The calculated union of the three clubs cannot be negative.")


def read_values(field_names):
    """Read non-negative whole-number membership counts from the console."""
    values = {}
    for key, label in field_names: # Loop through every field that needs to be entered.
        while True: # Keep asking until the user enters a valid number.
            text = input(f"{label}: ").strip()
            try:
                value = int(text)
            except ValueError:
                print("Membership counts must be whole numbers. Try again.")
                continue
            if value < 0:
                print("Membership counts cannot be negative. Try again.")
                continue
            values[key] = value
            break
    return values


def calculate_and_print(mode, values):
    """Validate values, calculate the union, and print the result."""
    try:
        validate_values(values, mode)
    except ValueError as error:
        print(f"\nCheck your inputs: {error}")
        return

    if mode == "2 clubs":
        total = count_two_sets(values["math"], values["science"], values["math_science"])
        formula = f"{values['math']} + {values['science']} - {values['math_science']} = {total}"
    else:
        total = count_three_sets(
            values["math"], values["science"], values["literature"],
            values["math_science"], values["math_literature"],
            values["science_literature"], values["all_three"])
        formula = (f"{values['math']} + {values['science']} + {values['literature']} - "
                   f"{values['math_science']} - {values['math_literature']} - "
                   f"{values['science_literature']} + {values['all_three']} = {total}")

    print(f"\nTOTAL UNIQUE STUDENTS: {total} students")
    print(f"Inclusion-Exclusion: {formula}")


def main():
    """Run the console version of the inclusion-exclusion calculator."""
    case_one = {"math": 25, "science": 18, "math_science": 10}
    case_two = {"math": 20, "science": 15, "literature": 10,
                "math_science": 5, "math_literature": 3,
                "science_literature": 2, "all_three": 1}
    two_club_fields = [("math", "Math Club total"),
                       ("science", "Science Club total"),
                       ("math_science", "Math and Science overlap")]
    three_club_fields = two_club_fields + [
        ("literature", "Literature Club total"),
        ("math_literature", "Math and Literature overlap"),
        ("science_literature", "Science and Literature overlap"),
        ("all_three", "All three clubs overlap")]

    print("INCLUSION-EXCLUSION PRINCIPLE")
    print("Club Membership Calculator")
    print("Calculate the number of unique students when memberships overlap.")

    while True:
        print("\n1. Calculate for two clubs")
        print("2. Calculate for three clubs")
        print("3. Load Case 1")
        print("4. Load Case 2")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            calculate_and_print("2 clubs", read_values(two_club_fields))
        elif choice == "2":
            calculate_and_print("3 clubs", read_values(three_club_fields))
        elif choice == "3":
            calculate_and_print("2 clubs", case_one)
        elif choice == "4":
            calculate_and_print("3 clubs", case_two)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
