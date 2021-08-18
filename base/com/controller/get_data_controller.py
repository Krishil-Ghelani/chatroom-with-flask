from base import app
import flask as f
from base.com.vo.get_data_vo import TableVo
from base.com.dao.get_data_dao import TableDao


@app.route('/', methods=['GET', 'POST'])
def sign_in():
    return f.render_template('signIn.html')

@app.route('/', methods=['GET', 'POST'])
def get_data():
    name = f.request.form.get('NAME')
    dis = f.request.form.get("DISCRIPTION")

    table_obj = TableVo()
    dao_obj = TableDao()

    table_obj.catagory_name = name
    table_obj.catagory_discription = dis

    dao_obj.insert_catagory(table_obj)