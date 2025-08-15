"""
Run All Dashboard Scripts
Israel-Palestine Conflict Analysis
"""
import os
import subprocess
import time

def run_script(script_name):
    """Run a Python script and print its output."""
    print(f"\n{'='*50}")
    print(f"Running {script_name}...")
    print(f"{'='*50}\n")
    
    # Run the script and capture output
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    
    # Print output
    if result.stdout:
        print(result.stdout)
    
    # Print errors if any
    if result.returncode != 0:
        print(f"Error running {script_name}:")
        print(result.stderr)
        return False
    
    return True

def main():
    """Run all visualization scripts."""
    start_time = time.time()
    
    # Create visualizations directory if it doesn't exist
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')
    
    # List of scripts to run in order
    scripts = [
        '1_event_types_bar.py',
        '2_actors_pie.py',
        '3_events_over_time.py',
        '4_fatalities_line.py',
        '5_geographic_scatter.py',
        '6_location_heatmap.py',
        'dashboard_index.py'
    ]
    
    # Run each script
    success = True
    for script in scripts:
        if not run_script(script):
            success = False
            print(f"Failed to run {script}. Continuing with other scripts...")
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n{'='*50}")
    if success:
        print(f"All scripts completed successfully in {duration:.2f} seconds!")
        print("\nYour dashboard is ready! Open visualizations/index.html in a web browser to view it.")
    else:
        print("Some scripts encountered errors. Check the output above for details.")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main() 