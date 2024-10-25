import React, { useState } from 'react';
import axios from 'axios';

const QuestionForm = () => {
    const [filename, setFilename] = useState('');
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/ask/', { question, filename });
            setAnswer(response.data.answer);
        } catch (error) {
            alert('Error asking question: ' + error.response.data.detail);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Filename"
                value={filename}
                onChange={(e) => setFilename(e.target.value)}
            />
            <input
                type="text"
                placeholder="Your question"
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />
            <button type="submit">Ask Question</button>
            {answer && <p>Answer: {answer}</p>}
        </form>
    );
};

export default QuestionForm;
