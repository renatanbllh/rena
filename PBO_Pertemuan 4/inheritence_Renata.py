#Superclass
class Pendidikan():
    
    def __init__(self, nama_sekolah, alamat_sekolah ) :
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah

#Subclass Pendidikan Sekolah Menengah Pertama dan Sekolah Menengah Atas
class Pendidikan_SekolahMenengahPertama(Pendidikan):
    pass

class Pendidikan_SekolahMenengahAtas(Pendidikan):
    pass


SDN01PondokBambu = Pendidikan("SDN01PondokBambu", "JakartaTimur")
SMPN202Jakarta = Pendidikan_SekolahMenengahPertama("SMPN202Jakarta", "JakartaTimur")
SMAN1Babelan = Pendidikan_SekolahMenengahAtas("SMAN1Babelan", "JakartaTimur")

#Output
print(SDN01PondokBambu.nama_sekolah, SDN01PondokBambu.alamat_sekolah)
print(SMPN202Jakarta.nama_sekolah, SMPN202Jakarta.alamat_sekolah)
print(SMAN1Babelan.nama_sekolah, SMAN1Babelan.alamat_sekolah)
