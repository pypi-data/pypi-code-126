from more_itertools import first_true
from datetime import datetime
import time
import re
from tonic_api.services.jobs import JobService
from tonic_api.services.models import ModelService
from tonic_api.classes.trained_model import TrainedModel
from tonic_api.classes.model import Model
from tonic_api.classes.httpclient import HttpClient


class TrainingJob:
    """Class for retrieving info and model objects from a Tonic training job.
    
    Parameters
    ----------
    id : str
        Tonic job id.
    workspace_id: str
        Tonic workspace id.
    published_time : str
        Time the training job began.
    client : HttpClient
        Client being used to make requests to Tonic.
    """

    def __init__(self, id: str, workspace_id: str, published_time, client: HttpClient):
        self.id = id
        self.workspace_id = workspace_id
        self.published_time = published_time
        self.client = client
        self.job_service = JobService(client)
        self.model_service = ModelService(client)

    def get_training_status(self):
        """Return the training status of the job.
        
        Returns
        -------
        TrainingStatus
        """
        job = self.job_service.get_job_status(self.id)
        return TrainingStatus(job)

    def tail_training_status(self):
        """Print training status every ~5 seconds until the training job is done.

        Examples
        --------
        >>> training_job.tail_training_status()
        [07/06/22 15:27:50] Training status: Running your_model (905/3000 epochs completed)
        [07/06/22 15:28:00] Training status: Running your_model (906/3000 epochs completed)
        [07/06/22 15:28:16] Training status: Running your_model (907/3000 epochs completed)
        [07/06/22 15:28:32] Training status: Running your_model (908/3000 epochs completed)
        """
        status = None
        status_messages = []
        last_epoch_metadata_by_model = {}
        while status is None or status.state != "Completed":
            status = self.get_training_status()

            if status.state == "Completed":
                # Show the final epoch training status on completion
                (
                    status_messages,
                    last_epoch_metadata_by_model,
                ) = self.__handle_epoch_updates(
                    status, last_epoch_metadata_by_model, True
                )
                status_messages.append("Training completed")
                break
            elif status.state == "Failed":
                status_messages = ["Training failed: " + status.error]
                break
            elif status.state == "Canceled":
                status_messages = ["Training was canceled by user"]
                break
            elif status.state == "Running":
                (
                    status_messages,
                    last_epoch_metadata_by_model,
                ) = self.__handle_epoch_updates(status, last_epoch_metadata_by_model)
            else:
                status_messages = ["Training status: " + status.state]

            self.__print_with_timestamp(status_messages)

            time.sleep(5)

        # Last message(s)
        self.__print_with_timestamp(status_messages)

    def get_trained_models(self):
        """Retrieve the models trained by the training job.

        Returns
        -------
        List[Model]
        """
        trained_models = self.model_service.get_trained_models(self.id)
        return [
            self.__convert_to_trained_model(trained_model)
            for trained_model in trained_models
        ]

    def get_trained_model_by_model_id(self, model_id: str) -> Model:
        """Retrieve Model object from the model id.

        Parameters
        ----------
        model_id: str
            Model id number.
        
        Returns
        -------
        Model
        """
        trained_models_json = self.model_service.get_trained_models(self.id)
        trained_models = [
            self.__convert_to_trained_model(trained_model)
            for trained_model in trained_models_json
        ]
        trained_model = first_true(
            trained_models, pred=lambda tm: tm.model.id == model_id
        )
        if trained_model is None:
            raise Exception("No model with ID " + model_id + " found")
        return trained_model

    def get_trained_model_by_model_name(self, model_name: str) -> Model:
        """Retrieve Model object from the model name.

        Parameters
        ----------
        model_name: str
            Model name.
        
        Returns
        -------
        Model
        """
        trained_models_json = self.model_service.get_trained_models(self.id)
        trained_models = [
            self.__convert_to_trained_model(trained_model)
            for trained_model in trained_models_json
        ]
        trained_model = first_true(
            trained_models, pred=lambda tm: tm.model.name == model_name
        )
        if trained_model is None:
            raise Exception("No model with name " + model_name + " found")
        return trained_model

    def describe(self):
        """Print training job id, published time, and workspace id."""
        print(
            "Training Job: " + self.id + " [Published at " + self.published_time + "]"
        )
        print("Workspace ID: " + self.workspace_id)

    def __convert_to_trained_model(self, model_json):
        return TrainedModel(
            model_json["modelTrainingId"],
            self.id,
            self.workspace_id,
            Model(model_json["modelId"], model_json["model"]),
            self.client,
        )

    def __print_with_timestamp(self, messages):
        now = datetime.now().strftime("%D %H:%M:%S")
        for message in messages:
            print("[" + now + "] " + message)

    def __handle_epoch_updates(
        self, status, last_epoch_metadata_by_model, update_existing_only=False
    ):
        status_messages = []

        epoch_metadata_by_model = status.current_epoch_progress()
        if epoch_metadata_by_model is not None:
            for model, epoch_metadata in epoch_metadata_by_model.items():
                # Only print when epoch has updated
                if not update_existing_only and (
                    model not in last_epoch_metadata_by_model
                    or epoch_metadata[0] != last_epoch_metadata_by_model[model][0]
                ):
                    status_messages.append(
                        "Training status: Running "
                        + model
                        + " ("
                        + epoch_metadata[0]
                        + "/"
                        + epoch_metadata[1]
                        + " epochs completed)"
                    )
                    last_epoch_metadata_by_model[model] = epoch_metadata
                elif (
                    update_existing_only
                    and model in last_epoch_metadata_by_model
                    and epoch_metadata[0] != last_epoch_metadata_by_model[model][0]
                ):
                    status_messages.append(
                        "Training status: Running "
                        + model
                        + " ("
                        + epoch_metadata[0]
                        + "/"
                        + epoch_metadata[1]
                        + " epochs completed)"
                    )
                    last_epoch_metadata_by_model[model] = epoch_metadata
        else:
            status_messages = [
                "Training status: Running (no training tasks reported yet)"
            ]

        return status_messages, last_epoch_metadata_by_model


class TrainingStatus:
    """Keeps track of information about the status of a training job.

    Parameters
    ----------
    job_json : dict
    """
    def __init__(self, job_json: dict):
        self.state = job_json["status"]
        self.error = job_json["errorMessages"] if "errorMessages" in job_json else None
        self.tasks = job_json["tasks"] if "tasks" in job_json else None

    def current_epoch_progress(self) -> dict:
        """If the job is currently training, returns the epoch the training job is on.
        
        Returns
        -------
        dict
        """
        epoch_metadata_by_model = {}
        if self.tasks is not None:
            epoch_tasks = [
                task
                for task in self.tasks
                if "Training AI Synthesizer Model" in task["action"]
            ]
            for task in epoch_tasks:
                regex = re.match(
                    "^Training AI Synthesizer Model for (\w+)$", task["action"]
                )
                if regex is not None:
                    model_name = regex.group(1)
                    if "stepsCompleted" in task and "totalSteps" in task:
                        epoch_metadata_by_model[model_name] = (
                            str(task["stepsCompleted"]),
                            str(task["totalSteps"]),
                        )
            return epoch_metadata_by_model
        return None

    def describe(self):
        """Print job status."""
        print("Job status: " + self.state)
        if self.error is not None:
            print('Job failed due to: "' + self.error + '"')
