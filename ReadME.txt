READ ME FOR AI PROMPT LIBRARY

### THIS WAS GENERATED WITH THE HELP OF OLLAMA's mimimax-m3:cloud Model !!

# A curated collection of AI-powered prompts for working with code. Each prompt is designed to help you learn, debug, improve, and document your projects faster.

This library uses a BMI Calculator (Python) as a running example to demonstrate every prompt in action.

##📑 Table of Contents
##⚙️ Prompt 1: Explain Code
##🐛 Prompt 2: Debug
##♻️ Prompt 3: Refactor
##📝 Prompt 4: Generate README
  #🚀 How to Use
  #💡 Why Use This Library?
  #🤝 Contributing
  #📜 License

⚙️ Prompt 1: Explain Code
💬 The Prompt
Explain this code line by line for a beginner.
🎯 Purpose
Turns complex code into easy-to-understand explanations. Perfect for:
📚 Learning a new language
🆕 Onboarding new team members
🧠 Understanding unfamiliar codebases
📦 Example
  #Given the BMI Calculator below:

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

The AI responds with:
"def is a keyword used to define a function..." "height ** 2 means height squared..." "return sends the value back to the caller..."
# Every line is broken down with plain English and helpful tables.

# Prompt 2: Debug
# The Prompt
Why is this code failing?
(Or: "Debug this code.")

#Purpose
Identifies runtime errors, logic bugs, and edge cases that break your program. The AI will:

# Detect the issue
# Provide a fix
# Compare before/after behavior
# Example
The original BMI Calculator crashes when:

Test Case	Original Behavior
Height = 0	 ZeroDivisionError
Weight = "abc"	 ValueError
Weight = -50	 Wrong result
The AI responds with:

"height ** 2 becomes 0 when height is 0, causing division by zero..." Wraps input in a try/except block and adds a validation loop to prevent crashes.

## The fixed version handles all edge cases gracefully.
# Prompt 3: Refactor
# The Prompt
Improve this code while keeping it beginner-friendly.
# Purpose
Enhances code quality without sacrificing readability:
# Removes redundancy
# Improves structure
# Adds docstrings & type hints
# Follows best practices
#Example
The BMI Calculator can be refactored to:
Extract category logic into a separate function
Use type hints (def calculate_bmi(weight: float, height: float) -> float:)
Add a main() function for cleaner entry point
Group constants (BMI thresholds) at the top
The AI responds with:

An improved version of the code that is more modular, documented, and ready to scale — while still easy en
