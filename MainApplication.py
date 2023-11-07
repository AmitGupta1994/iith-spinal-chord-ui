import random
import sys
import threading

from PyQt5.QtCore import QTimer, Qt, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QVBoxLayout, QScrollArea, QPushButton
from PyQt5.uic import loadUi
from PyQt5.uic.uiparser import QtCore
import pandas as pd

from SpinalChordMuscle import SpinalChordMuscle
from SpinalChordSegment import SpinalChordSegment


class MainApplication(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = loadUi("iith-spinal-chord-main.ui", self)

        self.setWindowTitle("Spinal Chord")

        # C5
        self.segment_c5_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('DELT1_l', 'Deltoid 1 Left'), SpinalChordMuscle('DELT1', 'Deltoid 1 Right'),
            SpinalChordMuscle('DELT2_l', 'Deltoid 2 Left'), SpinalChordMuscle('DELT2', 'Deltoid 2 Right'),
            SpinalChordMuscle('DELT3_l', 'Deltoid 3 Left'), SpinalChordMuscle('DELT3', 'Deltoid 3 Right'),
            SpinalChordMuscle('INFSP_l', 'Infraspinatus Left'), SpinalChordMuscle('INFSP', 'Infraspinatus Right'),
            SpinalChordMuscle('SUPSP_l', 'Supraspinatus Left'), SpinalChordMuscle('SUPSP', 'Supraspinatus Right'),
            SpinalChordMuscle('TMIN_l', 'Teres Minor Left'), SpinalChordMuscle('TMIN', 'Teres Minor Right'),
            SpinalChordMuscle('BIClong_l', 'Biceps Brachii Long Head Left'), SpinalChordMuscle('BIClong', 'Biceps Brachii Long Head Right'),
            SpinalChordMuscle('BICshort_l', 'Biceps Brachii Short Head Left'), SpinalChordMuscle('BICshort', 'Biceps Brachii Short Head Right'),
            SpinalChordMuscle('CORB_l', 'Corachobrachialis Left'), SpinalChordMuscle('CORB', 'Corachobrachialis Right'),
            SpinalChordMuscle('PECM1_l', 'Pectoralis Major 1 Left'), SpinalChordMuscle('PECM1', 'Pectoralis Major 1 Right'),
            SpinalChordMuscle('PECM2_l', 'Pectoralis Major 2 Left'), SpinalChordMuscle('PECM2', 'Pectoralis Major 2 Right'),
            SpinalChordMuscle('PECM3_l', 'Pectoralis Major 2 Left'), SpinalChordMuscle('PECM3', 'Pectoralis Major 2 Right'),

        ]
        self.segment_c5 = SpinalChordSegment("C5", self.segment_c5_muscles)

        # C6
        self.segment_c6_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('BIClong_l', 'Biceps Brachii Long Head Left'), SpinalChordMuscle('BIClong', 'Biceps Brachii Long Head Right'),
            SpinalChordMuscle('BICshort_l', 'Biceps Brachii Short Head Left'), SpinalChordMuscle('BICshort', 'Biceps Brachii Short Head Right'),
            SpinalChordMuscle('CORB_l', 'Corachobrachialis Left'), SpinalChordMuscle('CORB', 'Corachobrachialis Right'),
            SpinalChordMuscle('PECM1_l', 'Pectoralis Major 1 Left'), SpinalChordMuscle('PECM1', 'Pectoralis Major 1 Right'),
            SpinalChordMuscle('PECM2_l', 'Pectoralis Major 2 Left'), SpinalChordMuscle('PECM2', 'Pectoralis Major 2 Right'),
            SpinalChordMuscle('PECM3_l', 'Pectoralis Major 3 Left'), SpinalChordMuscle('PECM3', 'Pectoralis Major 3 Right'),
            SpinalChordMuscle('BRA_l', 'Brachialis Left'), SpinalChordMuscle('BRA', 'Brachialis Right'),
            SpinalChordMuscle('BRD_l', 'Brachioradialis Left'), SpinalChordMuscle('BRD', 'Brachioradialis Right'),
            SpinalChordMuscle('SUBSC_l', 'Subscapularis Left'), SpinalChordMuscle('SUBSC', 'Subscapularis Right'),
            SpinalChordMuscle('TMAJ_l', 'Teres Major Left'), SpinalChordMuscle('TMAJ', 'Teres Major Right'),
            SpinalChordMuscle('DELT1_l', 'Anconeus Left'), SpinalChordMuscle('ANC', 'Anconeus Right'),

        ]
        self.segment_c6 = SpinalChordSegment("C6", self.segment_c6_muscles)

        # C7
        self.segment_c7_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('CORB_l', 'Corachobrachialis Left'), SpinalChordMuscle('CORB', 'Corachobrachialis Right'),
            SpinalChordMuscle('PECM1_l', 'Pectoralis Major 1 Left'), SpinalChordMuscle('PECM1', 'Pectoralis Major 1 Right'),
            SpinalChordMuscle('PECM2_l', 'Pectoralis Major 2 Left'), SpinalChordMuscle('PECM2', 'Pectoralis Major 2 Right'),
            SpinalChordMuscle('PECM3_l', 'Pectoralis Major 3 Left'), SpinalChordMuscle('PECM3', 'Pectoralis Major 3 Right'),
            SpinalChordMuscle('ANC_l', 'Anconeus Left'), SpinalChordMuscle('ANC', 'Anconeus Right'),
            SpinalChordMuscle('LAT1_l', 'Latissimus Dorsi 1 Left'), SpinalChordMuscle('LAT1', 'Latissimus Dorsi 1 Right'),
            SpinalChordMuscle('LAT2_l', 'Latissimus Dorsi 2 Left'), SpinalChordMuscle('LAT2', 'Latissimus Dorsi 2 Right'),
            SpinalChordMuscle('LAT3_l', 'Latissimus Dorsi 3 Left'), SpinalChordMuscle('LAT3', 'Latissimus Dorsi 3 Right'),
            SpinalChordMuscle('PT_l', 'Pronator Teres Left'), SpinalChordMuscle('PT', 'Pronator Teres Right'),
            SpinalChordMuscle('TRIlat_l', 'Triceps Lateral Head Left'), SpinalChordMuscle('TRIlat', 'Triceps Lateral Head Right'),
            SpinalChordMuscle('TRIlong_l', 'Triceps Long Head Left'), SpinalChordMuscle('TRIlong', 'Triceps Long Head Right'),
            SpinalChordMuscle('TRImed_l', 'Triceps Medial Head Left'), SpinalChordMuscle('TRImed', 'Triceps Medial Head Right'),

        ]
        self.segment_c7 = SpinalChordSegment("C7", self.segment_c7_muscles)

        # C8
        self.segment_c8_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('ANC_l', 'Anconeus Left'), SpinalChordMuscle('ANC', 'Anconeus Right'),

        ]
        self.segment_c8 = SpinalChordSegment("C8", self.segment_c8_muscles)

        # T7-T12
        self.segment_t7_t12_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('extobl_l', 'External Oblique Left'), SpinalChordMuscle('extobl_r', 'External Oblique Right'),
            SpinalChordMuscle('intobl_l', 'Internal Oblique Left'), SpinalChordMuscle('intobl_r', 'Internal Oblique Right'),

        ]
        self.segment_t7_t12 = SpinalChordSegment("T7-T12", self.segment_t7_t12_muscles)

        # L1
        self.segment_l1_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('psoas_l', 'Psoas Major Left'), SpinalChordMuscle('psoas_r', 'Psoas Major Right'),
        ]
        self.segment_l1= SpinalChordSegment("L1", self.segment_l1_muscles)

        # L2
        self.segment_l2_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('grac_l', 'Gracilis Left'), SpinalChordMuscle('grac_r', 'Gracilis Right'),
            SpinalChordMuscle('iliacus_l', 'Iliacus Left'), SpinalChordMuscle('iliacus_r', 'Iliacus Right'),
            SpinalChordMuscle('pect_l', 'Pectineus Left'), SpinalChordMuscle('pect_r', 'Pectineus Right'),
            SpinalChordMuscle('add_mag2_l', 'Adductor Magnus Left'), SpinalChordMuscle('add_mag2_r', 'Adductor Magnus Right'),
            SpinalChordMuscle('sar_l', 'Sartorius Left'), SpinalChordMuscle('sar_r', 'Sartorius Right'),

        ]
        self.segment_l2 = SpinalChordSegment("L2", self.segment_l2_muscles)

        # L3
        self.segment_l3_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('add_mag2_l', 'Adductor Magnus Left'), SpinalChordMuscle('add_mag2_r', 'Adductor Magnus Right'),
            SpinalChordMuscle('sar_l', 'Sartorius Left'), SpinalChordMuscle('sar_r', 'Sartorius Right'),
            SpinalChordMuscle('rect_fem_l', 'Rectus Femoris Left'), SpinalChordMuscle('rect_fem_r', 'Rectus Femoris Right'),
            SpinalChordMuscle('vas_int_l', 'Vastus Intermedius Left'), SpinalChordMuscle('vas_int_r', 'Vastus Intermedius Right'),

        ]
        self.segment_l3= SpinalChordSegment("L3", self.segment_l3_muscles)

        # L4
        self.segment_l4_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('rect_fem_l', 'Rectus Femoris Left'), SpinalChordMuscle('rect_fem_r', 'Rectus Femoris Right'),
            SpinalChordMuscle('vas_int_l', 'Vastus Intermedius Left'), SpinalChordMuscle('vas_int_r', 'Vastus Intermedius Right'),
            SpinalChordMuscle('glut_med1_l', 'Gluteus Medius 1 Left'), SpinalChordMuscle('glut_med1_r', 'Gluteus Medius 1 Right'),
            SpinalChordMuscle('glut_med2_l', 'Gluteus Medius 2 Left'), SpinalChordMuscle('glut_med2_r', 'Gluteus Medius 2 Right'),
            SpinalChordMuscle('glut_med3_l', 'Gluteus Medius 3 Left'), SpinalChordMuscle('glut_med3_r', 'Gluteus Medius 3 Right'),
            SpinalChordMuscle('tfl_l', 'Tensor Fascia Latae Left'), SpinalChordMuscle('tfl_r', 'Tensor Fascia Latae Right'),
            SpinalChordMuscle('tib_ant_l', 'Tibialis Anterior Left'), SpinalChordMuscle('tib_ant_r', 'Tibialis Anterior Right'),
            SpinalChordMuscle('tib_post_l', 'Tibialis Posterior Left'), SpinalChordMuscle('tib_post_r', 'Tibialis Posterior Right'),

        ]
        self.segment_l4 = SpinalChordSegment("L4", self.segment_l4_muscles)

        # L5
        self.segment_l5_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('glut_med1_l', 'Gluteus Medius 1 Left'), SpinalChordMuscle('glut_med1_r', 'Gluteus Medius 1 Right'),
            SpinalChordMuscle('glut_med2_l', 'Gluteus Medius 2 Left'), SpinalChordMuscle('glut_med2_r', 'Gluteus Medius 2 Right'),
            SpinalChordMuscle('glut_med3_l', 'Gluteus Medius 3 Left'), SpinalChordMuscle('glut_med3_r', 'Gluteus Medius 3 Right'),
            SpinalChordMuscle('tfl_l', 'Tensor Fascia Latae Left'), SpinalChordMuscle('tfl_r', 'Tensor Fascia Latae Right'),
            SpinalChordMuscle('tib_ant_l', 'Tibialis Anterior Left'), SpinalChordMuscle('tib_ant_r', 'Tibialis Anterior Right'),
            SpinalChordMuscle('tib_post_l', 'Tibialis Posterior Left'), SpinalChordMuscle('tib_post_r', 'Tibialis Posterior Right'),
            SpinalChordMuscle('glut_max1_l', 'Gluteus Maximus 1 Left'), SpinalChordMuscle('glut_max1_r', 'Gluteus Maximus 1 Right'),
            SpinalChordMuscle('glut_max2_l', 'Gluteus Maximus 2 Left'), SpinalChordMuscle('glut_max2_r', 'Gluteus Maximus 2 Right'),
            SpinalChordMuscle('glut_max3_l', 'Gluteus Maximus 3 Left'), SpinalChordMuscle('glut_max3_r', 'Gluteus Maximus 3 Right'),
            SpinalChordMuscle('gem_l', 'Gemelli Left'), SpinalChordMuscle('gem_r', 'Gemelli Left'),
            SpinalChordMuscle('quad_fem_l', 'Quadratus Femoris Left'), SpinalChordMuscle('quad_fem_r', 'Quadratus Femoris Right'),

        ]
        self.segment_l5 = SpinalChordSegment("L5", self.segment_l5_muscles)

        # S1
        self.segment_s1_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('glut_max1_l', 'Gluteus Maximus 1 Left'), SpinalChordMuscle('glut_max1_r', 'Gluteus Maximus 1 Right'),
            SpinalChordMuscle('glut_max2_l', 'Gluteus Maximus 2 Left'), SpinalChordMuscle('glut_max2_r', 'Gluteus Maximus 2 Right'),
            SpinalChordMuscle('glut_max3_l', 'Gluteus Maximus 3 Left'), SpinalChordMuscle('glut_max3_r', 'Gluteus Maximus 3 Right'),
            SpinalChordMuscle('gem_l', 'Gemelli Left'), SpinalChordMuscle('gem_r', 'Gemelli Right'),
            SpinalChordMuscle('quad_fem_l', 'Quadratus Femoris Left'), SpinalChordMuscle('quad_fem_r', 'Quadratus Femoris Right'),
            SpinalChordMuscle('bifemlh_l', 'Biceps Femoris Long Head Left'), SpinalChordMuscle('bifemlh_r', 'Biceps Femoris Long Head Right'),
            SpinalChordMuscle('bifemsh_l', 'Biceps Femoris Short Head Left'), SpinalChordMuscle('bifemsh_r', 'Biceps Femoris Short Head Right'),
            SpinalChordMuscle('peri_l', 'Piriformis Left'), SpinalChordMuscle('peri_r', 'Piriformis Right'),
            SpinalChordMuscle('med_gas_l', 'Medial Gastrocnemius Left'), SpinalChordMuscle('med_gas_r', 'Medial Gastrocnemius Right'),
            SpinalChordMuscle('soleus_l', 'Soleus Left'), SpinalChordMuscle('soleus_r', 'Soleus Right'),

        ]
        self.segment_s1 = SpinalChordSegment("S1", self.segment_s1_muscles)

        # S2
        self.segment_s2_muscles = [
            SpinalChordMuscle('ercspn_l', 'Erector Spinae Left'), SpinalChordMuscle('ercspn_r', 'Erector Spinae Right'),
            SpinalChordMuscle('med_gas_l', 'Medial Gastrocnemius Left'), SpinalChordMuscle('med_gas_r', 'Medial Gastrocnemius Right'),
            SpinalChordMuscle('soleus_l', 'Soleus Left'), SpinalChordMuscle('soleus_r', 'Soleus Right'),

        ]
        self.segment_s2 = SpinalChordSegment("S2", self.segment_s2_muscles)

        ####################################
        # Create a layout for the main window
        main_layout = QHBoxLayout()
        main_layout.setAlignment(Qt.AlignLeft)

        # Get references to the buttons in the .ui file
        btn_width = 180
        btn_height = 40
        self.button1 = QPushButton("Tadasana-Ia")
        self.button1.setFixedSize(btn_width, btn_height)
        self.button2 = QPushButton("Tadasana-II")
        self.button2.setFixedSize(btn_width, btn_height)
        self.button3 = QPushButton("Tadasana-Ib")
        self.button3.setFixedSize(btn_width, btn_height)
        self.button4 = QPushButton("Tadasana-Activation")
        self.button4.setFixedSize(btn_width, btn_height)

        self.button5 = QPushButton("Virkshasana-Ia")
        self.button5.setFixedSize(btn_width, btn_height)
        self.button6 = QPushButton("Virkshasana-II")
        self.button6.setFixedSize(btn_width, btn_height)
        self.button7 = QPushButton("Virkshasana-Ib")
        self.button7.setFixedSize(btn_width, btn_height)
        self.button8 = QPushButton("Virkshasana-Activation")
        self.button8.setFixedSize(btn_width, btn_height)

        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button5.clicked.connect(self.button5_clicked)
        self.button6.clicked.connect(self.button6_clicked)
        self.button7.clicked.connect(self.button7_clicked)
        self.button8.clicked.connect(self.button8_clicked)

        # Create a horizontal layout for the buttons at the top
        buttons_layout = QVBoxLayout()
        buttons_layout.setAlignment(Qt.AlignCenter)

        # Add the buttons to the buttons layout
        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)
        buttons_layout.addWidget(self.button3)
        buttons_layout.addWidget(self.button4)
        buttons_layout.addWidget(self.button5)
        buttons_layout.addWidget(self.button6)
        buttons_layout.addWidget(self.button7)
        buttons_layout.addWidget(self.button8)


        # Add the buttons layout to the rectangle main layout
        self.segments = []

        self.segments.append(self.segment_c5)
        self.segments.append(self.segment_c6)
        self.segments.append(self.segment_c7)
        self.segments.append(self.segment_c8)
        self.segments.append(self.segment_c8)
        self.segments.append(self.segment_t7_t12)
        self.segments.append(self.segment_l1)
        self.segments.append(self.segment_l2)
        self.segments.append(self.segment_l3)
        self.segments.append(self.segment_l4)
        self.segments.append(self.segment_l5)
        self.segments.append(self.segment_s1)
        self.segments.append(self.segment_s2)

        rec_main_layout = QVBoxLayout()

        rec_main_layout.addWidget(self.segment_c5)
        rec_main_layout.addWidget(self.segment_c6)
        rec_main_layout.addWidget(self.segment_c7)
        rec_main_layout.addWidget(self.segment_c8)
        rec_main_layout.addWidget(self.segment_t7_t12)
        rec_main_layout.addWidget(self.segment_l1)
        rec_main_layout.addWidget(self.segment_l2)
        rec_main_layout.addWidget(self.segment_l3)
        rec_main_layout.addWidget(self.segment_l4)
        rec_main_layout.addWidget(self.segment_l5)
        rec_main_layout.addWidget(self.segment_s1)
        rec_main_layout.addWidget(self.segment_s2)

        # Add all to main layout
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(rec_main_layout)

        # Set the main layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Update Every 1 ms
        # self.color_timer = QTimer(self)
        # self.color_timer.timeout.connect(self.updateColors)
        # self.color_timer.start(1)  # 1000 ms (1 second) interval



    def initialize_ui(self):
        # self.ui.layout.addWidget(self.segment_c5)
        self.setCentralWidget(self.segment_c5)
        # self.setCentralWidget(self.segment_c6)

        pass

    def update_segments(self):
        # TODO Play the video

        for index, row in self.df.iterrows():
            for segment in self.segments:
                for muscles in segment.muscles_name_list:
                    try:
                        index_ = self.column_names.index(muscles.name)
                        muscles.value = row[index_]
                    except:
                        pass

                segment.update_segment()

        #Reset
        for segment in self.segments:
            for muscles in segment.muscles_name_list:
                muscles.value = 0
            segment.reset_segment()

    def updateColors(self):
        for segment in self.segments:
            segment.update_segment()

    def button1_clicked(self):
        split_value = "_Ia"
        print("btn1")
        df = pd.read_csv('S17_Tadasana_Afferents_Test.csv')
        print('shape before filter:', df.shape)

        filtered_columns = df.filter(like=split_value, axis=1)
        df = df[filtered_columns.columns]
        print('shape after filter:', df.shape)

        # Split Column name so as to remove '_Ia'
        df.columns = [col.split(split_value)[0] for col in df.columns]
        print("final df columns", df.columns)

        # print(df)

        for column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            if min_val == max_val:
                df[column] = 128  # If min and max are the same, set the column to 128 (midpoint of 0-255)
            else:
                df[column] = (df[column] - min_val) / (max_val - min_val) * 255

        print("Original DataFrame:")
        # print(df)

        self.df = df
        self.column_names = df.columns.tolist()

        update_segments_thread = threading.Thread(target=self.update_segments)
        # Start the thread
        update_segments_thread.start()

        # update_segments_thread.join()

        # self.color_timer = QTimer(self)
        # self.color_timer.timeout.connect(self.updateColors)
        # self.color_timer.start(1000)


    def button2_clicked(self):
        split_value = "_II"
        print("btn1")
        df = pd.read_csv('S17_Tadasana_Afferents_Test.csv')
        print('shape before filter:', df.shape)

        filtered_columns = df.filter(like=split_value, axis=1)
        df = df[filtered_columns.columns]
        print('shape after filter:', df.shape)

        # Split Column name so as to remove '_Ia'
        df.columns = [col.split(split_value)[0] for col in df.columns]
        print("final df columns", df.columns)

        # print(df)

        for column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            if min_val == max_val:
                df[column] = 128  # If min and max are the same, set the column to 128 (midpoint of 0-255)
            else:
                df[column] = (df[column] - min_val) / (max_val - min_val) * 255

        print("Original DataFrame:")
        # print(df)

        self.df = df
        self.column_names = df.columns.tolist()

        update_segments_thread = threading.Thread(target=self.update_segments)
        # Start the thread
        update_segments_thread.start()

        # update_segments_thread.join()

        # self.color_timer = QTimer(self)
        # self.color_timer.timeout.connect(self.updateColors)
        # self.color_timer.start(1000)

    def button3_clicked(self):
        split_value = "_Ib"
        print("btn1")
        df = pd.read_csv('S17_Tadasana_Afferents_Test.csv')
        print('shape before filter:', df.shape)

        filtered_columns = df.filter(like=split_value, axis=1)
        df = df[filtered_columns.columns]
        print('shape after filter:', df.shape)

        # Split Column name so as to remove '_Ia'
        df.columns = [col.split(split_value)[0] for col in df.columns]
        print("final df columns", df.columns)

        # print(df)

        for column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            if min_val == max_val:
                df[column] = 128  # If min and max are the same, set the column to 128 (midpoint of 0-255)
            else:
                df[column] = (df[column] - min_val) / (max_val - min_val) * 255

        print("Original DataFrame:")
        # print(df)

        self.df = df
        self.column_names = df.columns.tolist()

        update_segments_thread = threading.Thread(target=self.update_segments)
        # Start the thread
        update_segments_thread.start()

        # update_segments_thread.join()
        #
        # self.color_timer = QTimer(self)
        # self.color_timer.timeout.connect(self.updateColors)
        # self.color_timer.start(1000)


    def button4_clicked(self):
        pass

    def button5_clicked(self):
        split_value = "_Ia"
        print("btn1")
        df = pd.read_csv('S17_Vrikshasana_Afferents_Test.csv')
        print('shape before filter:', df.shape)

        filtered_columns = df.filter(like=split_value, axis=1)
        df = df[filtered_columns.columns]
        print('shape after filter:', df.shape)

        # Split Column name so as to remove '_Ia'
        df.columns = [col.split(split_value)[0] for col in df.columns]
        print("final df columns", df.columns)

        # print(df)

        for column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            if min_val == max_val:
                df[column] = 128  # If min and max are the same, set the column to 128 (midpoint of 0-255)
            else:
                df[column] = (df[column] - min_val) / (max_val - min_val) * 255

        print("Original DataFrame:")
        # print(df)

        self.df = df
        self.column_names = df.columns.tolist()

        update_segments_thread = threading.Thread(target=self.update_segments)
        # Start the thread
        update_segments_thread.start()

    def button6_clicked(self):
        split_value = "_II"
        print("btn1")
        df = pd.read_csv('S17_Vrikshasana_Afferents_Test.csv')
        print('shape before filter:', df.shape)

        filtered_columns = df.filter(like=split_value, axis=1)
        df = df[filtered_columns.columns]
        print('shape after filter:', df.shape)

        # Split Column name so as to remove '_Ia'
        df.columns = [col.split(split_value)[0] for col in df.columns]
        print("final df columns", df.columns)

        # print(df)

        for column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            if min_val == max_val:
                df[column] = 128  # If min and max are the same, set the column to 128 (midpoint of 0-255)
            else:
                df[column] = (df[column] - min_val) / (max_val - min_val) * 255

        print("Original DataFrame:")
        # print(df)

        self.df = df
        self.column_names = df.columns.tolist()

        update_segments_thread = threading.Thread(target=self.update_segments)
        # Start the thread
        update_segments_thread.start()

    def button7_clicked(self):
        split_value = "_Ib"
        print("btn1")
        df = pd.read_csv('S17_Vrikshasana_Afferents_Test.csv')
        print('shape before filter:', df.shape)

        filtered_columns = df.filter(like=split_value, axis=1)
        df = df[filtered_columns.columns]
        print('shape after filter:', df.shape)

        # Split Column name so as to remove '_Ia'
        df.columns = [col.split(split_value)[0] for col in df.columns]
        print("final df columns", df.columns)

        # print(df)

        for column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            if min_val == max_val:
                df[column] = 128  # If min and max are the same, set the column to 128 (midpoint of 0-255)
            else:
                df[column] = (df[column] - min_val) / (max_val - min_val) * 255

        print("Original DataFrame:")
        # print(df)

        self.df = df
        self.column_names = df.columns.tolist()

        update_segments_thread = threading.Thread(target=self.update_segments)
        # Start the thread
        update_segments_thread.start()

    def button8_clicked(self):
        pass

    def data_ready_thread(self):
        pass

class Worker(QObject):
    finished = pyqtSignal()

    def run(self):
        for i in range(10):
            self.update_signal.emit(f"Update {i}")

        self.finished.emit()


# Run the App
def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
