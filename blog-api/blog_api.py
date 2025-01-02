from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data to act as an in-memory database
blog_posts = [
    {"id": 1, "title": "First Blog Post", "content": "This is my first blog post!"},
    {"id": 2, "title": "Second Blog Post", "content": "Exploring REST APIs with Flask."},
]


# Get all blog posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(blog_posts)

# Get a single blog post by ID
@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in blog_posts if post["id"] == post_id), None)
    if post is None:
        abort(404, description="Post not found")
    return jsonify(post)

# Create a new blog post
@app.route('/api/posts', methods=['POST'])
def create_post():
    if not request.json or not "title" in request.json or not "content" in request.json:
        abort(400, description="Invalid request. Title and content are required.")
    
    new_post = {
        "id": blog_posts[-1]["id"] + 1 if blog_posts else 1,
        "title": request.json["title"],
        "content": request.json["content"]
    }
    blog_posts.append(new_post)
    return jsonify(new_post), 201

# Update an existing blog post
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in blog_posts if post["id"] == post_id), None)
    if post is None:
        abort(404, description="Post not found")
    if not request.json:
        abort(400, description="Invalid request.")

    post["title"] = request.json.get("title", post["title"])
    post["content"] = request.json.get("content", post["content"])
    return jsonify(post)

# Delete a blog post
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((post for post in blog_posts if post["id"] == post_id), None)
    if post is None:
        abort(404, description="Post not found")
    
    blog_posts.remove(post)
    return jsonify({"message": f"Post {post_id} deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
