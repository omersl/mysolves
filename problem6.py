# [ALGORİTMA] aralık gir. (1'den 10'a)
# [ALGORİTMA] bu aralıktaki sayıların karesini al.
# [ALGORİTMA] ve bu sayıları topla.
# [KOD] my_list = [i**2 for i in range(num)]
# [KOD] print(sum(my_list))
# [Not:]Varsayılan değerli argümanlarda dikkat etmemiz gereken en önemli kural;
# [Not:]varsayılan değerli parametrenin sıralamanın en sonunda olması gerektiğidir.

def square_sum(num,num1=0):
        my_list = [i**2 for i in range(num1,num)]

        my_list2 = [i for i in range(num1,num)]
     
        print (sum(my_list2)**2 - sum(my_list))


if __name__ == '__main__':
    square_sum(101)
    
