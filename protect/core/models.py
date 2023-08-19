from django.db import models

# bu projede "on_delete=models.PROTECT" i kullanarak silme işlemlerinde koruma sağlıyoruz.
#bununla birlikte silme işlemi yapmak istediğimizde hata alıyoruz.
#aynı zamanda sentry e de hata gönderiyoruz. ve detaylı bilgi alıyoruz.
#bu işlemleri kitap yazar ve yazar notları adı altında oluşturulmuş modelleri bir birine bağlayarak yapıyoruz
#örneğin bir yazar silinmek istediğinde yazarın notları ve yazdığı kitaplar da silinmek isteniyor ve ya yazar silinemiyor 
 
class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + self.author.name + " " + self.author.last_name


class AuthorNotes(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    note = models.TextField()

    def __str__(self):
        return self.author.name + " " + self.author.last_name 
#sentry e sinyal gönderilecekk 
