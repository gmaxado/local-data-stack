import great_expectations as gx
from great_expectations.data_context import FileDataContext
from local_data_stack.config import get_project_root

def get_quality_context() -> FileDataContext:
    root = get_project_root()
    quality_path = root / "quality"
    quality_path.mkdir(parents=True, exist_ok=True)
    
    context = gx.get_context(
        mode="file", 
        project_root_dir=quality_path,
    )

    return context