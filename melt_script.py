#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 2021

@author: Jesse Sallis

"""


def custom_melt(df, id_vars, value_vars, value_name="Value", var_name="Variable"):
    import pandas as pd

    """
    Given a dataframe, an identifier variable and value variables return a dataframe that has been
    melted by the value variables and rename columns based on string input.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        The dataframe to sample from
    id_vars : list 
        The columns to act as identifier variables
    value_vars : list
        The columns to be unpivoted
    value_name : str, optional
        Name of value column within melted df. Default is 'Value'      
    var_name : str, optional
        Name of variable column within melted df. Default is 'Variable'
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and the result of the action applied.
        
    Raises
    ------
    TypeError
        If the input argument df is not of type pandas.core.frame.DataFrame
    TypeError
        If the input argument id_vars and value_vars are not of type list
    TypeError
        If the input argument value_name and var_name are not of type string
        
    AssertError
        If the input argument id_vars are not in the data columns
    AssertError
        If the input argument value_vars are not in the data columns
    
    Examples
    --------
    >>> custom_melt(sales_data,['Quarter'],['Revenue','Units'],'Sales', 'Metric')
	Quarter	Metric  Sales
	1       Revenue 100	 
    1	    Units   2

    """

    # check if dataframe is being based as first arguement
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # check if list is being passed as id_vars and value_vars arguement
    if not isinstance([id_vars, value_vars], list):
        raise TypeError("The data arguement for id_vars/value_vars is not of type list")

    # check if naming arguements are being based as type string
    if type(value_name) is not str and type(var_name) is not str:
        raise TypeError("The data arguement for column names is not of type string")

    # confirming input columns are in df
    for i in id_vars:
        assert i in df.columns, "The ID column does not exist in df"
    for i in value_vars:
        assert i in df.columns, "The Value column does not exist in df"

    # melting dataframe
    melt = df.melt(
        id_vars=id_vars, value_vars=value_vars, value_name=value_name, var_name=var_name
    )

    # return melted df
    return melt
