from dataclasses import dataclass
from typing import Dict
import math


@dataclass(frozen=True)
class AminoAcid:
    one_letter: str
    three_letter: str
    full_name: str
    essential: bool = False
    conditionally_essential: bool = False
    daily_requirement_g: float = math.nan
    human_body_percentage: float = math.nan

    @classmethod
    def total_human_body_percentage(cls) -> float:
        """Sum all known human_body_percentage values from the module registry, ignoring NaN."""
        total = 0.0
        for aa in amino_acids.values():
            p = aa.human_body_percentage
            if not math.isnan(p):
                total += p
        return total


# registry mapping single-letter code -> AminoAcid instance
amino_acids: Dict[str, AminoAcid] = {
    "A": AminoAcid("A", "Ala", "Alanine", daily_requirement_g=1.0, human_body_percentage=8.5),
    "R": AminoAcid(
        "R", "Arg", "Arginine", conditionally_essential=True, daily_requirement_g=2.5, human_body_percentage=5.1
    ),
    "N": AminoAcid("N", "Asn", "Asparagine", daily_requirement_g=math.nan, human_body_percentage=4.4),
    "D": AminoAcid("D", "Asp", "Aspartic Acid", daily_requirement_g=math.nan, human_body_percentage=5.3),
    "C": AminoAcid("C", "Cys", "Cysteine", daily_requirement_g=1.0, human_body_percentage=1.6),
    "E": AminoAcid("E", "Glu", "Glutamic Acid", daily_requirement_g=math.nan, human_body_percentage=12.3),
    "Q": AminoAcid("Q", "Gln", "Glutamine", daily_requirement_g=math.nan, human_body_percentage=4.0),
    "G": AminoAcid("G", "Gly", "Glycine", daily_requirement_g=1.5, human_body_percentage=7.2),
    "H": AminoAcid("H", "His", "Histidine", essential=True, daily_requirement_g=0.7, human_body_percentage=2.1),
    "I": AminoAcid("I", "Ile", "Isoleucine", essential=True, daily_requirement_g=1.4, human_body_percentage=5.0),
    "L": AminoAcid("L", "Leu", "Leucine", essential=True, daily_requirement_g=2.7, human_body_percentage=9.0),
    "K": AminoAcid("K", "Lys", "Lysine", essential=True, daily_requirement_g=2.1, human_body_percentage=6.9),
    "M": AminoAcid("M", "Met", "Methionine", essential=True, daily_requirement_g=1.1, human_body_percentage=2.3),
    "F": AminoAcid("F", "Phe", "Phenylalanine", essential=True, daily_requirement_g=1.8, human_body_percentage=3.9),
    "P": AminoAcid("P", "Pro", "Proline", daily_requirement_g=math.nan, human_body_percentage=5.1),
    "S": AminoAcid("S", "Ser", "Serine", daily_requirement_g=math.nan, human_body_percentage=6.9),
    "T": AminoAcid("T", "Thr", "Threonine", essential=True, daily_requirement_g=1.1, human_body_percentage=4.5),
    "W": AminoAcid("W", "Trp", "Tryptophan", essential=True, daily_requirement_g=0.28, human_body_percentage=1.2),
    "Y": AminoAcid("Y", "Tyr", "Tyrosine", daily_requirement_g=math.nan, human_body_percentage=3.2),
    "V": AminoAcid("V", "Val", "Valine", essential=True, daily_requirement_g=1.8, human_body_percentage=7.0),
}


def get_amino_acid(letter: str) -> AminoAcid:
    """Return AminoAcid by one-letter code (uppercase). Raises KeyError if unknown."""
    return amino_acids[letter.upper()]
