from dataclasses import dataclass
from pathlib import Path

# THis is not the original data class, this decorator is being created for bulding my own custom return types.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
