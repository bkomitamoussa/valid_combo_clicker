# valid_combo_clicker

This script automates clicking YES or NO a set number of times for the Valid Combinations section of Survey 2a. When you run it, it opens a new browser. You'll need to log in yourself and navigate to the survey. Once there you tell it how many times to click, and it clicks for you. You'll interact with the program by inputting text in Terminal. I am still figuring out the best way to trigger the next click, so sometimes (often) the script will click again (multiple times even) before the next question loads. This means that if you tell the clicker to click 400 times, you might only get 200 (maybe only 100) functional clicks. Sometimes the rapid clicking causes an error in SurveyCTO because you're asking it to do too many things at once. When this happens the clicker stops clicking.  

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
	
