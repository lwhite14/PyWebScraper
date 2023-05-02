# University Web Scraper
Built using Python and Beautiful Soup. Parses University academic sites and compiles papers, articles, 
and other academic material into a .csv file.

## Creating Virtual Environment
I've used Visual Studio to create my virtual environment:
 1. Open the solution.
 1. Right click on 'Python Environments'. 
 1. Click 'Add Environment'.
 1. Make sure the new environment name is 'venv'.
 1. Create a new virtual environment based on requirements.txt.

This can also be done via the command line, however, I had some trouble integrating the environment with
Visual Studio when creating it this way. If you're not using Visual Studio then this method will work.

    cd UniversityWebScraper
    python -m venv ./venv
    cd venv/Scripts
    activate
    cd ../..
    pip install -r requirements.txt

## Running the Program
An executable file has been included for ease of use. Open a command prompt and cd to the root of the 
cloned/downloaded repository. Then run this command to get a list of command line arguments:
    
    PyUniScraper --help

You can use this executable to get .csv files that contain academic material information for your 
chosen university.