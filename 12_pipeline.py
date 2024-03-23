import subprocess

# List of scripts to execute in order
scripts = [
    "setup_requirements.py",
    "01_extract.py",
    "02_count.py",
    "03_database.py",
    #"sample_data.json",
    #"prompt.txt",
    "05_ping_openai.py",
    "06_prediction.py",
    "06_update_table.py",
    "07_create_responses.py",
    "08_categories.py",
    "09_visualization.py",
    #"clean_dataset.json"
    "11_export.py"
]

def run_script(script):
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

def main():
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()
