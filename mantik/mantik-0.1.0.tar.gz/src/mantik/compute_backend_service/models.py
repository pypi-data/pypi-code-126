"""Request models."""
import pydantic


class SubmitRunResponse(pydantic.BaseModel):
    """
    Model for submitted run response.

    Attributes
    ----------
    experiment_id: Experiment id.
    run_id: Run id.
    """

    experiment_id: int
    run_id: str
