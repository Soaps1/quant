def monty_python_probabilities(n):
    if n < 3:
        raise ValueError("Number of doors must be at least 3.")

    # Probability of winning if you stick: you picked the prize initially
    prob_stick = 1 / n

    # Probability of winning if you switch: you picked a non-prize door,
    # and after host opens n-2 empty doors, you switch to the other unopened door
    prob_switch = (n - 1) / n

    return {'stick': prob_stick, 'switch': prob_switch}

def main():
    try:
        n = int(input("Enter the number of doors (at least 3): "))
        result = monty_python_probabilities(n)
        print(f"Probability of winning if you stick: {result['stick']:.4f}")
        print(f"Probability of winning if you switch: {result['switch']:.4f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()