from flask import Flask, request, jsonify
import base64

app = Flask(__name__)


@app.route('/text_to_sign', methods=['POST'])
def accept_text():
    # Retrieve the 'q' parameter from the request's query string
    text_param = request.args.get('q')

    # Check if the 'q' parameter is present
    if text_param is None:
        return jsonify({'error': 'Text parameter (q) is required'}), 400

    text_param = text_param.lower()

    categories = {
        "thank": "thank.mp4",
    }

    words = text_param.split()

    result = []

    for word in words:
        if(word in categories):
            
            vidPath = categories[word]
            with open(vidPath, 'rb') as video_file:
                video_binary = video_file.read()

            # Encode the binary content using Base64
            video_base64 = base64.b64encode(video_binary).decode('utf-8')

            msg = {"word": word, "found": True, "video_base64": video_base64 }
            result.append(msg)
        else:
            msg = {"word": word, "found": False}
            result.append(msg)

    return jsonify(result)


app.run(debug=True)
