from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/convert', methods=['POST'])
def convert():
    print('helloo')
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    audio_filename = file.filename
    filename_without_extension = os.path.splitext(audio_filename)[0]
    #command = f"python3 -W ignore::UserWarning -m mask_cyclegan_vc.test --name mask_cyclegan_vc_{filename_without_extension} --save_dir results/New/ --preprocessed_data_dir VCTK_preprocessed/vctk_testing/ --gpu_ids 0 --speaker_A_id {filename_without_extension} --speaker_B_id p229F2 --ckpt_dir results/New/mask_cyclegan_vc_{filename_without_extension}/ckpts/ --load_epoch 300 --model_name generator_A2B"

    print(file.filename)
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        file_path = os.path.join('result' , file.filename)
        file.save(file_path)
    except Exception as e:
        return jsonify({'error': str(e)})

    try:
        os.system("python3  -W ignore::UserWarning -m mask_cyclegan_vc.test --name mask_cyclegan_vc_p306F1_p229F2 --save_dir results/New/ --preprocessed_data_dir VCTK_preprocessed/vctk_testing/ --gpu_ids 0 --speaker_A_id p306F1 --speaker_B_id p229F2 --ckpt_dir results/New/mask_cyclegan_vc_p306F1_p229F2/ckpts/ --load_epoch 300 --model_name generator_A2B")
    except Exception as e:
        return jsonify({'error': str(e)})

    return jsonify({'message': 'File saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
