import unittest
from pandas import DataFrame
from cssalib.dataframes import save_df
import os
import pandas as pd


class TestSaveDF(unittest.TestCase):

    def setUp(self):
        self.test_df = DataFrame({"col1": [1, 2], "col2": [3, 4]})
        self.filename = "test.pkl"

    def tearDown(self):
        # Delete file after test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_df_basic(self):
        # Save DF
        save_df(self.test_df, self.filename)

        # Check file was created
        self.assertTrue(os.path.exists(self.filename))

        # Load saved DF and check equality
        saved_df = pd.read_pickle(self.filename)
        self.assertTrue(self.test_df.equals(saved_df))

    def test_save_df_default_filename(self):
        # Save with default filename
        save_df(self.test_df)

        # Check default file was created
        self.assertTrue(os.path.exists("test.pkl"))

        # Load and check equality
        default_df = pd.read_pickle("test.pkl")
        self.assertTrue(self.test_df.equals(default_df))

    def test_save_df_invalid_path(self):
        # Try to save to invalid path
        invalid_path = "/invalid/path/test.pkl"
        with self.assertRaises(Exception):
            save_df(self.test_df, invalid_path)
