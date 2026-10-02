celebs = ["Tayler Swift", "Christiano Ronaldo", "Treavor Noah", "Dwa Lipa", "Jungkook"]
age = [34, 38, 39, 27, 26]

celeb_list = ()
for celeb in celebs:
    celeb_list.append(celeb)

ages_list = (age for age in age if age)

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celeb_list)



