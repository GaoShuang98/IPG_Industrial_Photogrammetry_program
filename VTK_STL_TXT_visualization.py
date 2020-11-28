# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# @Time    : 2020/8/25 12:01
# @Author  : 黄高爽
# @Email   : huanggaoshuang123@163.com
# @File    : VTK_STL_TXT_visualization.py  # 导入txt点文件和stl文件两种格式，并三维显示出来
# @Software: PyCharm

import vtk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


global renWin
global ren
# 创建渲染控制器
ren = vtk.vtkRenderer()
# 创建渲染窗口
renWin = vtk.vtkRenderWindow()

class MyInteractor(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, parent=None):
        self.AddObserver("CharEvent", self.OnCharEvent)
        self.AddObserver("KeyPressEvent", self.OnKeyPressEvent)

    # Override the default key operations which currently handle trackball or joystick styles is provided
    # OnChar is triggered when an ASCII key is pressed. Some basic key presses are handled here
    def OnCharEvent(self, obj, event):
        pass

    def OnKeyPressEvent(self, obj, event):
        # Get the compound key strokes for the event
        key = self.GetInteractor().GetKeySym()
        # Ask each renderer owned by this RenderWindow to render its image and synchronize this process
        if (key == 'B'):
            print('key B was clicked!')
        renWin.Render()
        return



def CreateCoordinates():  # 创建坐标系
    # create coordinate axes in the render window
    axes = vtk.vtkAxesActor()  # 创建坐标轴actor
    axes.SetTotalLength(400, 400, 400)  # Set the total length of the axes in 3 dimensions
    # Set the type of the shaft to a cylinder:0, line:1, or user defined geometry.
    axes.SetShaftType(0)  # 设置坐标轴的样式
    axes.SetCylinderRadius(0.02)  # 坐标轴半径
    axes.GetXAxisCaptionActor2D().SetWidth(0.01)  # 设置坐标轴图例的大小
    axes.GetYAxisCaptionActor2D().SetWidth(0.01)
    axes.GetZAxisCaptionActor2D().SetWidth(0.01)
    return axes


def get_file():
    """
    弹出获取文件路径界面,并获得文件路径,根据文件后缀判断是否为txt\stl格式,
    若是则调用相对应程序打开,
    若不是报错弹窗,重新打开获取文件路径界面.
    """
    r = tk.Tk()
    r.withdraw()
    file_dir = filedialog.askopenfilename()
    end_str = file_dir.split('.')[-1]
    if end_str == 'txt' or end_str == 'TXT':
        actor = poly_points(file_dir)
    elif end_str == 'stl' or end_str == 'STL':
        actor = get_stl_data(file_dir)
    else:
        messagebox.showinfo('tip', '所导入文件后缀名为：".{}"并非".txt"或".stl"'.format(end_str))
        main()  # 重新导入文件
        exit()
    return actor


def get_stl_data(stl_dir):
    """
    传入stl文件路径,打开stl文件,返回stl文件的actor对象
    """
    reader = vtk.vtkSTLReader()
    reader.SetFileName(stl_dir)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    return actor


def get_points(file_path):
    """
    根据传入的点文件路径打开并导入点文件,返回name\X\Y\Z数组
    """
    X = list()
    Y = list()
    Z = list()
    point_name = list()
    with open(file_path, 'r') as f:
        line = f.readlines()
        for i in line:
            pure = i.replace('\n', '')
            n, a, b, c = pure.split('\t')
            point_name.append(n)
            X.append(float(a))
            Y.append(float(b))
            Z.append(float(c))
    return point_name, X, Y, Z


def poly_points(file_dir):
    """
    传入点文件路径,并调用get_points()函数打开点文件,导出点文件Actor
    """
    names, X, Y, Z = get_points(file_dir)
    # 创建vtkpoints对象
    points = vtk.vtkPoints()
    # 创建大量模型点处存放对象：vtkCellArry
    cells = vtk.vtkCellArray()
    # 将导入的点名及其坐标添加至CellArry中
    for i in range(len(names)):
        points.InsertPoint(i, [X[i], Y[i], Z[i]])
        cells.InsertNextCell(1)
        cells.InsertCellPoint(i)
    # 创建一个poly_data对象
    point = vtk.vtkPolyData()
    # set the points and vertices we created as the geometry and topology of the polydata
    point.SetPoints(points)
    point.SetVerts(cells)
    # mapper
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(point)
    # actor
    actor_p = vtk.vtkActor()
    actor_p.SetMapper(mapper)
    actor_p.GetProperty().SetColor(1.0, 1.0, 0.0)
    actor_p.GetProperty().SetPointSize(2)
    return actor_p


def create():
    """主函数,创建获得文件(点文件或者stl文件),
    vtk可视化主要过程:
    vtk.vtkPolyDataMpper ===>
    PolyDataMapper.SetInputdata(InputData)
    vtk.vtkActor ===>
    Actor.SetMapper(mapper)
    vtk.vtkRenderer ===>
    Renderer.AddActor(Actor)
    vtk.vtkRenderWindow ===>
    RenderWindow.AddRenderer(Renderer)
    vtk.vtkRenderWindowInteractor ===>
    RenderWindowInteractor.SetRenderWindow()
    RenderWindowInteractor.SetRenderWindow()
    """
    file_data = get_file()
    # # 创建渲染控制器
    # ren = vtk.vtkRenderer()
    # # 创建渲染窗口
    # renWin = vtk.vtkRenderWindow()
    # 将渲染控制器添加进渲染窗口中
    renWin.AddRenderer(ren)
    # 设置鼠标交互模式
    style = MyInteractor()
    # style = vtk.vtkInteractorStyleTrackballCamera()  # 定义常规交互模式（MPS/s的3D界面交互模式）
    # 创建交互嗅探模块
    iren = vtk.vtkRenderWindowInteractor()
    # 将设置好的交互模块与渲染窗口绑定
    iren.SetRenderWindow(renWin)

    style.SetDefaultRenderer(ren)
    # 交互嗅探模块赋予交互方式
    iren.SetInteractorStyle(style)

    # 添加坐标轴
    axes = CreateCoordinates()
    ren.AddActor(axes)
    # 添加点或stl
    ren.AddActor(file_data)
    # 设置背景颜色
    ren.SetBackground(0.3, 0.3, 0.3)
    # 设置窗口大小、位置以及名字
    renWin.SetSize(1000, 700)  # 窗口大小
    renWin.SetPosition(250, 80)  # 窗口位置
    renWin.SetWindowName('Cylinder')  # 窗口标题

    # This allows the interactor to initalize itself. It has to be called before an event loop.
    iren.Initialize()

    # We'll zoom in a little by accessing the camera and invoking a "Zoom" method on it.
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1)

    # 窗口读取绘制器生成的图形
    renWin.Render()

    # 初始化鼠标嗅探模块，并开始循环
    iren.Start()


if __name__ == '__main__':
    create()

