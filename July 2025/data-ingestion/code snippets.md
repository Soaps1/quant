#python -m venv venv
#.\venv\Scripts\Activate 
#pip install notebook ipykernel
#python -m ipykernel install --user --name=venv --display-name "Python (venv) project name"
pip freeze > requirements.txt
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))  # ← back to Quant/
sys.path.insert(0, root_path)