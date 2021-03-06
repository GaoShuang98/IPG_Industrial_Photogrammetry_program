#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Jul 25, 2020 08:42:55 PM CST  platform: Windows NT

import sys
from IPG_GUI_support import SETTING_PARAMETER, SCAN_PARAMETER

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import scan_setting_win_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, setting_root
    setting_root = tk.Toplevel()
    scan_setting_win_support.set_Tk_var()
    top = scan_setting_win(setting_root)
    scan_setting_win_support.init(setting_root, top)
    setting_root.mainloop()

w = None
def create_scan_setting_win(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_scan_setting_win(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    setting_root = rt
    w = tk.Toplevel(setting_root)
    scan_setting_win_support.set_Tk_var()
    top = scan_setting_win(w)
    scan_setting_win_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_scan_setting_win():
    global w
    w.destroy()
    # w = None

class scan_setting_win:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("450x563+460+160")
        top.minsize(152, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("扫描设置")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#c0c0c0")
        top.configure(highlightcolor="black")
        #
        # global _images
        # _images = (
        #
        #  tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
        #          8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
        #          1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
        #          AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
        #          KkoNUtRHpYYAADs= '''),
        #
        #  tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
        #          INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
        #          Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
        #          AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
        #          GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),
        #
        #  tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
        #          rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
        #          +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
        #          KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
        #          IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        # )
        #
        # self.style.element_create("close", "image", "img_close",
        #        ("active", "pressed", "!disabled", "img_closepressed"),
        #        ("active", "alternate", "!disabled",
        #        "img_closeactive"), border=8, sticky='')
        #
        # self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
        #                              {"sticky": "nswe"})])
        # self.style.layout("ClosetabNotebook.Tab", [
        #     ("ClosetabNotebook.tab",
        #       { "sticky": "nswe",
        #         "children": [
        #             ("ClosetabNotebook.padding", {
        #                 "side": "top",
        #                 "sticky": "nswe",
        #                 "children": [
        #                     ("ClosetabNotebook.focus", {
        #                         "side": "top",
        #                         "sticky": "nswe",
        #                         "children": [
        #                             ("ClosetabNotebook.label", {"side":
        #                               "left", "sticky": ''}),
        #                             ("ClosetabNotebook.close", {"side":
        #                                 "left", "sticky": ''}),]})]})]})])
        #
        # PNOTEBOOK = "ClosetabNotebook"

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.scan_set_notebook = ttk.Notebook(top)
        self.scan_set_notebook.place(relx=0.0, rely=0.0, relheight=1.01
                , relwidth=1.007)
        # self.scan_set_notebook.configure(style=PNOTEBOOK)
        self.scan_set_notebook_single_pt = tk.Frame(self.scan_set_notebook)
        self.scan_set_notebook.add(self.scan_set_notebook_single_pt, padding=3)
        self.scan_set_notebook.tab(0, text="单点扫描参数", compound="none"
                ,underline="-1", )
        self.scan_set_notebook_single_pt.configure(background="#c0c0c0")
        self.scan_set_notebook_single_pt.configure(highlightbackground="#d9d9d9")
        self.scan_set_notebook_single_pt.configure(highlightcolor="#000000")
        self.scan_set_notebook_code_pt = tk.Frame(self.scan_set_notebook)
        self.scan_set_notebook.add(self.scan_set_notebook_code_pt, padding=3)
        self.scan_set_notebook.tab(1, text="编码点识别参数", compound="none"
                ,underline="-1", )
        self.scan_set_notebook_code_pt.configure(background="#c0c0c0")
        self.scan_set_notebook_code_pt.configure(highlightbackground="#d9d9d9")
        self.scan_set_notebook_code_pt.configure(highlightcolor="black")
        # ***************************************************************
        self.pt_light_frame1_notebook1 = ttk.Labelframe(self.scan_set_notebook_single_pt)
        self.pt_light_frame1_notebook1.place(relx=0.017, rely=0.014
                , relheight=0.293, relwidth=0.967)
        self.pt_light_frame1_notebook1.configure(relief='')
        self.pt_light_frame1_notebook1.configure(text='''标志亮度''')
        # ------------------------------------------------------------------
        self.TLabel1 = ttk.Label(self.pt_light_frame1_notebook1)
        self.TLabel1.place(relx=0.034, rely=0.212, height=23, width=68
                , bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''梯度阈值：''')

        self.grid_threshold_entry = ttk.Entry(self.pt_light_frame1_notebook1, justify='center')
        self.grid_threshold_entry.place(relx=0.172, rely=0.175, relheight=0.198
                , relwidth=0.252, bordermode='ignore')
        self.grid_threshold_entry.configure(takefocus="")
        self.grid_threshold_entry.configure(cursor="ibeam")
        self.grid_threshold_entry.insert(10, str(SCAN_PARAMETER.grid_threshold))
        # -------------------------------------------------------------------
        self.pace_label = ttk.Label(self.pt_light_frame1_notebook1)
        self.pace_label.place(relx=0.552, rely=0.212, height=23, width=38
                              , bordermode='ignore')
        self.pace_label.configure(background="#d9d9d9")
        self.pace_label.configure(foreground="#000000")
        self.pace_label.configure(font="TkDefaultFont")
        self.pace_label.configure(relief="flat")
        self.pace_label.configure(anchor='w')
        self.pace_label.configure(justify='left')
        self.pace_label.configure(text='''步距：''')

        self.pace_entry = ttk.Entry(self.pt_light_frame1_notebook1, justify='center')
        self.pace_entry.place(relx=0.655, rely=0.171, relheight=0.198
                , relwidth=0.252, bordermode='ignore')
        self.pace_entry.configure(takefocus="")
        self.pace_entry.configure(cursor="ibeam")
        self.pace_entry.insert(10, str(SCAN_PARAMETER.pace))
        # ------------------------------------------------------------
        self.TLabel2 = ttk.Label(self.pt_light_frame1_notebook1)
        self.TLabel2.place(relx=0.052, rely=0.599, height=22, width=58
                           , bordermode='ignore')
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''黑白比：''')

        self.black_white_entry = ttk.Entry(self.pt_light_frame1_notebook1, justify='center')
        self.black_white_entry.place(relx=0.172, rely=0.544, relheight=0.194
                , relwidth=0.252, bordermode='ignore')
        self.black_white_entry.configure(takefocus="")
        self.black_white_entry.configure(cursor="ibeam")
        self.black_white_entry.insert(10, str(SCAN_PARAMETER.black_white_max_limit))
        # ----------------------------------------------------------
        self.TLabel4 = ttk.Label(self.pt_light_frame1_notebook1)
        self.TLabel4.place(relx=0.5, rely=0.599, height=22, width=88
                , bordermode='ignore')
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''背景一致性：''')

        self.background_consistency_entry = ttk.Entry(self.pt_light_frame1_notebook1, justify='center')
        self.background_consistency_entry.place(relx=0.655, rely=0.558
                , relheight=0.194, relwidth=0.252, bordermode='ignore')
        self.background_consistency_entry.configure(takefocus="")
        self.background_consistency_entry.configure(cursor="ibeam")
        self.background_consistency_entry.insert(10, str(SCAN_PARAMETER.deviation))
        # ************************************************************
        self.pt_size_frame2_notebook1 = ttk.Labelframe(self.scan_set_notebook_single_pt)
        self.pt_size_frame2_notebook1.place(relx=0.017, rely=0.316
                , relheight=0.332, relwidth=0.967)
        self.pt_size_frame2_notebook1.configure(relief='')
        self.pt_size_frame2_notebook1.configure(text='''标志尺寸''')

        self.TLabel3 = ttk.Label(self.pt_size_frame2_notebook1)
        self.TLabel3.place(relx=0.483, rely=0.037, height=23, width=34
                           , bordermode='ignore')
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''最小''')

        self.TLabel5 = ttk.Label(self.pt_size_frame2_notebook1)
        self.TLabel5.place(relx=0.759, rely=0.037, height=23, width=34
                           , bordermode='ignore')
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''最大''')
        # -----------------------------------------------------
        self.TLabel6 = ttk.Label(self.pt_size_frame2_notebook1)
        self.TLabel6.place(relx=0.276, rely=0.15, height=32, width=78
                , bordermode='ignore')
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='w')
        self.TLabel6.configure(justify='left')
        self.TLabel6.configure(text='''总像素数：''')

        self.min_total_pix_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.min_total_pix_entry.insert(10, str(SCAN_PARAMETER.pix_num_min_limit))
        self.min_total_pix_entry.place(relx=0.414, rely=0.15, relheight=0.134
                , relwidth=0.217, bordermode='ignore')
        self.min_total_pix_entry.configure(takefocus="")
        self.min_total_pix_entry.configure(cursor="ibeam")

        self.max_total_pix_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.max_total_pix_entry.insert(10, str(SCAN_PARAMETER.pix_num_max_limit))
        self.max_total_pix_entry.place(relx=0.69, rely=0.15, relheight=0.138
                , relwidth=0.217, bordermode='ignore')
        self.max_total_pix_entry.configure(takefocus="")
        self.max_total_pix_entry.configure(cursor="ibeam")
        # -----------------------------------------------------
        self.TLabel7 = ttk.Label(self.pt_size_frame2_notebook1)
        self.TLabel7.place(relx=0.241, rely=0.341, height=32, width=97
                           , bordermode='ignore')
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font="TkDefaultFont")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(anchor='w')
        self.TLabel7.configure(justify='left')
        self.TLabel7.configure(text='''x方向像素数：''')

        self.min_x_pix_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.min_x_pix_entry.insert(10, str(SCAN_PARAMETER.width_min_limit))
        self.min_x_pix_entry.place(relx=0.414, rely=0.341, relheight=0.134
                , relwidth=0.217, bordermode='ignore')
        self.min_x_pix_entry.configure(takefocus="")
        self.min_x_pix_entry.configure(cursor="ibeam")

        self.max_x_pix_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.max_x_pix_entry.insert(10, str(SCAN_PARAMETER.width_max_limit))
        self.max_x_pix_entry.place(relx=0.69, rely=0.341, relheight=0.134
                , relwidth=0.217, bordermode='ignore')
        self.max_x_pix_entry.configure(takefocus="")
        self.max_x_pix_entry.configure(cursor="ibeam")
        # -----------------------------------------------------
        self.TLabel8 = ttk.Label(self.pt_size_frame2_notebook1)
        self.TLabel8.place(relx=0.241, rely=0.528, height=32, width=98
                           , bordermode='ignore')
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font="TkDefaultFont")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(anchor='w')
        self.TLabel8.configure(justify='left')
        self.TLabel8.configure(text='''y方向像素数：''')

        self.min_y_pix_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.min_y_pix_entry.insert(10, str(SCAN_PARAMETER.height_min_limit))
        self.min_y_pix_entry.place(relx=0.414, rely=0.528, relheight=0.138
                , relwidth=0.217, bordermode='ignore')
        self.min_y_pix_entry.configure(takefocus="")
        self.min_y_pix_entry.configure(cursor="ibeam")

        self.max_y_pix_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.max_y_pix_entry.insert(10, str(SCAN_PARAMETER.height_max_limit))
        self.max_y_pix_entry.place(relx=0.69, rely=0.528, relheight=0.138
                , relwidth=0.217, bordermode='ignore')
        self.max_y_pix_entry.configure(takefocus="")
        self.max_y_pix_entry.configure(cursor="ibeam")
        # ---------------------------------------------------------
        self.TLabel9 = ttk.Label(self.pt_size_frame2_notebook1)
        self.TLabel9.place(relx=0.31, rely=0.72, height=32, width=54
                           , bordermode='ignore')
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font="TkDefaultFont")
        self.TLabel9.configure(relief="flat")
        self.TLabel9.configure(anchor='w')
        self.TLabel9.configure(justify='left')
        self.TLabel9.configure(text='''宽高比：''')

        self.width_height_entry = ttk.Entry(self.pt_size_frame2_notebook1, justify='center')
        self.width_height_entry.insert(10, str(SCAN_PARAMETER.shape))
        self.width_height_entry.place(relx=0.414, rely=0.72, relheight=0.138
                , relwidth=0.217, bordermode='ignore')
        self.width_height_entry.configure(takefocus="")
        self.width_height_entry.configure(cursor="ibeam")
        # ******************************************************************
        # ----------------------------------------------------------
        self.reject_thrshold_frame3_notebook1 = ttk.Labelframe(self.scan_set_notebook_single_pt)
        self.reject_thrshold_frame3_notebook1.place(relx=0.017, rely=0.657
                                                    , relheight=0.319, relwidth=0.967)
        self.reject_thrshold_frame3_notebook1.configure(relief='')
        self.reject_thrshold_frame3_notebook1.configure(text='''剔除阈值''')
        # ----------------------------------------------------------------
        self.TLabel10 = ttk.Label(self.reject_thrshold_frame3_notebook1)
        self.TLabel10.place(relx=0.483, rely=0.157, height=32, width=58
                            , bordermode='ignore')
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font="TkDefaultFont")
        self.TLabel10.configure(relief="flat")
        self.TLabel10.configure(anchor='w')
        self.TLabel10.configure(justify='left')
        self.TLabel10.configure(text='''过曝率：''')

        self.TLabel14 = ttk.Label(self.reject_thrshold_frame3_notebook1)
        self.TLabel14.place(relx=0.828, rely=0.199, height=22, width=17
                            , bordermode='ignore')
        self.TLabel14.configure(background="#d9d9d9")
        self.TLabel14.configure(foreground="#000000")
        self.TLabel14.configure(font="TkDefaultFont")
        self.TLabel14.configure(relief="flat")
        self.TLabel14.configure(anchor='w')
        self.TLabel14.configure(justify='left')
        self.TLabel14.configure(text='''%''')

        self.over_exposure_ratio_entry = ttk.Entry(self.reject_thrshold_frame3_notebook1, justify='center')
        self.over_exposure_ratio_entry.insert(10, str(SCAN_PARAMETER.over_exposure * 100))
        self.over_exposure_ratio_entry.place(relx=0.603, rely=0.157
                , relheight=0.153, relwidth=0.217, bordermode='ignore')
        self.over_exposure_ratio_entry.configure(takefocus="")
        self.over_exposure_ratio_entry.configure(cursor="ibeam")
        # ---------------------------------------------------------------------
        self.light_threshold_label = ttk.Label(self.reject_thrshold_frame3_notebook1)
        self.light_threshold_label.place(relx=0.466, rely=0.513, height=23
                                         , width=78, bordermode='ignore')
        self.light_threshold_label.configure(background="#d9d9d9")
        self.light_threshold_label.configure(foreground="#000000")
        self.light_threshold_label.configure(font="TkDefaultFont")
        self.light_threshold_label.configure(relief="flat")
        self.light_threshold_label.configure(anchor='w')
        self.light_threshold_label.configure(justify='left')
        self.light_threshold_label.configure(text='''亮度阈值：''')

        self.gray_thrashold_entry = ttk.Entry(self.reject_thrshold_frame3_notebook1, justify='center')
        self.gray_thrashold_entry.insert(10, str(SCAN_PARAMETER.brightness))
        self.gray_thrashold_entry.place(relx=0.603, rely=0.475, relheight=0.153
                , relwidth=0.217, bordermode='ignore')
        self.gray_thrashold_entry.configure(takefocus="")
        self.gray_thrashold_entry.configure(cursor="ibeam")
        # ----------------------------------------------------------------------------
        self.style.map('TRadiobutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.shape_ratio_radiobutton = ttk.Radiobutton(self.reject_thrshold_frame3_notebook1)
        self.shape_ratio_radiobutton.place(relx=0.155, rely=0.157, relwidth=0.184
                , relheight=0.0, height=25, bordermode='ignore')
        self.shape_ratio_radiobutton.configure(variable=scan_setting_win_support.selectedButton)
        self.shape_ratio_radiobutton.configure(text='''形状平滑度''')
        self.shape_ratio_radiobutton.configure(cursor="hand2")
        self.shape_ratio_radiobutton.configure(state='disable')

        self.over_exposure_Radiobutton = ttk.Radiobutton(self.reject_thrshold_frame3_notebook1)
        self.over_exposure_Radiobutton.place(relx=0.155, rely=0.318
                ,relwidth=0.145, relheight=0.0, height=24, bordermode='ignore')
        self.over_exposure_Radiobutton.configure(variable=scan_setting_win_support.selectedButton)
        self.over_exposure_Radiobutton.configure(text='''过度曝光''')
        self.over_exposure_Radiobutton.configure(state='disable')

        self.light_Radiobutton = ttk.Radiobutton(self.reject_thrshold_frame3_notebook1)
        self.light_Radiobutton.place(relx=0.155, rely=0.475, relwidth=0.128
                , relheight=0.0, height=24, bordermode='ignore')
        self.light_Radiobutton.configure(variable=scan_setting_win_support.selectedButton)
        self.light_Radiobutton.configure(text='''亮度''')
        self.light_Radiobutton.configure(state='disable')

        self.single_pt_scan_set_check_Button = ttk.Button(self.reject_thrshold_frame3_notebook1)
        self.single_pt_scan_set_check_Button.place(relx=0.534, rely=0.75
                , height=40, width=89, bordermode='ignore')
        self.single_pt_scan_set_check_Button.configure(command=scan_setting_win_support.single_pt_scan_set_button_click)
        self.single_pt_scan_set_check_Button.configure(takefocus="")
        self.single_pt_scan_set_check_Button.configure(text='''确定''')
        self.single_pt_scan_set_check_Button.configure(cursor="hand2")

        self.single_pt_scan_set_exit_Button = ttk.Button(self.reject_thrshold_frame3_notebook1)
        self.single_pt_scan_set_exit_Button.place(relx=0.759, rely=0.75
                , height=40, width=89, bordermode='ignore')
        self.single_pt_scan_set_exit_Button.configure(command=scan_setting_win_support.single_pt_scan_set_exit_button_click)
        self.single_pt_scan_set_exit_Button.configure(takefocus="")
        self.single_pt_scan_set_exit_Button.configure(text='''退出''')
        self.single_pt_scan_set_exit_Button.configure(cursor="hand2")
        # ****************************************************************************
        # -------------------------------------------------------
        self.TLabel11 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel11.place(relx=0.267, rely=0.088, height=22, width=109)
        self.TLabel11.configure(background="#c0c0c0")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font="TkDefaultFont")
        self.TLabel11.configure(relief="flat")
        self.TLabel11.configure(anchor='w')
        self.TLabel11.configure(justify='left')
        self.TLabel11.configure(text='''编码点名前缀：''')

        self.TEntry1 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry1.place(relx=0.45, rely=0.088, relheight=0.035, relwidth=0.21)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        self.TEntry1.insert(10, SETTING_PARAMETER.code_prefix_name)
        # -------------------------------------------------------
        self.TLabel12 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel12.place(relx=0.267, rely=0.151, height=23, width=109)
        self.TLabel12.configure(background="#c0c0c0")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font="TkDefaultFont")
        self.TLabel12.configure(relief="flat")
        self.TLabel12.configure(anchor='w')
        self.TLabel12.configure(justify='left')
        self.TLabel12.configure(text='''点群接近因子：''')

        self.TEntry2 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry2.place(relx=0.45, rely=0.151, relheight=0.035, relwidth=0.21)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")
        self.TEntry2.insert(10, SETTING_PARAMETER.pt_proximity_factor)
        # -------------------------------------------------------
        self.TLabel13 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel13.place(relx=0.267, rely=0.215, height=22, width=109)
        self.TLabel13.configure(background="#c0c0c0")
        self.TLabel13.configure(foreground="#000000")
        self.TLabel13.configure(font="-family 微软雅黑 -size 9 -weight normal -slant roman -underline 0 -overstrike 0")
        self.TLabel13.configure(relief="flat")
        self.TLabel13.configure(anchor='w')
        self.TLabel13.configure(justify='left')
        self.TLabel13.configure(text='''点群最大点数：''')

        self.TEntry3 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry3.place(relx=0.45, rely=0.215, relheight=0.035, relwidth=0.21)
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="ibeam")
        self.TEntry3.insert(10, SETTING_PARAMETER.search_parameter)
        # -------------------------------------------------------
        self.TLabel15 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel15.place(relx=0.2, rely=0.278, height=22, width=145)
        self.TLabel15.configure(background="#c0c0c0")
        self.TLabel15.configure(foreground="#000000")
        self.TLabel15.configure(font="TkDefaultFont")
        self.TLabel15.configure(relief="flat")
        self.TLabel15.configure(anchor='w')
        self.TLabel15.configure(justify='left')
        self.TLabel15.configure(text='''共线误差阈值（°）：''')

        self.TEntry4 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry4.place(relx=0.45, rely=0.278, relheight=0.035, relwidth=0.21)
        self.TEntry4.configure(takefocus="")
        self.TEntry4.configure(cursor="ibeam")
        self.TEntry4.insert(10, SETTING_PARAMETER.line_error)
        # -------------------------------------------------------
        self.TLabel16 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel16.place(relx=0.317, rely=0.341, height=23, width=79)
        self.TLabel16.configure(background="#c0c0c0")
        self.TLabel16.configure(foreground="#000000")
        self.TLabel16.configure(font="TkDefaultFont")
        self.TLabel16.configure(relief="flat")
        self.TLabel16.configure(anchor='w')
        self.TLabel16.configure(justify='left')
        self.TLabel16.configure(text='''剔除因子：''')

        self.TEntry5 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry5.place(relx=0.45, rely=0.341, relheight=0.036, relwidth=0.21)
        self.TEntry5.configure(takefocus="")
        self.TEntry5.configure(cursor="ibeam")
        self.TEntry5.insert(10, SETTING_PARAMETER.reject_factor)
        # -------------------------------------------------------
        self.TLabel17 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel17.place(relx=0.317, rely=0.404, height=22, width=78)
        self.TLabel17.configure(background="#c0c0c0")
        self.TLabel17.configure(foreground="#000000")
        self.TLabel17.configure(font="TkDefaultFont")
        self.TLabel17.configure(relief="flat")
        self.TLabel17.configure(anchor='w')
        self.TLabel17.configure(justify='left')
        self.TLabel17.configure(text='''交比误差：''')

        self.TEntry6 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry6.place(relx=0.45, rely=0.404, relheight=0.035, relwidth=0.21)
        self.TEntry6.configure(takefocus="")
        self.TEntry6.configure(cursor="ibeam")
        self.TEntry6.insert(10, SETTING_PARAMETER.cross_error)
        # -------------------------------------------------------
        self.TLabel18 = ttk.Label(self.scan_set_notebook_code_pt)
        self.TLabel18.place(relx=0.267, rely=0.468, height=22, width=109)
        self.TLabel18.configure(background="#c0c0c0")
        self.TLabel18.configure(foreground="#000000")
        self.TLabel18.configure(font="TkDefaultFont")
        self.TLabel18.configure(relief="flat")
        self.TLabel18.configure(anchor='w')
        self.TLabel18.configure(justify='left')
        self.TLabel18.configure(text='''仿射变换误差：''')

        self.TEntry7 = ttk.Entry(self.scan_set_notebook_code_pt, justify='center')
        self.TEntry7.place(relx=0.45, rely=0.468, relheight=0.035, relwidth=0.21)
        self.TEntry7.configure(takefocus="")
        self.TEntry7.configure(cursor="ibeam")
        self.TEntry7.insert(10, SETTING_PARAMETER.affine_error)
        # -------------------------------------------------------------
        self.code_scan_set_check_Button = ttk.Button(self.scan_set_notebook_code_pt)
        self.code_scan_set_check_Button.place(relx=0.483, rely=0.593, height=40
                , width=89)
        self.code_scan_set_check_Button.configure(command=scan_setting_win_support.code_scan_set_check_Button_click)
        self.code_scan_set_check_Button.configure(takefocus="")
        self.code_scan_set_check_Button.configure(text='''确定''')
        self.code_scan_set_check_Button.configure(cursor="hand2")

        self.code_scan_set_exit_Button = ttk.Button(self.scan_set_notebook_code_pt)
        self.code_scan_set_exit_Button.place(relx=0.683, rely=0.593, height=40
                , width=89)
        self.code_scan_set_exit_Button.configure(command=scan_setting_win_support.code_scan_set_exit_Button_click)
        self.code_scan_set_exit_Button.configure(takefocus="")
        self.code_scan_set_exit_Button.configure(text='''退出''')
        self.code_scan_set_exit_Button.configure(cursor="hand2")
        self.scan_set_notebook.bind('<Button-1>',_button_press)
        self.scan_set_notebook.bind('<ButtonRelease-1>',_button_release)
        self.scan_set_notebook.bind('<Motion>',_mouse_over)

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index

def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except TclError:
        pass
    if "close" in element and widget._active == index:
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])



