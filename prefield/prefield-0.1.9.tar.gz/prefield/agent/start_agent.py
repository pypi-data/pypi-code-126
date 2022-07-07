import os

from prefect.agent.ecs import ECSAgent


def start_fargate_agent():
    ENV = os.getenv("ENV", "dev")
    agent_name = os.getenv("AGENT_NAME")

    print(f"Starting fargate agent `{agent_name}`")
    print("NOTE: this will register the agent with Prefect Cloud")

    env_vars = {"ENV": ENV, "PREFECT__BACKEND": "cloud"}
    ecs_agent = ECSAgent(
        name=agent_name,
        env_vars=env_vars,
        region_name=os.getenv("AWS_REGION"),
        cluster="prefect",
        launch_type="FARGATE",
    )
    ecs_agent.start()


if __name__ == "__main__":
    start_fargate_agent()
