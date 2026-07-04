from pathlib import Path

def get_project_root() -> Path:

    # Start from the current file's directory
    current_path = Path(__file__).resolve()
    
    # Loop through parent directories
    for parent in current_path.parents:
        if (parent / 'pyproject.toml').exists():
            return parent
            
    # Fallback to the current file's parent if no marker is found
    return current_path.parent

def get_data_layer_paths() -> dict[str, Path]:

    # Root
    project_root = get_project_root()

    # Data
    data_folder = (project_root / 'data')

    # Data layers - raw, bronze, silver, gold
    data_layers = {layer: data_folder / layer for layer in ['raw','bronze','silver','gold']}

    # Check/create folders in case they don't exist
    for layer, path in data_layers.items():
        path.mkdir(parents=True, exist_ok=True)

    return data_layers