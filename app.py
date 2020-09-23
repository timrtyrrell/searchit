from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        subreddit = request.form.get("subreddit", "")
        filtercontent = request.form.get("filtercontent", "")
        filteramount = request.form.get("filteramount", "")
        return render_template('index.html', subreddit=subreddit, filtercontent=filtercontent, filteramount=filteramount)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
