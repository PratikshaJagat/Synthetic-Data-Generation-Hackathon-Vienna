import json
import numpy as np
import matplotlib.pyplot as plt
import umap
from pathlib import Path


# # Load clusters from JSON using relative path
# data_dir = Path(__file__).parent.parent / 'data' / 'processed' / 'clusters'
# cluster_file = data_dir / 'cluster_daily_FullYear.json'


# # Load clusters from JSON
# with open(cluster_file, 'r') as f:
#     clusters = json.load(f)

# # Convert clusters to array format
# cluster_arrays = []
# labels = []
# for cluster_id, vectors in clusters.items():
#     cluster_arrays.extend(vectors)
#     labels.extend([int(cluster_id)] * len(vectors))

# # Reduce dimensionality with UMAP
# reducer = umap.UMAP(random_state=42)
# reduced_data = reducer.fit_transform(cluster_arrays)

# # Plot clusters
# plt.figure(figsize=(12,8))
# scatter = plt.scatter(reduced_data[:,0], reduced_data[:,1], c=labels, cmap='tab20', alpha=0.6)
# plt.colorbar(scatter)
# plt.title('Cluster Visualization using UMAP')
# plt.xlabel('UMAP Dimension 1')
# plt.ylabel('UMAP Dimension 2') 
# plt.show()


def plot_cluster_umap(cluster_file_path, output_dir=None):
    """
    Create UMAP visualization of clusters.
    
    Args:
        cluster_file_path (Path): Path to cluster JSON file
        output_dir (Path, optional): Directory to save plot
    """
    # Load clusters from JSON
    with open(cluster_file_path, 'r') as f:
        clusters = json.load(f)

    # Convert clusters to array format
    cluster_arrays = []
    labels = []
    for cluster_id, vectors in clusters.items():
        cluster_arrays.extend(vectors)
        labels.extend([int(cluster_id)] * len(vectors))

    # Reduce dimensionality with UMAP
    reducer = umap.UMAP(random_state=42)
    reduced_data = reducer.fit_transform(cluster_arrays)

    # Plot clusters
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], 
                         c=labels, cmap='tab20', alpha=0.6)
    plt.colorbar(scatter)
    plt.title('Cluster Visualization using UMAP')
    plt.xlabel('UMAP Dimension 1')
    plt.ylabel('UMAP Dimension 2')
    
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_dir / 'cluster_umap.png', dpi=300, bbox_inches='tight')
    
    plt.show()