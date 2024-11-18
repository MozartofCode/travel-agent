#!/usr/bin/env python
import sys
from travel_agent.src.travel_agent.crew import TravelAgentCrew

def create_report(starting_point: str, destination: str, start_date: str, end_date: str):
    """
    Create a report the crew
    """
    inputs = {
        'starting_point': starting_point,
        'destination': destination,
        'start_date': start_date,
        'end_date': end_date
    }

    TravelAgentCrew().reporter_crew().kickoff(inputs=inputs)


def create_presentation(starting_point: str, destination: str, start_date: str, end_date: str):
    """
    Create a presentation
    """
    
    inputs = {
        'starting_point': starting_point,
        'destination': destination,
        'start_date': start_date,
        'end_date': end_date
    }

    TravelAgentCrew().presenter_crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TravelAgentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelAgentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        TravelAgentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
