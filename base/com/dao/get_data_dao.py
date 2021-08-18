from base import db
from base.com.vo.get_data_vo import TableVo

class TableDao:
	def insert_catagory(self, catagory_vo):
		db.session.add(catagory_vo)
		db.session.commit()

	def view_catagory(self):
		catagory_vo_list = TableVo.querry.all()
		return catagory_vo_list

	def delete_category(self, category_vo):
        category_vo_list = TableVo.query.get(category_vo.category_id)
        db.session.delete(category_vo_list)
        db.session.commit()

    def edit_category(self, category_vo):
        category_vo_list = TableVo.query. \
            filter_by(category_id=category_vo.category_id).all()
        return category_vo_list

    def update_category(self, category_vo):
        db.session.merge(category_vo)
        db.session.commit()