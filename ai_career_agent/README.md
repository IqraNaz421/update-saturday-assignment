# 💼 Career Mentor Agent

A multi-agent career exploration system built with **custom Agent & Runner classes** using OpenAI Chat Completions API and Chainlit that demonstrates advanced AI agent orchestration and tool integration.

## 🧠 What It Does

Guide students through career exploration using multi-agent support:
- **Recommends career paths** based on interests
- **Uses Tool**: `get_career_roadmap()` to show skills needed for a chosen field
- **Hands off between agents**:
  - **CareerAgent** (suggests fields)
  - **SkillAgent** (shows skill-building plans)
  - **JobAgent** (shares real-world job roles)

## ⚙️ Technology Stack

- **OpenAI Chat Completions API** - Direct API integration
- **Custom Agent & Runner Classes** - Advanced agent orchestration
- **Tools**: Skill Roadmap Generator with automatic tool calling
- **Handoff**: Intelligent switching between Career, Skill, and Job Agents
- **UI**: Chainlit for interactive chat interface

## 🚀 Features

### Multi-Agent Architecture with Custom Classes
- **CareerAgent**: Analyzes user interests and suggests career fields (Data Science, Software Development, Cybersecurity)
- **SkillAgent**: Generates detailed skill-building roadmaps using the `get_career_roadmap` tool
- **JobAgent**: Provides real-world job titles for the chosen career field
- **CareerMentorRunner**: Orchestrates the complete workflow using custom Runner class

### Advanced Tool Integration
- **get_career_roadmap()**: Custom tool that provides structured learning paths for each career field
- **Automatic Tool Calling**: SkillAgent automatically calls the roadmap tool when needed
- **Tool Schema**: Proper tool definition and parameter handling

### Intelligent Agent Handoff System
- **Sequential Processing**: Agents work in sequence using the custom Runner
- **Context Preservation**: Career field information is passed between agents automatically
- **Progress Tracking**: Users can see which agent is currently working
- **Error Handling**: Robust error handling and recovery

## 📋 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the Application
```bash
chainlit run main.py
```

Then open the provided URL (usually http://localhost:8000) in your browser.

## 🎯 How It Works

1. **User Input**: User describes their interests (e.g., "I love solving puzzles and working with data")
2. **CareerAgent**: Analyzes interests and suggests a career field using OpenAI Chat Completions
3. **SkillAgent**: Automatically generates a skill-building roadmap using the `get_career_roadmap` tool
4. **JobAgent**: Lists real-world job titles for the chosen field
5. **Runner Orchestration**: CareerMentorRunner manages the entire workflow seamlessly

## 📁 Project Structure

```
career_mentor_chainlit_full/
├── main.py              # Main Chainlit application with custom Runner
├── agents.py            # Custom Agent & Runner classes using OpenAI API
├── tools.py             # Custom tools including get_career_roadmap
├── requirements.txt     # Python dependencies (standard openai library)
├── README.md           # This file
├── test_agents.py      # Test script for custom Agent & Runner functionality
├── setup.py            # Quick setup script
└── chainlit.md         # Chainlit configuration
```

## 🔧 Customization

### Adding New Career Fields
Edit `tools.py` to add new career fields to the roadmap dictionary:

```python
roadmaps = {
    "Data Science": "...",
    "Software Development": "...",
    "Cybersecurity": "...",
    "Your New Field": "Your roadmap here..."
}
```

### Modifying Agent Instructions
Update the instructions in `agents.py` for each agent class to change their behavior.

### Extending the Workflow
Add new agents to the `CareerMentorRunner` workflow in `agents.py`:

```python
self.workflow = [
    {"agent": self.career_agent, "description": "..."},
    {"agent": self.skill_agent, "description": "..."},
    {"agent": self.job_agent, "description": "..."},
    {"agent": self.new_agent, "description": "..."},  # Add new agent
]
```

### Creating Custom Agents
Extend the base `Agent` class to create new agents:

```python
class CustomAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(
            name="CustomAgent",
            model="gpt-4o",
            instructions="Your custom instructions here",
            tools=[your_custom_tool],  # Optional
            **kwargs
        )
```

## 🎨 Example Usage

**User**: "I enjoy solving complex problems and working with numbers"

**CareerAgent**: "Based on your interest in problem-solving and numbers, I recommend **Data Science** as your career field."

**SkillAgent**: "Here's your Data Science roadmap:
- **Phase 1**: Learn Python, Statistics, SQL
- **Phase 2**: Master Machine Learning
- **Phase 3**: Specialize in Deep Learning"

**JobAgent**: "Common Data Science job titles:
- Data Scientist
- Machine Learning Engineer
- Data Analyst
- Business Intelligence Analyst"

## 🧪 Testing

Run the test suite to verify custom Agent & Runner functionality:

```bash
python test_agents.py
```

This will test:
- Tool functionality
- Individual agent responses using OpenAI Chat Completions
- Complete workflow orchestration

## 🔔 Advanced Features Demonstrated

This project showcases advanced AI concepts:

1. **Custom Agent Classes**: Building agents using OpenAI Chat Completions API
2. **Runner Pattern**: Workflow orchestration and agent handoff
3. **Tool Integration**: Custom tools with automatic calling
4. **Context Management**: Information flow between agents
5. **Error Handling**: Robust error handling and recovery

These concepts are essential for building sophisticated AI applications and demonstrate practical implementation of advanced AI agent patterns using the standard OpenAI library.
