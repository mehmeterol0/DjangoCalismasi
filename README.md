# DjangoCalismasi

#Register Ekranı
Öncelikle oluşturduğumuz siteye kullanıcı kayıt edelim. 

![register](https://user-images.githubusercontent.com/116752575/198673765-fa73d741-4f48-4b20-b130-7fee9730f21d.png)

Yukardaki ekranda Username, Email, Firstname, Lastname, Password ve Re-Password alanları eksiksiz doldurulmalıdır. 
Eğer bu alanların birisi boş bırakılsa Kayıt Oluşturulmayacaktır.
Kullanıcı kayıt olurken, Password ile Re-Password'ün ikisi de aynı olmasına dikkat etmelidir.
Tüm alanlar doğru bir şekilde doldurulduğu takdirde kayıt olma işlemi başarıyla gerçekleşecektir.
Kayıtlar veritabanına aktarılacaktır. Aynı zamanda Admin Paneli üzerinden de erişebilinmektedir.

![login](https://user-images.githubusercontent.com/116752575/198674429-66155300-fdc6-4585-ab5b-68ee8e479bff.png)

Kayıt olan kullanıcı Login (Giriş) olmalıdır. Kullanıcı Username ve Passwordu doğru bir şekilde yazdığı takdirde Başarıyla Giriş Yapacaktır.
Herhangi bir textteki bilgi yanlış olduğunda kullanıcı Login olamaz. username ya da parola yanlış uyarısı alır.

![navbar](https://user-images.githubusercontent.com/116752575/198674867-bbda5569-041d-4d17-8b91-851632729045.png)

Login olan kullanıcı kayıt olurken ki girdiği isim ve soyisimle üst tarafta login olduğunu gösteren bir Hoşgeldiniz bölümü karşılar.
Bu Navbar bölümünde; Anasayfa, İş ilanları, SearchBar ve Logout butonu bulunmaktadır. Kullanıcı Logout'a bastığında hesaptan çıkış yapar.
Anasayfa ve iş ilanlarına giden kullanıcı iş ilanları ve anasayfaya yönlendirme yapar.

![anasayfa](https://user-images.githubusercontent.com/116752575/198675400-ffb7fed6-79d0-4a6c-9614-da51c1e1468e.png)

Anasayfa ve İş ilanları bölümünde sitedeki varolan tüm iş ilanları listelenir. Kullanıcı iş ilanının başlığına tıkladığında iş ilanının detay sayfasına yönlendirilir.

![kategoriler](https://user-images.githubusercontent.com/116752575/198675839-eb5566c9-8c8c-44bd-89c3-01be982c23be.png)

Kategori bölümü meslek gruplarının var olduğu bölümdür. Kullanıcı kendine ait olan meslek grubuna girerek ilgili iş ilanlarını görüntüleyebilir.

![kategori seçme](https://user-images.githubusercontent.com/116752575/198676087-780b1c34-5a7a-4a3f-a4c3-236fc39a6aec.png)

Örnek olarak Uçak Mühendisliği gurubundaki iş ilanları listelemek isteyen kullanıcı, Kategorilerden Uçak Mühendisliğini seçerek ilgili alanın 
iş ilanları kullanıcıya gösterilir. 

![iş ilann detay](https://user-images.githubusercontent.com/116752575/198676582-3bcc6586-59c4-48a2-9ae3-5e07108f2819.png)

Yukarıda Görüntüleme Sistemleri Yazılım Mühendisi iş ilanının detayına girmiş olan kullanıcıyı görmektesiniz. 
aşağıya doğru inersek;
![başvuru yapma](https://user-images.githubusercontent.com/116752575/198676825-8bf7bb65-d352-4d85-9b12-c275ff231c32.png)

Kullanıcı E-Mail, Ön Yazı ve CV'sini yükleyerek ilgili iş ilanına başvurabilir. 

Kullandığım Teknolojiler;
• Python
• DJANGO
• Html
• Css
• Js
• Sql

Bu ilk DJANGO,HTML,CSS,JS ile çalışmam olmuştur. 

