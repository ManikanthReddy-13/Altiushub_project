from flask import Flask, jsonify, request

import uuid

app = Flask(__name__)
invoices =[]

@app.route('/invoices',methods =['POST'])
def create_invoice():
    data =request.json
    # if not valide_invoice_items(items):
    #     return jsonify({'message':"Invalid"}),400
    invoice_id=str(uuid.uuid4())
    invoice = {
        'id' : invoice_id,
        # 'Date': data['date'],
        'InvoiceNumber': data['InvoiceNumber'],
        'CustomerName': data['CustomerName']
        #some data need to included


    }
    invoices.append(invoice)
    return jsonify({'message':"Invoice data added",'id':invoice_id}),201

@app.route('/invoices/<invoice_id>',methods =['GET'])
def get_invoice(invoice_id):
    for invoice in invoices:
        if invoice['íd'] == invoice_id:
            return jsonify(invoice)
    return jsonify({'message': "no data found"}),404

@app.route('/invoices/<invoice_id>',methods =['PUT'])
def update_invoice(invoice_id):
    for invoice in invoices:
        if invoice['íd'] == invoice_id:
            data=request.json
            invoice.update(data)
            return jsonify({'Message': "invoice data updated "}),200
    return jsonify({'message': "no data found"}), 404

@app.route('/invoices/<invoice_id>',methods =['DELETE'])
def delete_invoice(invoice_id):
    for index, invoice in enumerate(invoices):
        if invoice['íd'] == invoice_id:
            del invoices[index]

            return jsonify({'Message': "invoice data deleted"}),200
    return jsonify({'message': "no data found"}), 404

@app.route('/invoices',methods =['GET'])
def retrive_invoices():
    return jsonify(invoices)
# Validations for InvoiceItems:
# Amount = Quantity x Price
# Price, Quantity, and Amount must be greater than zero.

# def valide_invoice_items(items):
#     for item in items:
#         if item['quantity']<= 0 or item['price'] <= 0 or item['amount']<=0:
#             return false
#         if item['amount']!= item['quantity']* item['price'] :
#             return false
#     return true

if __name__ == '__main__':
    app.run(debug=True)


