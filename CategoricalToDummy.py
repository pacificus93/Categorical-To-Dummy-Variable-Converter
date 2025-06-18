import pandas as pd

"""
Short Description:

The following code helps to replace categorical variable columns with dummy variable columns.

The function works only with data file in csv format.

As the result, you will get new csv format document within the path destination, that you have specified.

Input: original_path - original file full path;
       destination_path - full path for new file to be saved in;
       category_columns - columns within the file, that you have defined, as categorical.
"""

def Categorical_Dummy_Variable_Converter (original_path,destination_path,category_columns = []):
    #Turn CSV data into dataframe form
    df = pd.read_csv(original_path)
    
    #Get the names of the columns
    columns = df.columns
    
    #Turn each categorical variables into dummy variables (in a dataframe form), related to it
    dummy_variables = [pd.get_dummies(df[variable],dtype = int) for variable in category_columns]
    
    #Create empty dataframe
    new_df = pd.DataFrame()
    
    #Add columns from original dataframe, but replace each categorical column with dummy variable columns related to it
    for column in columns:
        if column in category_columns:
            for dv_column in dummy_variables[category_columns.index(column)].columns:
                new_df.loc[:,"{0}".format(dv_column)] = dummy_variables[category_columns.index(column)][dv_column]
            continue
        new_df.loc[:,"{0}".format(column)] = df[column]
    
    #Save it, as CSV file
    new_df.to_csv(destination_path, index = False)

if __name__=='__main__':
    Categorical_Dummy_Variable_Converter("original_pathway\\file.csv","destination_pathway\\file.csv",['Column1','Column2','Column3'])
