from flask import Flask, jsonify

app = Flask(__name__)

counts = {
    'elfen1x': 0,
    'swamy': 0,
    'latumbasuricatos': 0,
    'senorefe':0,
    'payis': 0,
    'mitsu': 0,
    'rafaela': 0,
    'ieiko': 0,
    'vickjoy': 0,
    'leofloresdc': 0
}

is_counting_frozen = False

@app.route('/count/<variable>')
def increment_count(variable):
    if not is_counting_frozen:
        if variable in counts:
            counts[variable] += 1
            return jsonify({'res': f"votos: {counts[variable]}"})
        else:
            return jsonify(error='Invalid variable.')
    else:
        return jsonify(error='Counting is frozen.')

@app.route('/freeze')
def freeze_counting():
    global is_counting_frozen
    is_counting_frozen = True
    return jsonify(status='Counting frozen.')

@app.route('/counts')
def get_counts():
    return jsonify({'res': f"elfen1x: {counts['elfen1x']}, swamy: {counts['swamy']},latumbasuricatos: {counts['latumbasuricatos']},señorefe: {counts['señorefe']},payis: {counts['payis']},mitsu: {counts['mitsu']},rafaela: {counts['rafaela']},ieiko: {counts['ieiko']},vickjoy: {counts['vickjoy']},leofloresdc: {counts['leofloresdc']},"})

@app.route('/restart')
def restart():
    global counts
    counts = {
        'elfen1x': 0,
        'swamy': 0,
        'latumbasuricatos': 0,
        'señorefe':0,
        'payis': 0,
        'mitsu': 0,
        'rafaela': 0,
        'ieiko': 0,
        'vickjoy': 0,
        'leofloresdc': 0
    }
    return jsonify(counts)

if __name__ == '__main__':
    app.run()