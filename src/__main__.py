import os
import sys

if __name__ == "__main__":
    script_path = os.path.join(os.path.dirname(__file__), "streamlit_app.py")

    try:
        os.system(f"streamlit run {script_path} {' '.join(sys.argv[1:])}")
    except KeyboardInterrupt:
        print("Streamlit app has been stopped.")
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
