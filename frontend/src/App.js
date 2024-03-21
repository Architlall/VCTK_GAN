import React, { useState } from 'react';
import axios from 'axios';
import './App.css'
function App() {
    const [selectedModel, setSelectedModel] = useState('');
    const [uploadedFiles, setUploadedFiles] = useState([]);
    const [targetVoiceFile, setTargetVoiceFile] = useState(null);

const [file, setFile] = useState(null);

const handleFileChange = (event) => {
  setFile(event.target.files[0]);
};
const handleModelChange = (e) => {
    setSelectedModel(e.target.value);
};


const handleSubmit = async () => {
  try {
    const formData = new FormData();
    formData.append('file', file);

    const response = await axios.post('http://localhost:5000/convert', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    console.log(response.data);
  } catch (error) {
    console.error('Error uploading file:', error);
  }
};

//     const handleDownload = async () => {
//         if (convertedAudio) {
//             const downloadLink = document.createElement('a');
//             downloadLink.href = `http://localhost:5000/uploads/${convertedAudio}`;
//             downloadLink.download = 'converted_audio.wav';
//             downloadLink.click();
//         }
    

    return (
        <div className="app">
            <div className="container">
                <div className="box">
                    <h2>Deepfake Generator</h2>
                    <div className="input-group">
                        <label>Select Model:</label>
                        <select value={selectedModel} onChange={handleModelChange}>
                            <option value="model1">Model 1</option>
                            <option value="model2">Model 2</option>
                            {/* Add more models as needed */}
                        </select>
                    </div>
                    <div className="input-group">
                        <label>Upload Source Voice Files:</label>
                        <input type="file" accept=".wav" onChange={handleFileChange} />
                    </div>
                    {/* <div className="input-group">
                        <label>Upload Target Voice File:</label>
                        <input type="file" onChange={handleTargetVoiceFileUpload} />
                    </div> */}
                    <button onClick={handleSubmit} disabled={!file} >Generate Deepfake</button>
                    {/* <button onClick={handleDownload} >Download output audio</button> */}
                </div>
            </div>
        </div>
    );

                };
export default App;


