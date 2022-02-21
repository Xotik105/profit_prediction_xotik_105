import pytest

from regression_model.config_base.core_test import config
from regression_model.processing.data_manager import load_dataset


@pytest.fixture()
def sampl_input_data():
    return load_dataset(file_name=config.app_config.test_data_name)