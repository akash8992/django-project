# prompt: write a frbonic service code in python in short

from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
  try:
    n = int(request.args.get('n'))
    if n < 0:
      return jsonify({'error': 'Input must be a non-negative integer'}), 400
    result = fibonacci(n)
    return jsonify({'result': result})
  except (ValueError, TypeError):
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
  app.run(debug=True)