#coding=gbk
def city_country(city_name, country):
    return country + ',' + city_name;
end = city_country('Hangzhou', 'Chnia');
print(end);
end = city_country('Lanzhou', 'Chnia');
print(end);
end = city_country('Xian', 'Chnia');
print(end);
print('==============================分割线===========================');
def make_album(singer_name,album_name):
    end_dict = {'singer_name':singer_name,'album_name':album_name}
    return end_dict;
end = make_album('Lin Junjie', 'Summer');
print(end);
end = make_album('Liang Jingru', 'Courage');
print(end);
end = make_album('Cheng Long', 'Zuiquan');
print(end);
def make_album(singer_name, album_name, number = ''):
    if number:
        end_dict = {'singer_name':singer_name,'album_name':album_name,'number':number}
    else:
        end_dict = {'singer_name':singer_name,'album_name':album_name}
    return end_dict;
end = make_album('Lin Junjie', 'Summer','30');
print(end);
end = make_album('Liang Jingru', 'Courage');
print(end);
end = make_album('Cheng Long', 'Zuiquan');
print(end);
print('==============================分割线===========================');
while 1:
    singer_name = input('Input singer name(Input q to quit!):');
    if(singer_name == 'q'):
        break;
    album_name = input('Input album name:');
    number = input('Input the number:');
    end = make_album(singer_name,album_name,number);
    print(end);
