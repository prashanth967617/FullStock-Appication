import React from 'react';
import UploadForm from './components/UploadForm';
import QuestionForm from './components/QuestionForm';

function App() {
    return (
        <div>
            <h1>PDF Question App</h1>
            <UploadForm />
            <QuestionForm />
        </div>
    );
}

export default App;
