
import os
import subprocess
import sys

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def check_env_file():
    """Check if .env file exists and has API key"""
    if not os.path.exists(".env"):
        print("⚠️  .env file not found")
        print("📝 Creating .env file...")
        with open(".env", "w") as f:
            f.write("# OpenAI API Configuration\n")
            f.write("# Get your API key from: https://platform.openai.com/api-keys\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
        print("✅ .env file created")
        print("🔑 Please edit .env file and add your OpenAI API key")
    else:
        print("✅ .env file found")
        with open(".env", "r") as f:
            content = f.read()
            if "your_openai_api_key_here" in content:
                print("⚠️  Please update your OpenAI API key in .env file")

def run_tests():
    """Run basic tests"""
    print("🧪 Running basic tests...")
    try:
        subprocess.check_call([sys.executable, "test_agents.py"])
        print("✅ Tests passed!")
    except subprocess.CalledProcessError:
        print("❌ Tests failed")
        print("💡 Make sure you have set up your OpenAI API key in .env file")

def main():
    """Main setup function"""
    print("🚀 Career Mentor Agent - Setup")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Install dependencies
    install_dependencies()
    
    # Check environment file
    check_env_file()
    
    # Run tests
    run_tests()
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Run: chainlit run main.py")
    print("3. Open the provided URL in your browser")
    print("\n💡 For help, check the README.md file")

if __name__ == "__main__":
    main() 