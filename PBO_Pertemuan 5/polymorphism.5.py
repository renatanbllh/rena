class suku:
    def intro(self):
        print("indonesia mempunyai berbagai macam suku")

    def daerah(self):
        print("suku suku tersebut menetap diberbagai daerah")

class sunda(suku):
    def daerah(self):
        print("Orang Sunda, secara tradisional tinggal di provinsi Jawa Barat , Banten , Jakarta , dan bagian barat Jawa Tengah.")

class jawa(suku):
    def daerah(self):
        print("Orang Jawa, secara tradisional tinggal di provinsi Jawa Tengah, DIY, dan Jawa Timur.")

class bugis(suku):
    def daerah(self):
        print("Orang Bugis, secara tradisional tinggal di provinsi Sulawesi Selatan")

obj_suku = suku()
obj_sunda = sunda()
obj_jawa = jawa()
obj_bugis = bugis()

obj_suku.intro()
obj_suku.daerah()

print("\n")

obj_sunda.intro()
obj_sunda.daerah()

print("\n")

obj_jawa.intro()
obj_jawa.daerah()

print("\n")

obj_bugis.intro()
obj_bugis.daerah()