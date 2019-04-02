from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import random


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Thebestofall9@localhost/customer_details'
db=SQLAlchemy(app)
db.create_all()
db.session.commit()


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Thebestofall9@localhost/company'
db2=SQLAlchemy(app)
db2.create_all()
db2.session.commit()

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Thebestofall9@localhost/transaction'
db3=SQLAlchemy(app)
db3.create_all()
db3.session.commit()

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Thebestofall9@localhost/bank'
db4=SQLAlchemy(app)
db4.create_all()
db4.session.commit()

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Thebestofall9@localhost/wallet'
db5=SQLAlchemy(app)
db5.create_all()
db5.session.commit()


class Data(db.Model):
    __tablename__="data"
    cid_=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    first_=db.Column(db.String(120))
    last_=db.Column(db.String(120))
    add_=db.Column(db.String(120))
    cell_=db.Column(db.Integer)
    password_=db.Column(db.String(120))
    income_=db.Column(db.Integer)
    acc_=db.Column(db.Integer)

    def __init__(self,cid_,email_,first_,last_,add_,cell_,password_,income_,acc_):
        self.cid_=cid_
        self.email_=email_
        self.first_=first_
        self.last_=last_
        self.add_=add_
        self.cell_=cell_
        self.password_=password_
        self.income_=income_
        self.acc_=acc_

class Company(db2.Model):
    __tablename__="company_details"
    company_code=db2.Column(db2.Integer,primary_key=True)
    company_name=db2.Column(db2.String(120),unique=True)
    numberof_shares=db2.Column(db2.Integer)
    stockprice_current=db2.Column(db2.Integer)
    stockprice_previous=db2.Column(db2.Integer)

    def __init__(self,company_code,company_name,numberof_shares,stockprice_current,stockprice_previous):
        self.company_code=company_code
        self.company_name=company_name
        self.numberof_shares=numberof_shares
        self.stockprice_current=stockprice_current
        self.stockprice_previous=stockprice_previous

class Transaction(db3.Model):
    __tablename__="transaction_details"
    transaction_id=db3.Column(db3.Integer,primary_key=True)
    amount=db3.Column(db3.Integer)
    numberof_stockspur=db3.Column(db3.Integer)
    stock_number=db3.Column(db3.Integer)

    def __init__(self,transaction_id,amount,numberof_stockspur,stock_number):
        self.transaction_id=transaction_id
        self.amount=amount
        self.numberof_stockspur=numberof_stockspur
        self.stock_number=stock_number

class Bank(db4.Model):
    __tablename__="bank_details"
    card_num=db4.Column(db4.Integer)
    full_name=db4.Column(db4.String(120))
    cvv_number=db4.Column(db4.Integer)
    bankname=db4.Column(db4.String(120),primary_key=True)
    currency=db4.Column(db4.String(120))

    def __init__(self,card_num,full_name,cvv_number,bankname,currency):
        self.card_num=card_num
        self.full_name=full_name
        self.cvv_number=cvv_number
        self.bankname=bankname
        self.currency=currency

class Wallet(db5.Model):
    __tablename__="wallet_details"
    card_number=db5.Column(db5.Integer)
    full_names=db5.Column(db5.String(120))
    cvv_numbers=db5.Column(db5.Integer)
    banknames=db5.Column(db5.String(120),primary_key=True)
    currencys=db5.Column(db5.String(120))
    amount=db5.Column(db5.Integer)

    def __init__(self,card_number,full_names,cvv_numbers,banknames,currencys,amount):
        self.card_number=card_number
        self.full_names=full_names
        self.cvv_numbers=cvv_numbers
        self.banknames=banknames
        self.currencys=currencys
        self.amount=amount



if db2.session.query(Company).filter(Company.company_code==100 ).count()== 0:
    company_details=Company(company_code=100,company_name='Microsoft',numberof_shares=15000,stockprice_current=110,stockprice_previous=127)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==101 ).count()== 0:
    company_details=Company(company_code=101,company_name='Google',numberof_shares=16000,stockprice_current=1127,stockprice_previous=1125)
    db2.session.add(company_details)
    db2.session.commit()



if db2.session.query(Company).filter(Company.company_code==102 ).count()== 0:
    company_details=Company(company_code=102,company_name='Apple',numberof_shares=15500,stockprice_current=221,stockprice_previous=220)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==103 ).count()== 0:
    company_details=Company(company_code=103,company_name='IBM',numberof_shares=16500,stockprice_current=134,stockprice_previous=133)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==104 ).count()== 0:
    company_details=Company(company_code=104,company_name='Intel',numberof_shares=14000,stockprice_current=46,stockprice_previous=47)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==105 ).count()== 0:
    company_details=Company(company_code=105,company_name='Facebook',numberof_shares=15000,stockprice_current=159,stockprice_previous=158)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==106 ).count()== 0:
    company_details=Company(company_code=106,company_name='NVIDIA',numberof_shares=16000,stockprice_current=244,stockprice_previous=243)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==107 ).count()== 0:
    company_details=Company(company_code=107,company_name='Audi AG',numberof_shares=18000,stockprice_current=730,stockprice_previous=731)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==108 ).count()== 0:
    company_details=Company(company_code=108,company_name='Amazon.com,Inc',numberof_shares=14000,stockprice_current=1831,stockprice_previous=1829)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==109 ).count()== 0:
    company_details=Company(company_code=109,company_name='Berkshire Hathaway',numberof_shares=6000,stockprice_current=315200,stockprice_previous=314750)
    db2.session.add(company_details)
    db2.session.commit()

if db2.session.query(Company).filter(Company.company_code==110 ).count()== 0:
    company_details=Company(company_code=110,company_name='Mitsubishi',numberof_shares=15000,stockprice_current=8900,stockprice_previous=890)
    db2.session.add(company_details)
    db2.session.commit()


update_this=Company.query.filter_by(company_code=108).first()
update_this.numberof_shares=14000
db2.session.commit()


@app.route('/')

def home():
    return render_template("home.html")

@app.route('/success',methods=['POST'])

def success():
    if request.method=='POST':
        email=request.form["email_name"]
        first=request.form["first_name"]
        last=request.form["last_name"]
        add=request.form["address_name"]
        cell=request.form["cell_number"]
        password=request.form["new_password"]
        income=request.form["tax_id"]
        acc=request.form["acc_number"]
        cid=request.form["customer_id"]
        print(email,first)
        if db.session.query(Data).filter(Data.email_== email).count()== 0:
            data=Data(cid_=cid,email_=email,first_=first,last_=last,add_=add,cell_=cell,password_=password,income_=income,acc_=acc)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template('signup.html')



@app.route('/ver',methods=['POST'])

def ver():

    if request.method=='POST':
        em=request.form["email_confirm"]
        id=request.form["customer_confirm"]
        pas=request.form["password_confirm"]
        return render_template("ver.html")

@app.route('/payment',methods=['POST'])

def payment():
    if request.method=='POST':
        global q

        qty=request.form["stock_quantity"]
        pr=request.form["stock_price"]
        sid=request.form["stock_id"]

        transaction_details=Transaction(transaction_id=random.randint(1,5000)*3,amount=pr,numberof_stockspur=qty,stock_number=sid)
        db3.session.add(transaction_details)
        db3.session.commit()
        return render_template("payment.html")


@app.route('/bank', methods=['POST'])

def bank():
    if request.method=='POST':

        return render_template("bank.html")

@app.route('/paysucc',methods=['POST'])

def paysucc():
    if request.method=='POST':
        cnum=request.form["card_numb"]
        fname=request.form["card_name"]
        cvv=request.form["card_cvv"]
        bname=request.form["bank_name"]
        cur=request.form["currency_used"]

        bank_details=Bank(card_num=cnum,full_name=fname,cvv_number=cvv,bankname=bname,currency=cur)
        db4.session.add(bank_details)
        db4.session.commit()
        return render_template("paysucc.html")





@app.route('/brochure')

def brochure():
    return render_template("brochure.html")

@app.route('/wallsucc',methods=['POST'])

def wallsucc():
    if request.method=='POST':
        cnu=request.form["card_num"]
        fnam=request.form["card_nam"]
        cv=request.form["card_cv"]
        bnam=request.form["bank_nam"]
        cu=request.form["currency_use"]
        amnt=request.form["amt"]

        wallet_details=Wallet(card_number=cnu,full_names=fnam,cvv_numbers=cv,banknames=bnam,currencys=cu,amount=amnt)
        db5.session.add(wallet_details)
        db5.session.commit()
        return render_template(wallsucc)


@app.route('/signup')

def signup():
    return render_template("signup.html")

@app.route('/loginc')

def loginc():
    return render_template("loginc.html")


if __name__=="__main__":
    app.run(debug=True)
