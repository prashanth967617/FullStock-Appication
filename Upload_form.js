import React, { useState } from 'react';
import axios from 'axios';

const UploadForm = () => {
    const [file, setFile] = useState(null);

    const handleChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:8000/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            alert('File uploaded: ' + response.data.filename);
        } catch (error) {
            alert('Error uploading file: ' + error.response.data.detail);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" accept=".pdf" onChange={handleChange} />
            <button type="submit">Upload PDF</button>
        </form>
    );
};

export default UploadForm;
