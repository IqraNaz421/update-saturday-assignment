


import asyncio
from dotenv import load_dotenv
from tools import get_career_roadmap
from agents import CareerAgent, SkillAgent, JobAgent, CareerMentorRunner

def test_tools():
    """Test the get_career_roadmap tool"""
    print("🧪 Testing get_career_roadmap tool...")
    
    test_careers = ["Data Science", "Software Development", "Cybersecurity"]
    
    for career in test_careers:
        result = get_career_roadmap(career)
        print(f"\n📋 {career} Roadmap:")
        print(result)
        print("-" * 50)

async def test_agents():
    """Test individual agents"""
    print("\n🤖 Testing individual agents...")
    
    try:
        # Test creating agents
        career_agent = CareerAgent()
        skill_agent = SkillAgent()
        job_agent = JobAgent()
        
        print("✅ All agents created successfully!")
        print(f"   CareerAgent: {career_agent.name}")
        print(f"   SkillAgent: {skill_agent.name}")
        print(f"   JobAgent: {job_agent.name}")
        
        # Test agent responses
        test_input = "I love solving puzzles and working with data"
        
        print(f"\n🧪 Testing CareerAgent with input: '{test_input}'")
        career_response = await career_agent.run(test_input)
        print(f"CareerAgent Response: {career_response}")
        
    except Exception as e:
        print(f"❌ Error testing agents: {e}")

async def test_runner():
    """Test the CareerMentorRunner workflow"""
    print("\n🏃 Testing CareerMentorRunner workflow...")
    
    try:
        runner = CareerMentorRunner()
        print("✅ CareerMentorRunner created successfully!")
        
        # Test complete workflow
        test_input = "I enjoy creating software and solving complex problems"
        print(f"\n🧪 Testing complete workflow with input: '{test_input}'")
        
        results = await runner.run_workflow(test_input)
        
        print("\n📊 Workflow Results:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['agent']}:")
            print(f"   Description: {result['description']}")
            print(f"   Response: {result['response'][:100]}...")
        
        print("\n✅ Workflow completed successfully!")
        
    except Exception as e:
        print(f"❌ Error testing runner: {e}")

async def main():
    """Run all tests"""
    print("🚀 Career Mentor Agent - Custom Agent & Runner Test Suite")
    print("=" * 65)
    
    # Test tools
    test_tools()
    
    # Test agents
    await test_agents()
    
    # Test runner
    await test_runner()
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main()) 