from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPen, QColor
import random

class MatrixBackground(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAutoFillBackground(True)
        
        if parent:
            self.resize(parent.size())
        
        self.points = []
        self.lines = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_points)
        self.timer.start(30)  
        self.glow_points = []  
        self.opacity = 0.02  

    def update_points(self):
        width = self.width()
        height = self.height()
        
        if len(self.points) < 100:  
            self.points.append([random.randint(0, width), 
                              random.randint(0, height),
                              random.uniform(-2, 2),  
                              random.uniform(-2, 2)])

        for point in self.points:
            point[0] += point[2]
            point[1] += point[3]
            
            if point[0] < 0 or point[0] > width:
                point[2] *= -1
            if point[1] < 0 or point[1] > height:
                point[3] *= -1

        self.lines = []
        for i, point1 in enumerate(self.points):
            for point2 in self.points[i+1:]:
                distance = ((point1[0] - point2[0])**2 + 
                          (point1[1] - point2[1])**2)**0.5
                if distance < 100:
                    self.lines.append((point1, point2, distance))

        self.glow_points = random.sample(self.points, min(len(self.points), 10))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        painter.fillRect(self.rect(), QColor(0, 0, 0, 0))
        
        for line in self.lines:
            opacity = max(0, min(1.0, 1 - (line[2] / 100)))  
            color = QColor(46, 204, 113)
            color.setAlphaF(opacity * 0.7)  
            painter.setPen(QPen(color, 1.5))
            painter.drawLine(int(line[0][0]), int(line[0][1]),
                           int(line[1][0]), int(line[1][1]))
        
        for point in self.points:
            color = QColor(46, 204, 113)
            color.setAlphaF(0.9)  
            painter.setPen(QPen(color, 4))
            painter.drawPoint(int(point[0]), int(point[1]))
        
        for point in self.glow_points:

            glow = QColor(46, 204, 113)
            glow.setAlphaF(0.3)  
            painter.setPen(QPen(glow, 16))
            painter.drawPoint(int(point[0]), int(point[1]))
            
            center = QColor(46, 204, 113)
            center.setAlphaF(0.9)  
            painter.setPen(QPen(center, 8))
            painter.drawPoint(int(point[0]), int(point[1]))
