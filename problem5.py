check_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # num bu sayılara bölünecek.

def function(x):
    for num in range(x,999999999):  # num sayısını bu aralıkta al.
        if all(num % i == 0 for i in check_list):  # tüm num'lar için if atadık. Bu num'lar check_list içerisindeki sayılara bölünecek.
            return num # print çıktısı olmadığı için return koyduk ki sayıyı yazdırsın.
    return None # sayı bulamazsa işlemi none yapacak.

if __name__ == '__main__':
    solution = function(20)
    if solution is None:
        print('Sayıyı bulamadık.')
    else:
        print('Sayıyı bulduk.', solution)
