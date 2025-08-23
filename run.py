#!/usr/bin/env python3
"""
LivingNotes - Google Docs Humor Enhancement
Startup script for the hackathon project
"""

import os
import sys
import subprocess

def main():
    print("🎭 LivingNotes - Google Docs Humor Enhancement")
    print("=" * 50)
    print()
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  No .env file found!")
        print("Please copy env.example to .env and configure your API keys:")
        print("   cp env.example .env")
        print()
    
    # Check if requirements are installed
    try:
        import flask
        import requests
        import dotenv
    except ImportError:
        print("📦 Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print()
    
    print("Choose which version to run:")
    print("1. Basic version (simulated API calls)")
    print("2. Enhanced version (with Composio integration)")
    print()
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            print("\n🚀 Starting basic version...")
            print("Access the app at: http://localhost:5001")
            print("Press Ctrl+C to stop the server")
            print()
            os.system("python app.py")
            break
        elif choice == "2":
            print("\n🚀 Starting enhanced version...")
            print("Access the app at: http://localhost:5001")
            print("Press Ctrl+C to stop the server")
            print()
            os.system("python app_with_composio.py")
            break
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
