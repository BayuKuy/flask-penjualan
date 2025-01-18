from flask import Blueprint, render_template, redirect, url_for
from .models import products

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html', products=products)

@main.route('/buy/<int:product_id>', methods=['POST'])
def buy(product_id):
    for product in products:
        if product_id == product.id and product.stock > 0:
            product.stock -= 1
            break
    else:
        return redirect(url_for('main.home'))
    return redirect(url_for('main.home'))
