from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.firecrawl import FirecrawlTools
from textwrap import dedent

def init_team(openai_key, firecrawl_key):
    if not (openai_key and firecrawl_key):
        return None

    tools = [FirecrawlTools(search=True, crawl=True, poll_interval=10)]
    model = OpenAIChat(id="gpt-4o")

    launch_analyst = Agent(
        name="Product Launch Analyst",
        description=dedent("""You analyze competitor product launches..."""),
        model=model, tools=tools, show_tool_calls=True, markdown=True
    )

    sentiment_analyst = Agent(
        name="Market Sentiment Specialist",
        description=dedent("""You analyze market sentiment..."""),
        model=model, tools=tools, show_tool_calls=True, markdown=True
    )

    metrics_analyst = Agent(
        name="Launch Metrics Specialist",
        description=dedent("""You analyze KPIs & adoption metrics..."""),
        model=model, tools=tools, show_tool_calls=True, markdown=True
    )

    team = Team(
        name="Product Intelligence Team",
        mode="coordinate",
        model=model,
        members=[launch_analyst, sentiment_analyst, metrics_analyst],
        instructions=[
            "Use the right agent depending on request type",
            "Always provide sources and actionable insights"
        ],
        show_tool_calls=True, markdown=True, debug_mode=True,
        show_members_responses=True,
    )
    return team
