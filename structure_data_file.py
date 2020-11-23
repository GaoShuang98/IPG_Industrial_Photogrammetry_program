# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 21:21
# @Author  : 黄高爽
# @Email   : huanggaoshuang123@163.com
# @File    : structure_data_file.py
# @Software: PyCharm

"""说明：以下数据结构为光束法平差程序可调用的数据结构"""


class CAMERA_DATA:
    """相机10参数"""
    def __init__(self, df=24, dx0=0, dy0=0, dk1=0, dk2=0, dk3=0, dp1=0, dp2=0, db1=0, db2=0):
        self.df = df
        self.dx0, self.dy0 = dx0, dy0
        self.dk1, self.dk2, self.dk3 = dk1, dk2, dk3
        self.dp1, self.dp2 = dp1, dp2
        self.db1, self.db2 = db1, db2


class IMG_PTS:
    """像点参数结构"""
    def __init__(self, index=0, Match=0, Station_Index=0, x=0, y=0, X=0, Y=0, Z=0, Corx=0, Cory=0, Resix=0,
                 Resiy=0, _3D_Point_Index=0, RMS=0):
        self.Index = index
        self.Match = Match
        self.Station_Index = Station_Index
        self.x, self.y = x, y
        self.X, self.Y, self.Z = X, Y, Z
        self.Corx, self.Cory = Corx, Cory
        self.Resix, self.Resiy = Resix, Resiy
        self._3D_Point_Index = _3D_Point_Index
        self.RMS = RMS


class SHOT_STA:
    """摄站参数结构"""
    def __init__(self, img_target=0, Xs=0, Ys=0, Zs=0, Rx=0, Ry=0, Rz=0, q0=1, q1=0, q2=0, q3=0, a1=0,
                        a2=0, a3=0, b1=0, b2=0, b3=0, RMSx=0, RMSy=0, value=False):
        self.img_target = img_target  # 0
        self.Xs, Ys, Zs = Xs, Ys, Zs  # 1 2 3
        self.Rx, Ry, Rz = Rx, Ry, Rz  # 4 5 6
        self.q0 = q0  # 7
        self.q1, q2, q3 = q1, q2, q3  # 8 9 10
        self.a1, a2, a3 = a1, a2, a3  # 11 12 13
        self.b1, b2, b3 = b1, b2, b3  # 14 15 16
        self.RMSx, RMSy = RMSx, RMSy  # 17 18 19
        self.value = value  # 20


class POINTS_3D:
    """3d点结构体"""
    def __init__(self, Match=0, X=0, Y=0, Z=0, value=False, Cal_X=0, Cal_Y=0, Cal_z=0, RMS=0, RMS_x=0, RMS_y=0):
        self.Match = Match  # 0
        self.X, Y, Z =X, Y, Z  # 1, 2, 3
        self.value = value  # 4
        self.Cal_X, Cal_Y, Cal_z = Cal_X, Cal_Y, Cal_z  # 5, 6, 7
        self.RMS = RMS  # 8
        self.RMS_x, RMS_y = RMS_x, RMS_y  # 9


class QUADRILATERAL:
    """四边形结构体（相机文件）"""

    def __init__(self, area=0, first_point_index=0, second_point_index=0, third_point_index=0,
                 fourth_point_index=0, value=False):
        self.area = area  # 0
        self.first_point_index = first_point_index  # 1
        self.second_point_index = second_point_index  # 2
        self.third_point_index = third_point_index  # 3
        self.fourth_point_index = fourth_point_index  # 4
        self.value = value  # 5


class Bundle_matrix_thread:
    """光束法平差的矩阵定义"""
    """L_3DPts *p3Dpts
    int n3DptsCount
    int n3DptsCountPerThread
    int nImgCount
    double df, dx0, dy0
    CMatrix *N11
    CMatrix *N21
    CMatrix *N22
    CMatrix *R1
    CMatrix *R2"""
    pass


class Corresponding_points:
    """同名点结构体"""
    # station_index = 0
    # match_num = 0

    def __init__(self, station_index=0, match_num=0):
        self.station_index = station_index
        self.match_num = match_num

class MN:
    """三维重建过程中的比例系数"""
    # m = 0  # (X-Xs)/(Z-Zs)
    # n = 0  # (Y-Ys)/(Z-Zs)
    # Xs, Ys, Zs = 0, 0, 0  # 因为要组成方程式，必须将m,n,Xs，Ys，Zs对应起来

    def __init__(self, m=0, n=0, Xs=0, Ys=0, Zs=0):
        self.m = m
        self.n = n
        self.Xs, self.Ys, self.Zs = Xs, Ys, Zs



