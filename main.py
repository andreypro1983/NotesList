# import model.note as nt
# from datetime import datetime as dt
import view.text as text
from model.service import Service
from view.view import View
import controller.controller as c


if __name__ == '__main__':
    txt = text.Text()
    controller = c.Controller(Service(), View(txt), txt)
    controller.start()
    
    # user1 = nt.Note('старт', 'проверка старта', dt.now())
    # print(user1)
