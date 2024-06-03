from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('serper_api_key')


from crewai_tools import SerperDevTool



# Initialize the tool for internet searching capabilities
tool = SerperDevTool()