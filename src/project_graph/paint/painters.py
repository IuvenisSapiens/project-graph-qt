from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen

from project_graph.data_struct.connect_straight_line import ConnectStraightLine
from project_graph.data_struct.curve import ConnectCurve, ConnectCurveShifted
from project_graph.data_struct.rectangle import Rectangle
from project_graph.data_struct.text import Text


class ProjectGraphPainter:
    """该类可用于定义样式，他传入的参数一般是data_struct下自定义的某些数据,
    然后做的内容一般是设置相关的Pen，Brush等，然后将其绘制出来
    """

    def __init__(self, painter: QPainter):
        self._painter = painter

    def q_painter(self) -> QPainter:
        return self._painter

    def paint_rect(self, rect: Rectangle):
        self._painter.drawRect(
            QRectF(
                rect.location_left_top.x,
                rect.location_left_top.y,
                rect.width,
                rect.height,
            )
        )

    def paint_text(self, text: Text):
        ascent = self._painter.fontMetrics().ascent()
        self._painter.drawText(
            QPointF(text.left_top.x, text.left_top.y + ascent), text.text
        )

    def paint_text_in_rect(self, str_text: str, rect: Rectangle):
        """
        绘制文本，使得文本中心居中在矩形框内
        :param str_text: 文本内容
        :param rect: 矩形框
        """
        ascent = self._painter.fontMetrics().ascent()
        text_width = self._painter.fontMetrics().width(str_text)
        text_height = self._painter.fontMetrics().height()
        self._painter.drawText(
            QPointF(
                rect.location_left_top.x + (rect.width - text_width) / 2,
                rect.location_left_top.y + (rect.height - text_height) / 2 + ascent,
            ),
            str_text,
        )

    def paint_curve(self, curve: ConnectCurve | ConnectCurveShifted, color: QColor):
        pen = QPen(color, 3)  # 创建QPen并设置颜色和宽度
        self._painter.setRenderHint(QPainter.Antialiasing)
        self._painter.setPen(pen)
        self._painter.setBrush(QBrush())
        self._painter.drawPath(curve.path)
        self._painter.setBrush(color)
        self._painter.drawPath(curve.arrow.path)
        self._painter.setRenderHint(QPainter.Antialiasing, False)

    def paint_straight_line(
        self, straight_line: ConnectStraightLine, color: QColor, with_arrow=True
    ):
        pen = QPen(color, 3)  # 创建QPen并设置颜色和宽度
        self._painter.setRenderHint(QPainter.Antialiasing)
        self._painter.setPen(pen)
        self._painter.setBrush(QBrush())
        self._painter.drawPath(straight_line.path)
        self._painter.setBrush(color)
        if with_arrow:
            self._painter.drawPath(straight_line.arrow.path)
        self._painter.setRenderHint(QPainter.Antialiasing, False)
