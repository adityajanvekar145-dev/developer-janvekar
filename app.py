from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        length = int(data.get('length', 12))
        
        # Validate length
        if length < 4:
            return jsonify({'error': 'Password length must be at least 4 characters!'}), 400
        
        if length > 128:
            return jsonify({'error': 'Password length cannot exceed 128 characters!'}), 400
        
        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation
        
        # Combine all characters
        all_chars = lowercase + uppercase + digits + special_chars
        
        # Ensure password has at least one of each type
        password_chars = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_chars)
        ]
        
        # Fill remaining length with random characters
        for _ in range(length - 4):
            password_chars.append(random.choice(all_chars))
        
        # Shuffle to avoid predictable pattern
        random.shuffle(password_chars)
        
        # Join to create final password
        password = ''.join(password_chars)
        
        return jsonify({'password': password}), 200
    
    except ValueError:
        return jsonify({'error': 'Please enter a valid number for password length!'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
