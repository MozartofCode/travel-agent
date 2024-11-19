from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from travel_agent.src.travel_agent.tools.custom_tool import PowerPointTool
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
serper_api_key = os.getenv('SERPER_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'


@CrewBase
class TravelAgentCrew():

	# CREATING ALL THE AGENTS

	@agent
	def train_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['train_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def flight_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['flight_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	
	@agent
	def car_rental_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['car_rental_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def hotel_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['hotel_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def airbnb_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['airbnb_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def weatherman(self) -> Agent:
		return Agent(
			config=self.agents_config['weatherman'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def clothing_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['clothing_advisor'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def museum_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['museum_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def restaurant_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['restaurant_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def activity_finder(self) -> Agent:
		return Agent(
			config=self.agents_config['activity_finder'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def historian(self) -> Agent:
		return Agent(
			config=self.agents_config['historian'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def slide_maker(self) -> Agent:
		return Agent(
			config=self.agents_config['slide_maker'],
			tools=[SerperDevTool(), PowerPointTool()],
			verbose=True
		)

	
	@agent
	def reporter_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_agent'],
			verbose=True
		)
	
	
	@agent
	def presenter_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['presenter_agent'],
			verbose=True
		)
	
	# CREATING ALL THE TASKS
	
	@task
	def find_transportation(self) -> Task:
		return Task(
			config=self.tasks_config['find_transportation'],
		)

	@task
	def find_hotel(self) -> Task:
		return Task(
			config=self.tasks_config['find_hotel'],
		)

	@task
	def get_weather(self) -> Task:
		return Task(
			config=self.tasks_config['get_weather'],
		)

	@task
	def get_activities(self) -> Task:
		return Task(
			config=self.tasks_config['get_activities'],
		)

	@task
	def get_history(self) -> Task:
		return Task(
			config=self.tasks_config['get_history'],
		)

	@task
	def get_presentation(self) -> Task:
		def generate_presentation(subtask_results):
			presentation_data = {
				"transportation": subtask_results['find_transportation'],
				"hotel": subtask_results['find_hotel'],
				"weather": subtask_results['get_weather'],
				"activities": subtask_results['get_activities'],
				"history": subtask_results['get_history'],
			}
			self.slide_maker().action(presentation_data)
			return "Presentation created successfully."

		return Task(
			config=self.tasks_config['get_presentation'],
			subtasks=[
				self.find_transportation(),
				self.find_hotel(),
				self.get_weather(),
				self.get_activities(),
				self.get_history(),
			],
			action=generate_presentation,
			output_file="Presentation.pptx"
		)


	@task
	def get_report(self) -> Task:
		def aggregate_results(subtask_results):
			# Generate the report
			report = f"""
			Travel Report:
			- Transportation: {subtask_results['find_transportation']}
			- Accommodation: {subtask_results['find_hotel']}
			- Weather: {subtask_results['get_weather']}
			- Activities: {subtask_results['get_activities']}
			- History: {subtask_results['get_history']}
			"""

			with open('Report.pdf', 'w') as file:
				file.write(report)
			return "Report.pdf"

		return Task(
			config=self.tasks_config['get_report'],
			subtasks=[
				self.find_transportation(),
				self.find_hotel(),
				self.get_weather(),
				self.get_activities(),
				self.get_history(),
			],
			action=aggregate_results,
			output_file='Report.pdf'
		)


	# CREATING ALL THE CREWS

	@crew
	def reporter_crew(self) -> Crew:
		return Crew(
			agents=[
				self.train_finder(),
				self.flight_finder(),
				self.car_rental_finder(),
				self.hotel_finder(),
				self.airbnb_finder(),
				self.weatherman(),
				self.clothing_advisor(),
				self.museum_finder(),
				self.restaurant_finder(),
				self.activity_finder(),
				self.historian(),
			],
			tasks=[
				self.find_transportation(),
				self.find_hotel(),
				self.get_weather(),
				self.get_activities(),
				self.get_history(),
				self.get_report(),
			],
			verbose=True,
			manager_agent=self.reporter_agent(),
        	manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
			process=Process.hierarchical
		)


	@crew
	def presenter_crew(self) -> Crew:
		return Crew(
			agents=[
				self.train_finder(),
				self.flight_finder(),
				self.car_rental_finder(),
				self.hotel_finder(),
				self.airbnb_finder(),
				self.weatherman(),
				self.clothing_advisor(),
				self.museum_finder(),
				self.restaurant_finder(),
				self.activity_finder(),
				self.historian(),
				self.slide_maker()
			],
			tasks=[
				self.get_presentation(),
			],
			verbose=True,
			manager_agent=self.presenter_agent(),
        	manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
			process=Process.hierarchical
		)