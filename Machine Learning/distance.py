#!/usr/bin/python
# encoding: utf-8
'''
MinkowskiDistance:闵可夫斯基距离
'''

class Distance(object):

    @staticmethod
    def minkowski_distance(vector1,vector2,q):      ##vector：向量,q:几次方   minkowski:米可夫斯基距离

        """

        :param vector1: [1,2,3,45,6]
        :param vector2: [1,2,4,56,7]
        :return:
        """
        distance=0.
        n=len(vector1)
        for i in range(n):
            distance +=pow(abs(vector1[i]-vector2[i]),q)
        return round(pow(distance,1.0/q),5)



# #####################
# # a=[1,2,3]
# # b=[3,4,5]
# # c=Distance.minkowski_distance(a,b,2)
# # print(c)
# if __name__ == '__main__':     #只有在主函数下才能执行
#     print('cat')


