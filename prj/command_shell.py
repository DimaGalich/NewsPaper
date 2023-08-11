py manage.py makemigrations

py manage.py migrate

py manage.py shell

from newapp.models import *


1.Создать двух пользователей (с помощью метода User.objects.create_user).

user1 = User.objects.create(username='Mike', first_name='Frank')
user2 = User.objects.create(username='Semyon', first_name='Ber')

2.Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(authorUser=user1)
Author.objects.create(authorUser=user2)


3.Добавить 4 категории в модель Category.
Category.objects.create(name='IT')
Category.objects.create(name='Education')
Category.objects.create(name='Sport')
Category.objects.create(name='Music')

4.Добавить 2 статьи и 1 новость.
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')), categoryType='NW', title='smth title', text='smth text')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')), categoryType='AR', title='smth title2222', text='222222smth text')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Semyon')), categoryType='NW', title='smth title22', text='222smth text')

5.Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Education')
c3 = Category.objects.get(name='Sport')
c4 = Category.objects.get(name='Music')
p1.postCategory.add(c1)
p2.postCategory.add(c1, c2)
p3.postCategory.add(c3, c4)

6.Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(commentUser=User.objects.get(username='Mike'), commentPost= Post.objects.get(pk=1), text='comment one')
Comment.objects.create(commentUser=User.objects.get(username='Mike'), commentPost= Post.objects.get(pk=2), text='comment two')
Comment.objects.create(commentUser=User.objects.get(username='Semyon'), commentPost= Post.objects.get(pk=3), text='comment three')
Comment.objects.create(commentUser=User.objects.get(username='Semyon'), commentPost= Post.objects.get(pk=4), text='comment four')

7.Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=2).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=3).like()

8.Обновить рейтинги пользователей.
Author.objects.get(authorUser=User.objects.get(username='Mike')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Semyon')).update_rating()
a = Author.objects.get(authorUser=User.objects.get(username='Semyon'))
a.ratingAuthor
Author.objects.get(authorUser=User.objects.get(username='Mike')).ratingAuthor

9.Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
print(best)


