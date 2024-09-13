from crewai import Task

def research_task(researcher, website_search_tool, search_tool, topic):
  return Task(
    description=(
      f"Identify sector described as follows: {topic}."
      "Indetify law changes for that sector and specific situation."
      "Focus on risks, but also oportunities."
    ),
    expected_output='A comprehensive 4-5 paragraphs long report on possible risks and changes in the topic of EU AI act.',
    tools=[website_search_tool, search_tool],
    agent=researcher,
  )

def analysis_task(analyst, website_search_tool, search_tool):
  return Task(
    description=(
      "Analyze given changes and summrize them. Draw possible situations where you need to apply the needed changes and when not."
    ),
    expected_output='A comprehensive 4-5 paragraphs long report, defining sector, outlining number of articles from EU AI act and possible situations which might be treated differently due to changes in the laws.',
    tools=[website_search_tool, search_tool],
    agent=analyst,
  )

# Writing task with language model configuration
def writer_task(writer, topic):
  return Task(
    description=(
      f"Compose an engaging and clear response mail for your client, which describes himself as \"{topic}\". using report from analyst."
      "This email should be easy to understandable for wide non-tech audience and showing personal touch to the recipent."
      "In the email you should provide law acts with regard to the certain points you mention."
    ),
    expected_output='A 2-3 paragraph email answer formatted as plain text. You work for law firm called Awesome Law LLC.',
    tools=[],
    agent=writer,
    async_execution=False,
    output_file='mail.txt'  # Example of output customization
  )