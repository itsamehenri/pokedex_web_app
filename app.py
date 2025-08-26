from flask import Flask, render_template, redirect, url_for, request
from services import get_all_generations, get_all_types, get_all_pokemon

app = Flask(__name__)

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    name = request.args.get('name', "", type=str)
    type1 = request.args.get('type1', 0, type=int)
    type2 = request.args.get('type2', 0, type=int)
    region = request.args.get('region', 0, type=int)    

    types = get_all_types()
    regions = get_all_generations()
    data = get_all_pokemon(name, type1, type2, region)

    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    paginated_items = data[start:end]

    total_pages = (len(data) + per_page - 1) // per_page

    return render_template(
        'base.html',
        types=types,
        regions=regions,
        name=name,
        t1=type1,
        t2=type2,
        region=region,
        page=page,
        data=paginated_items,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)