var recorder; // globally accessible

const request = {
    "url": "http://127.0.0.1:5000/voice",
    "method": "POST",
    "processData": false,
    "contentType": false,
    "data": ''
};

async function sendToServer(blob) {
    const form = new FormData();
    form.append("language", "pt-PT");
    form.append("audio", blob, "file.wav");

    request.data = form;

    console.log("A enviar para processamento...")
    return $.ajax(request);
}

function capturemicrophone(callback) {
    navigator.mediaDevices
        .getUserMedia({audio: true})
        .then(callback)
        .catch(console.error);
}

function listen() {
    capturemicrophone(microphone => {
        recorder = new RecordRTCPromisesHandler(microphone, {
            recorderType: StereoAudioRecorder,
            mimeType: 'audio/wav',
            disableLogs: true
        });

        recorder.startRecording();
        console.log("A ouvir...")
        const speechEvents = hark(microphone, {});

        speechEvents.on('stopped_speaking', async () => {
            await recorder.stopRecording();
            console.log("Áudio recebido")

            const blob = await recorder.getBlob();

            sendToServer(blob)
                .then(console.dir)
                .catch(console.error);

            setTimeout(listen, 3000);
        });
    });
}

$('#voice').click(() => {
    listen()
});
