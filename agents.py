from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os 

load_dotenv()

# Define the environment variables

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"

## Create a Senior Blog Content Researcher

blog_researcher = Agent(
    role = "Blog Researcher from YouTube Videos",
    goal = "Get the relevant video content for the topic {topic} from YouTube Channel",
    verbose = True,
    memory = True,
    backstory= "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" ,
    tools = [yt_tool],
    allow_delegation = True

)


## Create a Senior Blog Writer agent with YT Tool

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False


)
