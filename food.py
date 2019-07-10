
from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)
foods=[
    {"name":"Pizza","price":20,"id":1},
    {"name":"Chicken","price":15,"id":2},
    {"name":"Rice","price":2,"id":3}
]
@app.route("/",methods=["GET"])
def index():
    return render_template("food.html",FOODS=foods) 

@app.route('/delete/<food_id>')
def delete_food(food_id):
    for v in foods:
        if v["id"]==int(food_id):
            foods.remove(v)
            break
    return redirect(url_for('index'))
@app.route("/",methods=['POST'])
def post_food():
    food_name=request.form.get('name')
    food_price=request.form.get('price')
    food_id=foods[len(foods)-1]['id']+1
    foods.append({'name':food_name,'price':food_price,'id':food_id})
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
