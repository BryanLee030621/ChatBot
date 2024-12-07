import React, { useState } from 'react';

function FileUpload() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    await fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: formData,
    });
    alert('File uploaded successfully.');
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default FileUpload;
