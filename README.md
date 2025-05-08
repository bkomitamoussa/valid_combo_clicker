# valid_combo_clicker

This script automates clicking YES or NO for the Valid Combinations section of Survey 2a. When you run it, it opens a new browser. You'll need to log in yourself and navigate to the survey. Once there you tell it how to click. You do this in two ways. First, you provide a pattern as a string of 'y's and 'n's. Then you tell it how many times to repeat this pattern. For instance, a table might have individual and household level outcomes. If the first five outcomes are individual level, you would want to click YES for outcome-individual and then NO for outcome-household. So you provide the string 'yn' and enter 5 for the number of repetitions. In the limiting case where you need to click NO hundreds of times, you would input 'n' and enter 500 for the number of repetitions. You'll interact with the program by inputting text in Terminal. Once you make your selection, the program will print the selection it clicked and the number of the repitition it's in each time it clicks. I have not made this program very robust, so try not to input any characters in any form other than what is asked for in the question. The phrasing of the prompts to the user are a little sloppy, so also feel free to recommend changes there (or any other changes if something isn't working).

## Setup Instructions

### Step 1: Install Python
See the Downloads section at https://www.python.org/ 

### Step 2: Install Firefox (if you don't have it already)
I think the code would work for a different browser, I've just set it up to use Firefox since that's what I use. 

### Step 3: Download this repository

### Step 4: Install Required Packages (just selenium):
Open a new terminal at the project folder (left-click the folder and then choose "New Terminal at Folder") and run:

	pip install -r requirements.txt

### Step 5: Run the script:
In your terminal run:

	python3 validcombos.py
	
