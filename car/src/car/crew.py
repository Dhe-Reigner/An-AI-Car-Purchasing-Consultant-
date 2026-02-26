from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Car():
    """Car crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def car_purchase_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['car_purchase_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def used_car_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['used_car_market_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def buyer_profiling_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['buyer_profiling_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def loan_risk_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['loan_risk_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def insurance_risk_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['insurance_risk_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reliability_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reliability_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def final_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['final_recommendation_agent'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def car_purchase_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['car_purchase_analysis'], # type: ignore[index]
        )

    @task
    def used_car_market_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['used_car_market_analysis'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def loan_risk_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['loan_risk_analysis'], # type: ignore[index]
        )

    @task
    def insurance_risk_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['insurance_risk_analysis'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def reliability_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['reliability_analysis'], # type: ignore[index]
        )

    @task
    def final_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config['final_recommendation'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Car crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
