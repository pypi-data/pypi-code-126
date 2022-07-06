"""
"""

import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

# =================================
# BROAD 10X
# =================================

BROAD_TENX_SAMPLE_METADATA_PATH = PACKAGE_DIR / 'files/BROAD.TENX.SampleMetadata.csv.gz'
BROAD_TENX_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/BROAD_TENX/BROAD.TENX.ordered.zarr'
BROAD_TENX_CELL_TYPE_ANNOTATION_PATH = '/gale/netapp/cemba3c/BICCN/wmb/broad/BROAD.TENX.Annotations.zarr'
BROAD_TENX_OUTLIER_IDS_PATH = PACKAGE_DIR / 'files/BROAD.TENX.DoubletsID.txt.gz'

# gene metadata
BROAD_TENX_GENE_MAP_PATH = PACKAGE_DIR / 'files/BROAD.TENX.GeneMap.csv'
