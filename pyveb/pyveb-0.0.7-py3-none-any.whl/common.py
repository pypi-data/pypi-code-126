import os
import yaml
import inspect
from datetime import date, datetime
import logging
import sys

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_config(): 
    """
        RETURN
            config object enabling fetching of config from config.yml via dot notation

        ADDITIONAL INFO
            In docker image we copy config file into current dir, for local development we fetch config from level lower
    """
    caller_file = os.path.dirname(inspect.stack()[1].filename)
    try: 
        with open(caller_file + '/config.yml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
    except:
        with open(caller_file + '/../config.yml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
    config = dotdict(config)
    return config


def create_partition_key(partition_date:str) -> str:
    """
        ARGUMENT
            partition_date: date of airflow task start date. eg 2020-01-01 12:00
        
        RETURN
            year=2020/month=01/day=01/    
    """
    format = "%Y-%m-%d"
    if not isinstance(partition_date, date):
        partition_date = datetime.strptime(partition_date, format)
    day = '{:02d}'.format(partition_date.day)
    month = '{:02d}'.format(partition_date.month)
    year = partition_date.year
    return f"year={year}/month={month}/day={day}/"



def get_args(args):
    """
        ARGUMENTS
            args: sys.args

        RETURNS
            env, pipeline_type, partition_start, partition_start, partition_key

        ADDITIONAL INFO
            Command line args are passed to python programs via airflow dag - AWS Batchoperator - Overrides - Command  
            These args are then passed to our program via entrypoint.sh via $@

            Env, pipeline type and partition start ( ie. airflow task start date) are mandatory for incremental/full pipelines.
            For incremental pipeline, additionally we require a partition end date. 
    """
    try: 
        env = args[1]
        pipeline_type = args[2]
        assert env in ['local', 'dev', 'prd']
        assert pipeline_type in ['full', 'incremental']
        logging.info(f"Environment: {env}")
        logging.info(f"Pipeline type: {pipeline_type}")
    except AssertionError as e:
        logging.error("Incorrect environment or pipeline type argument passed. Exiting...")
        logging.error(e)
        sys.exit(1)
    except Exception:
        logging.error("No environment argument passed. Exiting...")
        sys.exit(1)

    # fetch airflow partition(s)
    try:
        format = "%Y-%m-%d"
        partition_start = args[3]
        try:
            is_valid_start = bool(datetime.strptime(partition_start, format))
        except:
            is_valid_start = False
        assert is_valid_start
        logging.info(f"Partition start: {partition_start}")
        if pipeline_type == 'incremental':
            partition_end = args[4]
            try:
                is_valid_end = bool(datetime.strptime(partition_end, format))
            except:
                is_valid_end= False
            assert is_valid_end
            logging.info(f"Partition end: {partition_end}")
        else:
            partition_end = None
        partition_key = create_partition_key(partition_start)
    except AssertionError as e:
        logging.error("Incorrect partition date argument passed. Dates must be passed as YYYY-MM-DD Exiting...")
        logging.error(e)
        sys.exit(1)
    except: 
        logging.error("No partition date arguments passed. Exiting")
        logging.info("Pass partition start and partition end date arguments as postional arguments 2 and 3")
        sys.exit(1)
    return env, pipeline_type, partition_start, partition_end, partition_key