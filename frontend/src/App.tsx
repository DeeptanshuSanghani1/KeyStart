import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { FilePond, registerPlugin } from 'react-filepond';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';


registerPlugin(FilePondPluginImagePreview);

function App() {
  const [files, setFiles] = useState<any[]>([]);
  return (
    <div className="App">
      <FilePond
        files={files}
        allowMultiple={true}
        maxFiles={3}
        onupdatefiles={setFiles}
        server={{
          url: 'http://127.0.0.1:8000',
          process: {
            url: '/api/upload/getFile',
            method: 'POST',
            withCredentials: false,
            headers: {},
            timeout: 7000,
            onload(response) {
              console.log(response)
              return response
            },
            onerror: (response) => console.error('Error uploading file', response),
          },
        }}
        name="file"
        acceptedFileTypes={['audio/x-midi', 'audio/midi', 'audio/mid']}
        labelIdle='Drag & Drop your files or <span class="filepond--label-action">Browse</span>'
      />
    </div>

  );
}

export default App;
