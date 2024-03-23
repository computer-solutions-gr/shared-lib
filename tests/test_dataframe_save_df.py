import os
import pandas as pd
import pytest
from cssalib.dataframes import save_df

# Happy path tests with various realistic test values
@pytest.mark.parametrize("data, filename, test_id", [
    (pd.DataFrame({'a': [1, 2], 'b': [3, 4]}), "output1.pkl", "HP_1"),
    (pd.DataFrame({'x': [10], 'y': [20]}), "output2.pkl", "HP_2"),
    (pd.DataFrame(index=[0], columns=['empty']), "output3.pkl", "HP_3"),
])
def test_save_df_happy_path(tmp_path, data, filename, test_id):
    # Arrange
    file_path = tmp_path / filename

    # Act
    save_df(data, str(file_path))

    # Assert
    assert file_path.exists()
    assert pd.read_pickle(file_path).equals(data)

# Edge cases
@pytest.mark.parametrize("data, filename, test_id", [
    (pd.DataFrame(), "empty_df.pkl", "EC_1"),
    (pd.DataFrame({'a': []}), "empty_col_df.pkl", "EC_2"),
])
def test_save_df_edge_cases(tmp_path, data, filename, test_id):
    # Arrange
    file_path = tmp_path / filename

    # Act
    save_df(data, str(file_path))

    # Assert
    assert file_path.exists()
    assert pd.read_pickle(file_path).equals(data)

# Error cases
@pytest.mark.parametrize("data, filename, test_id", [
    (pd.DataFrame({'a': [1, 2]}), "/invalid/path/output.pkl", "ER_1"),
])
def test_save_df_error_cases(tmp_path, data, filename, test_id):
    # Arrange
    file_path = tmp_path / filename if "invalid" not in filename else filename
    # Act & Assert
    with pytest.raises(Exception):
        save_df(data, str(file_path))
