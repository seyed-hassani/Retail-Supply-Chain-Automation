import os
import sys
import subprocess

def run_dbt_pipeline(project_path, profiles_path):
    try:
        print(f"🔁 Running dbt pipeline in: {project_path}")
        os.chdir(project_path)
        subprocess.run(
            ["dbt", "run", "--profiles-dir", profiles_path],
            check=True
        )
        print("✅ dbt run completed successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ dbt run failed:", e)
    except FileNotFoundError as e:
        print("❌ Path error:", e)

if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else "D:/Job Apply/April 2025/Siemens/Projects/dbt_project"
    profiles_path = sys.argv[2] if len(sys.argv) > 2 else "D:/Job Apply/April 2025/Siemens/Projects/dbt_project"
    run_dbt_pipeline(project_path, profiles_path)
