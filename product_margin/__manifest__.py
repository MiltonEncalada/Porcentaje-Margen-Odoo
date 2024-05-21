{
    'name': 'Product Margin',
    'version': '1.0',
    'summary': 'Add margin percentage to products',
    'category': 'Inventory',
    'author': 'Your Name',
    'depends': ['product', 'web'],
    'data': [
        'views/product_template_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'product_margin/static/src/js/product_margin_widget.js',
        ],
    },
    'installable': True,
    'application': False,
}
