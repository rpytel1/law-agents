from crewai import Crew, Process
from dotenv import load_dotenv
import agentops
load_dotenv()

agentops.init(tags=['eu-ai-act'])

from agents import get_writer, get_analyst, get_researcher, website_search_tool, search_tool
from tasks import research_task, analysis_task, writer_task

website_tool = website_search_tool()
s_tool = search_tool()

topic = "I am an agriculture bussiness using AI for forecasting harvest using computer vision"
    
researcher = get_researcher(website_tool, s_tool, topic)
analyst = get_analyst(website_tool, s_tool, topic)
writer = get_writer(topic)

research_t = research_task(researcher, website_tool, s_tool, topic)
analysis_t = analysis_task(analyst, website_tool, s_tool)
write_t = writer_task(writer, topic)


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[researcher, analyst, writer],
  tasks=[research_t, analysis_t,  write_t],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff()
print(result)
agentops.end_session('Success')