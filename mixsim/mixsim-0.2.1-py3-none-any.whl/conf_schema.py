from enum import Enum
from pathlib import Path
from typing import Callable, Optional

from pydantic import validator, BaseModel, Field, FilePath


class Backend(str, Enum):
    pyroomacoustics = "pyroomacoustics"
    gpuRIR = "gpuRIR"


class SourceLoaderStyle(str, Enum):
    map = "map"  # ensure to map all the source files.
    iter = "iter"  # iterate over the source files.


class SourceLoader(BaseModel):
    """Source loader configuration."""
    fpath_file: FilePath = Field(
        default=...,
        description="Path to a file containing a list of paths to clean wav files."
    )
    num_sources: int = Field(
        default=1,
        description="Number of sources to be generated each time. "
                    "If it is larger than one, You must specify ``collect_spk_id_fn``."
    )
    offset: int = Field(
        default=0,
        description="Number of files to be skipped."
    )
    limit: Optional[int] = Field(
        default=None,
        description="Number of files to be loaded."
    )
    sample_rate: int = Field(
        default=16000,
        description="Sampling rate."
    )
    parallel_load: bool = Field(
        default=False,
        description="Whether to load data in parallel."
    )
    shuffle: bool = Field(
        default=True,
        description="Whether to shuffle the dataset."
    )
    include_vad: bool = Field(
        default=True,
        description="Whether to include VAD information."
    )
    max_norm: bool = Field(
        default=True,
        description="Whether to normalize the waveform."
    )
    use_cache: bool = Field(
        default=False,
        description="Whether to use cache."
    )
    cache_args: dict = Field(
        default_factory=dict,
        description="Arguments of the cache."
    )
    collect_id_fn: Optional[Callable[[Path], str]] = Field(
        default=None,
        description="Function to collect source id."
    )
    collect_spk_id_fn: Optional[Callable[[Path], str]] = Field(
        default=None,
        description="Function to collect speaker id."
    )
    style: SourceLoaderStyle = Field(
        SourceLoaderStyle.iter,
        description="Style of the dataloader, e.g., ``map`` or ``iter``."
    )

    @validator("num_sources")
    def check_num_sources(cls, v):
        if v > 1:
            assert cls.collect_spk_id_fn is not None, "You must specify a ``collect_spk_id_fn`` for generate spk id."
        return v


class Mixer(BaseModel):
    """Mixing configuration."""
    snr_list: list = Field(
        default=[0.0],
        description="List of SNR in dB."
    )
    sir_list: list = Field(
        default=[0.0],
        description="List of SIR in dB."
    )
    loudness_level: float = Field(
        default=-25.0,
        le=0,
        description="Target loudness in dB."
    )
    loudness_floating: float = Field(
        default=5.0,
        description="Loudness floating in dB."
    )
    mix_mode: str = Field(
        default="min",
        description="Mixing mode."
    )


class RIRSimulator(BaseModel):
    """RIR simulator configuration."""
    array_arch: list[float] = Field(
        default_factory=list,
        description="Array architecture."
    )
    t60_range: list[float] = Field(
        default_factory=list,
        description="T60 range. [min, max]"
    )
    room_size: list[float] = Field(
        default_factory=list,
        description="Room size. ([x_min, y_min, z_min], [x_max, y_max, z_max])"
    )
    room_absorption_coefficient: list[float] = Field(
        default_factory=list,
        description="Room absorption coefficient. ([x_min, y_min, z_min], [x_max, y_max, z_max])"
    )
    min_allowable_distance_to_wall: float = Field(
        default=0.1,
        description="Minimum allowable distance to wall, in meters."
    )
    trajectory_types: list[str] = Field(
        default_factory=list,
        description="List of trajectory types, e.g., static, sine, etc."
    )
    use_elevation_angle: bool = Field(
        default=False,
        description="Whether to use elevation angle."
    )
    use_distance: bool = Field(
        default=False,
        description="Whether to use distance."
    )
    rir_interval: float = Field(
        default=0.1,
        description="Interval of RIRs, in seconds."
    )
    split_rir: bool = Field(
        default=False,
        description="Whether to split RIRs."
    )
    early_path_length: float = Field(
        default=0.05,
        description="The length of early-path part of RIR, in seconds. If ``split_rir`` is True, "
    )
    angle_dist: list = Field(
        default_factory=list,
        description="Angle distribution."
    )
    backend: Backend = Field(
        default=Backend.gpuRIR,
        description="Select a backend for RIR simulator, e.g., pyroomacoustics or gpuRIR."
    )

    @validator("backend")
    def check_backend(cls, v) -> Backend:
        if v not in Backend:
            raise ValueError(f"{v} is not a valid backend.")
        return v


class Config(BaseModel):
    """Configuration schema."""
    seed: int = Field(
        default=1,
        description="Random seed for numpy, random, etc."
    )
    sample_rate: int = Field(
        default=16000,
        description="Sampling rate."
    )
    clean: SourceLoader = Field(
        default_factory=SourceLoader,
        description="Clean source loader."
    )
    noise: SourceLoader = Field(
        default_factory=SourceLoader,
        description="Noise source loader."
    )
    mixer: Mixer = Field(
        default_factory=Mixer,
        description="Mixing parameters."
    )
    rir_simulator: RIRSimulator = Field(
        default_factory=RIRSimulator,
        description="RIR simulator."
    )
