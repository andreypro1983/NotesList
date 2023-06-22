import model.note as nt
from datetime import datetime as dt
if __name__ == '__main__':
  
    user1 = nt.Note('старт', 'проверка старта', dt.now())
    print(user1)
