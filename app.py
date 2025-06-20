from flask import Flask, request, send_from_directory, jsonify
import os, uuid

app = Flask(__name__)
AUDIO_FOLDER = "static/audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "no file"}), 400
    voice_id = str(uuid.uuid4())
    file_path = os.path.join(AUDIO_FOLDER, f"{voice_id}.ogg")
    file.save(file_path)
    return jsonify({"voice_id": voice_id})

@app.route('/v/<voice_id>')
def serve_voice(voice_id):
    return send_from_directory(AUDIO_FOLDER, f"{voice_id}.ogg", mimetype='audio/ogg')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
