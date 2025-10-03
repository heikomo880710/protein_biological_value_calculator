from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class AminoAcid:
    one_letter: str
    three_letter: str
    full_name: str
    essential: bool = False
    conditionally_essential: bool = False
    comment: Optional[str] = None


# registry mapping single-letter code -> AminoAcid instance
amino_acids: Dict[str, AminoAcid] = {
    "A": AminoAcid("A", "Ala", "Alanine"),
    "R": AminoAcid(
        "R",
        "Arg",
        "Arginine",
        conditionally_essential=True,
        comment="conditionally essential",
    ),
    "N": AminoAcid("N", "Asn", "Asparagine"),
    "D": AminoAcid("D", "Asp", "Aspartic Acid"),
    "C": AminoAcid("C", "Cys", "Cysteine"),
    "E": AminoAcid("E", "Glu", "Glutamic Acid"),
    "Q": AminoAcid("Q", "Gln", "Glutamine"),
    "G": AminoAcid("G", "Gly", "Glycine"),
    "H": AminoAcid("H", "His", "Histidine", essential=True),
    "I": AminoAcid("I", "Ile", "Isoleucine", essential=True),
    "L": AminoAcid("L", "Leu", "Leucine", essential=True),
    "K": AminoAcid("K", "Lys", "Lysine", essential=True),
    "M": AminoAcid("M", "Met", "Methionine", essential=True),
    "F": AminoAcid("F", "Phe", "Phenylalanine", essential=True),
    "P": AminoAcid("P", "Pro", "Proline"),
    "S": AminoAcid("S", "Ser", "Serine"),
    "T": AminoAcid("T", "Thr", "Threonine", essential=True),
    "W": AminoAcid("W", "Trp", "Tryptophan", essential=True),
    "Y": AminoAcid("Y", "Tyr", "Tyrosine"),
    "V": AminoAcid("V", "Val", "Valine", essential=True),
}


def get_amino_acid(letter: str) -> AminoAcid:
    """Return AminoAcid by one-letter code (uppercase). Raises KeyError if unknown."""
    return amino_acids[letter.upper()]


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
        if aa.comment:
            print(f"Comment: {aa.comment}")
    except KeyError:
        print(f"Unknown amino acid code: {code}")
        sys.exit(1)
