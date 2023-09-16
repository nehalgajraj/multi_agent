
# Import Tools that you want to use
from Tools.weather import Weather
from Tools.wikipedia import Wikipedia
from Tools.agentcreator import AgentCreator
from Tools.memory import Memory
from Tools.twitter import Twitter

# Add the Tools to the list of available tools
TOOLS = [
    {"function": Weather.get_current_weather, "metadata": Weather.function_metadata},
    {"function": Wikipedia.get_summary, "metadata": Wikipedia.function_metadata},
    {"function": AgentCreator.create_new_agent, "metadata": AgentCreator.function_metadata},
    {"function": Twitter.tweet, "metadata": Twitter.function_metadata},

    # Add more tools as needed
]
