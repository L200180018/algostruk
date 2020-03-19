class Manusia(object):
      keadaan='Lapar'
      def __init__(self,nama):
            self.nama=nama
      def ucapkansalam(self):
            print("salam, namaku",self.nama)
      def makan(self,s):
            self.keadaan='kenyang'
      def olahraga(self, k):
            print("Saya baru saja latihan",k)
            self.keadaan='lapar'
      def mengalikandengandua(self,n):
            return n*2
        
class mahasiswa(Manusia):
      def __init__(self,nama,NIM,kota,us):
            self.nama=nama
            self.NIM=NIM
            self.kotatinggal=kota
            self.uangsaku=us
      def __str__(self):
            s=self.nama + ', NIM '+str(self.NIM)\
               + ',  Tinggal di  '+self.kotatinggal\
               + ', Uang saku Rp '+str(self.uangsaku)\
               + ', tiap bulannya '
            return s
      def ambilNama(self):
            return self.nama
      def ambilNIM(self):
            return self.NIM
      def ambilUangSaku(self):
            return self.uangsaku
      def makan(self,s):
            print("Saya nbaru saja makan",s,"sambil tidur.")
            self.keadaan='kenyang'

class MhsTIF(mahasiswa):
    def katakanPy(self):
        print('Python is cool')

c0 = MhsTIF('ika',10,'sukoharjo',240000)
c1 = MhsTIF('budi',51,'sragen',230000)
c2 = MhsTIF('ahmad',2,'surakarta',250000)
c3 = MhsTIF('candra',18,'surakarta',235000)
c4 = MhsTIF('eka',4,'boyolali',240000)
c5 = MhsTIF('fandi',31,'salatiga',250000)
c6 = MhsTIF('deni',13,'klaten',245000)
c7 = MhsTIF('galuh',5,'wonogiri',245000)
c8 = MhsTIF('janto',23,'klaten',245000)
c9 = MhsTIF('hasan',64,'karanganyar',270000)
c10 = MhsTIF('khalid',29,'purwodadi',265000)

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

target = 'klaten'
for i in daftar:
    if i.kotatinggal == target:
        print(i.nama + '  tinggal di ' + target)
