import os
from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool
import agentops 

def search_tool():
  return SerperDevTool()

def website_search_tool():
  return WebsiteSearchTool(website='https://artificialintelligenceact.eu/')

# Creating a senior researcher agent with memory and verbose mode
@agentops.track_agent(name='research-agent')
def get_researcher(website_search_tool, search_tool, topic):
  return Agent(
  role='Senior Law Paralegal',
  goal=f'Uncover changes in EU AI Act for the sector defined in the following statement: {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a keen eye for detail, you uncover the latest"
    "law related articles and precendents in the field of AI law"
  ),
  tools=[website_search_tool, search_tool],
  allow_delegation=True
)

@agentops.track_agent(name='analyst-agent')
def get_analyst(website_search_tool, search_tool, topic):
  return Agent(
  role='Law Ascociate',
  goal='Given large portion of information you create small report with specilized law related vocabulary in topic of AI law changes for the given situation: {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a keen eye for detail, you uncover the latest"
    "law related papers, paradoxes, and contradictions in the law"
  ),
  tools=[website_search_tool, search_tool],
  allow_delegation=True
)

# Creating a writer agent with custom tools and delegation capability
@agentops.track_agent(name='writer-agent')
def get_writer(topic):
  return Agent(
  role='Senior Partner',
  goal=f'Write an email message for non-law audience with the following situation: {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "clear law reports for wide audience, so that they can understand ins and outs of complex law topics."
    "You are menticioulous and provide right law acts for reference from EU AI act for the certain points you mention."
  ),
  tools=[],
  allow_delegation=False
)
