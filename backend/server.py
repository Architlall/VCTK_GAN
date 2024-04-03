from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/convert', methods=['POST'])
def convert():
    if 'sourceFile' not in request.files or 'targetFile' not in request.files:
        return jsonify({'error': 'Both source and target files are required'})

    source_file = request.files['sourceFile']
    target_file = request.files['targetFile']

    if source_file.filename == '' or target_file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        source_file_path = os.path.join('results', source_file.filename)
        target_file_path = os.path.join('results', target_file.filename)
        source_file.save(source_file_path)
        target_file.save(target_file_path)
    except Exception as e:
        return jsonify({'error': str(e)})

    try:
        # Your conversion logic here
        # You can use source_file_path and target_file_path for processing
        # Example command:
        # os.system(f"python3 your_script.py --source_file {source_file_path} --target_file {target_file_path}")
        # Replace "your_script.py" with your actual script name and provide appropriate arguments
        print(f"Source file saved at: {source_file_path}")
        print(f"Target file saved at: {target_file_path}")
    except Exception as e:
        return jsonify({'error': str(e)})

    return jsonify({'message': 'Files saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
