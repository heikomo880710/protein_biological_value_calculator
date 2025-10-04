from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class AminoAcid:
    one_letter: str
    three_letter: str
    full_name: str
    essential: bool = False
    conditionally_essential: bool = False
    daily_requirement_g: Optional[float] = None


# registry mapping single-letter code -> AminoAcid instance
amino_acids: Dict[str, AminoAcid] = {
    "A": AminoAcid("A", "Ala", "Alanine", daily_requirement_g=1.0),
    "R": AminoAcid("R", "Arg", "Arginine", conditionally_essential=True, daily_requirement_g=2.5),
    "N": AminoAcid("N", "Asn", "Asparagine", daily_requirement_g=None),
    "D": AminoAcid("D", "Asp", "Aspartic Acid", daily_requirement_g=None),
    "C": AminoAcid("C", "Cys", "Cysteine", daily_requirement_g=1.0),
    "E": AminoAcid("E", "Glu", "Glutamic Acid", daily_requirement_g=None),
    "Q": AminoAcid("Q", "Gln", "Glutamine", daily_requirement_g=None),
    "G": AminoAcid("G", "Gly", "Glycine", daily_requirement_g=1.5),
    "H": AminoAcid("H", "His", "Histidine", essential=True, daily_requirement_g=0.7),
    "I": AminoAcid("I", "Ile", "Isoleucine", essential=True, daily_requirement_g=1.4),
    "L": AminoAcid("L", "Leu", "Leucine", essential=True, daily_requirement_g=2.7),
    "K": AminoAcid("K", "Lys", "Lysine", essential=True, daily_requirement_g=2.1),
    "M": AminoAcid("M", "Met", "Methionine", essential=True, daily_requirement_g=1.1),
    "F": AminoAcid("F", "Phe", "Phenylalanine", essential=True, daily_requirement_g=1.8),
    "P": AminoAcid("P", "Pro", "Proline", daily_requirement_g=None),
    "S": AminoAcid("S", "Ser", "Serine", daily_requirement_g=None),
    "T": AminoAcid("T", "Thr", "Threonine", essential=True, daily_requirement_g=1.1),
    "W": AminoAcid("W", "Trp", "Tryptophan", essential=True, daily_requirement_g=0.28),
    "Y": AminoAcid("Y", "Tyr", "Tyrosine", daily_requirement_g=None),
    "V": AminoAcid("V", "Val", "Valine", essential=True, daily_requirement_g=1.8),
}


def get_amino_acid(letter: str) -> AminoAcid:
    """Return AminoAcid by one-letter code (uppercase). Raises KeyError if unknown."""
    return amino_acids[letter.upper()]
