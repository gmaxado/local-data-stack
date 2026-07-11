from dagster_dbt import DbtProject
from local_data_stack.config import get_project_root

dbt_project = DbtProject(
    project_dir= get_project_root() / 'transform'
)

dbt_project.prepare_if_dev()