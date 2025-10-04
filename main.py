from acids import get_amino_acid

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <one-letter amino acid code>")
        sys.exit(1)

    code = sys.argv[1]
    try:
        aa = get_amino_acid(code)
        print(f"One-letter: {aa.one_letter}")
        print(f"Three-letter: {aa.three_letter}")
        print(f"Full name: {aa.full_name}")
        print(f"Essential: {'Yes' if aa.essential else 'No'}")
        print(f"Conditionally essential: {'Yes' if aa.conditionally_essential else 'No'}")
    except KeyError:
        print(f"Unknown amino acid code: {code}")
        sys.exit(1)
