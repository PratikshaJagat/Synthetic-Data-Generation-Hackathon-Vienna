import json
import pandas as pd
from pathlib import Path

def validate_cluster_data(cluster_file_path, raw_data_path):
    """
    Validate that all original data is preserved in clustering.
    
    Args:
        cluster_file_path (Path): Path to cluster JSON file
        raw_data_path (Path): Path to original CSV file
        
    Returns:
        int: Number of matching vectors
    """
    # Load clustered data
    with open(cluster_file_path) as f:
        data = json.load(f)

    vectors_json = []
    for i in range(23):  # Assuming 23 clusters
        for j in range(len(data[str(i)])):
            x = data[str(i)][j]
            vectors_json.append(x)

    # Load original data
    df = pd.read_csv(raw_data_path)
    df.set_index(df.columns[0], inplace=True)

    vectors_df = []
    for col in df.columns:
        vectors_df.append(df[col].values.tolist())

    # Count matches
    matching_count = 0
    for vector in vectors_df:
        if vector in vectors_json:
            matching_count += 1

    print(f"Number of matching vectors: {matching_count}")
    return matching_count