import pandas as pd
import analysis
import machine_learning
import visualisation

def load_data(file_path):
    """
    Load the data from a CSV file.

    Args:
        file_path (str): Path to CSV data file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def main():
    # Load the data
    data_file = 'sakura_first_bloom_dates.csv'
    df = load_data(data_file)

    # Reshape (melt!) and clean data
    df_cleaned = analysis.clean_data(df)
    df_melted = analysis.reshape_data(df_cleaned)

    # Perform analysis
    analysis.perform_analysis(df_melted)

    # Run basic linear regression
    machine_learning.run_machine_learning(df_cleaned)

    # Generate Sapporo visualizations
    visualisation.generate_visualizations(df_melted)

if __name__ == "__main__":
    main()
