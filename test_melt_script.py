#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 28 2021

@author: Jesse Sallis

This function creates a sample data to test the melt script created for the Python Programming for Data Science final project.
"""

from melt_script import custom_melt
import pandas as pd


def test_custom_melt():

    # Create sample df and write tests for the function
    raw_data = {
        "Quarter": [1, 2, 3, 4],
        "Revenue": [100, 200, 400, 100],
        "Units": [2, 4, 8, 2],
    }

    sample_data = pd.DataFrame.from_dict(raw_data)

    test_df = custom_melt(
        sample_data, ["Quarter"], ["Revenue", "Units"], "Sales", "Metric"
    )

    assert test_df.shape == (8, 3)
    assert test_df["Sales"].sum() == 816
    assert test_df["Metric"].nunique() == 2
