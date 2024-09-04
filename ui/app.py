from flask import Flask, request, jsonify, render_template
import os
import sys

# Adjust the Python path to find the inference_engine module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inference_engine.inference_engine import InferenceEngine, load_knowledge_base

app = Flask(__name__)

# Load knowledge base once on startup
knowledge_base_path = os.path.join(os.path.dirname(__file__), '../knowledge_base/hardware_issues.json')
knowledge_base = load_knowledge_base(knowledge_base_path)

# Instantiate the inference engine
engine = InferenceEngine(knowledge_base)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    problem = request.form['problem']
    solution = engine.diagnose(problem)
    return render_template('index.html', problem=problem, solution=solution)

if __name__ == '__main__':
    app.run(debug=True)
