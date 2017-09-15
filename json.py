data = {'review': [{'name': 'Mr. Anwar Nasser', 'slug': 'Anwar', 'arabic_name': 'أنور ناصر', 'last_updated_date': '2017-09-14T15:14:01Z', 'rating': 2}, {'name': 'Ms. Mariam Alghaith', 'slug': 'Mariam', 'arabic_name': 'مريم الغيث', 'last_updated_date': '2017-09-14T15:14:01Z', 'rating': 3}, {'name': 'Mr. Ahmad Muqeem', 'slug': 'Ahmad', 'arabic_name': 'احمد مقيم', 'last_updated_date': '2017-09-14T15:14:01Z', 'rating': 3}, {'name': 'Mr. Yaaqoub Al Ali', 'slug': 'Yaaqoub', 'arabic_name': 'يعقوب العلى', 'last_updated_date': '2017-09-14T15:14:01Z', 'rating': 1}, {'name': 'Ms. Zainab Dashti', 'slug': 'Zainab', 'arabic_name': 'زينب دشتى', 'last_updated_date': '2017-09-14T15:14:01Z', 'rating': 5}, {'name': 'Mr. Omar Jassim', 'slug': 'Omar', 'arabic_name': 'عمر جاسم', 'last_updated_date': '2017-09-14T15:14:01Z', 'rating': 3}]}

print(data)

a = data["review"]

for obj in a:
    print(obj["name"])
    print("rating:" + str(obj["rating"]))
    print("")
