from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Paths:
    ROOT: Path = Path(__file__).resolve().parents[2]
    DATA: Path = ROOT / "src" / "data"
    ARTIFACTS: Path = DATA / "artifacts"
    MODELS: Path = ARTIFACTS / "models"
    REPORTS: Path = ARTIFACTS / "reports"