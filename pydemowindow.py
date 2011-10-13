import sys
import string
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_pydemowindow import Ui_PyDemoWindow


class ImageLoadingError(Exception):
    pass


def make_empty_image(width, height, fill_color=QtGui.QColor(0, 0, 0, 0)):
    image = QtGui.QImage(width, height, QtGui.QImage.Format_ARGB32)
    image.fill(fill_color.rgb())
    return image

def expand_rect(rect, left_padding=0, top_padding=0, right_padding=0, bottom_padding=0,
                      left_right_padding=None, top_bottom_padding=None, padding=None):
    if padding is not None:
        left_padding = top_padding = right_padding = bottom_padding = padding
    else:
        if left_right_padding is not None:
            left_padding = right_padding = left_right_padding
        if top_bottom_padding is not None:
            top_padding = bottom_padding = top_bottom_padding
    rect = rect.__class__(rect.left() - left_padding, rect.top() - top_padding,
                          rect.width() + left_padding + right_padding,
                          rect.height() + top_padding + bottom_padding)
    return rect

def load_pixmap(filename):
    image = QtGui.QImage(filename)
    if image.isNull():
        raise ImageLoadingError
    pixmap = QtGui.QPixmap.fromImage(image)
    return pixmap


class ExtendedRectItem(QtGui.QGraphicsRectItem):
    def __init__(self, *args):
        QtGui.QGraphicsRectItem.__init__(self, *args)

    @property
    def pen_width(self):
        return self.pen().width()

    @pen_width.setter
    def pen_width(self, width):
        pen = self.pen()
        pen.setWidth(width)
        self.setPen(pen)

    @property
    def pen_color(self):
        return self.pen().color()

    @pen_color.setter
    def pen_color(self, color):
        pen = self.pen()
        pen.setColor(color)
        self.setPen(pen)

    @property
    def brush_color(self):
        return self.brush().color()

    @brush_color.setter
    def brush_color(self, color):
        brush = self.brush()
        brush.setColor(color)
        self.setBrush(brush)


class PyDemoWindow(QtGui.QMainWindow, Ui_PyDemoWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
        self.big_font_size = self.bigFontSizeBox.value()
        self.small_font_size = self.smallFontSizeBox.value()

        scene = QtGui.QGraphicsScene()
        self.graphicsView.setScene(scene)

        self._view = View(model=self)
        self._controller = Controller(model=self, view=self._view)

    @property
    def scene(self):
        return self.graphicsView.scene()

    @property
    def text(self):
        lines = unicode(self.textEdit.toPlainText()).splitlines()
        return filter(lambda s: s, map(string.strip, lines))

    @text.setter
    def text(self, new_text):
        self.textEdit.setPlainText(new_text)

    @property
    def top_padding(self):
        return self.topPaddingBox.value()

    @top_padding.setter
    def top_padding(self, value):
        self.topPaddingBox.setValue(value)

    @property
    def right_padding(self):
        return self.rightPaddingBox.value()

    @right_padding.setter
    def right_padding(self, value):
        self.rightPaddingBox.setValue(value)

    @property
    def bottom_padding(self):
        return self.bottomPaddingBox.value()

    @bottom_padding.setter
    def bottom_padding(self, value):
        self.bottomPaddingBox.setValue(value)

    @property
    def left_padding(self):
        return self.leftPaddingBox.value()

    @left_padding.setter
    def left_padding(self, value):
        self.leftPaddingBox.setValue(value)

    @property
    def frame_width(self):
        return self.frameWidthBox.value()

    @frame_width.setter
    def frame_width(self, value):
        self.frameWidthBox.setValue(value)

    @property
    def text_interval(self):
        return self.textIntervalBox.value()

    @text_interval.setter
    def text_interval(self, value):
        self.textIntervalBox.setValue(value)

    @property
    def bottom_text_padding(self):
        return self.bottomTextPaddingBox.value()

    @bottom_text_padding.setter
    def bottom_text_padding(self, value):
        self.bottomPaddingBox.setValue(value)

    @property
    def frame_spacing(self):
        return self.frameSpacingBox.value()

    @frame_spacing.setter
    def frame_spacing(self, value):
        self.frameSpacingBox.setValue(value)

    @property
    def background_color(self):
        return QtGui.QColor(self.backgroundColorEdit.text())

    @background_color.setter
    def background_color(self, color):
        self.backgroundColorEdit.setValue(color.name())

    @property
    def font_color(self):
        return QtGui.QColor(self.fontColorEdit.text())

    @font_color.setter
    def font_color(self, color):
        self.fontColorEdit.setValue(color.name())

    @property
    def frame_color(self):
        return QtGui.QColor(self.frameColorEdit.text())

    @frame_color.setter
    def frame_color(self, color):
        self.frameColorEdit.setValue(color.name())

    @property
    def scale_down(self):
        return self.scaleDownBox.value()

    @scale_down.setter
    def scale_down(self, value):
        self.scaleDownBox.setValue(value)

    @property
    def big_font(self):
        return self.bigFontComboBox.currentFont()

    @big_font.setter
    def big_font(self, font):
        self.bigFontComboBox.setCurrentFont(font)

    @property
    def big_font_size(self):
        return self.bigFontComboBox.currentFont().pointSize()

    @big_font_size.setter
    def big_font_size(self, size):
        font = self.bigFontComboBox.currentFont()
        font.setPointSize(size)
        self.bigFontComboBox.setCurrentFont(font)

    @property
    def small_font(self):
        return self.smallFontComboBox.currentFont()

    @small_font.setter
    def small_font(self, font):
        self.smallFontComboBox.setCurrentFont(font)

    @property
    def small_font_size(self):
        return self.smallFontComboBox.currentFont().pointSize()

    @small_font_size.setter
    def small_font_size(self, size):
        font = self.smallFontComboBox.currentFont()
        font.setPointSize(size)
        self.smallFontComboBox.setCurrentFont(font)

    @property
    def quality(self):
        return self.imageQualityBox.value()

    @quality.setter
    def quality(self, value):
        self.imageQualityBox.setValue(value)

    def get_open_file_name(self):
        return QtGui.QFileDialog.getOpenFileName(self, self.tr('Open Image'), '',
                self.tr('Image Files (*.png *.jpg *.bmp)'))

    def get_save_file_name(self):
        return QtGui.QFileDialog.getSaveFileName(self, self.tr('Save As...'), '',
                self.tr('Image Files (*.png *.jpg *.bmp)'))


class View(object):
    def __init__(self, model):
        self._model = model
        self._scene = model.scene

        self._background_rect_item = ExtendedRectItem()
        self._background_rect_item.setZValue(-1)
        self._background_rect_item.setBrush(QtGui.QBrush(QtCore.Qt.SolidPattern))
        self._pixmap_item = QtGui.QGraphicsPixmapItem()
        self._frame_rect_item = ExtendedRectItem()
        self._frame_rect_item.setBrush(QtGui.QBrush(QtCore.Qt.NoBrush))

        scene = self._scene
        scene.addItem(self._background_rect_item)
        scene.addItem(self._pixmap_item)
        scene.addItem(self._frame_rect_item)

    def pixmap_from_file(self, filename):
        pixmap = load_pixmap(filename)
        self._pixmap_item.setPixmap(pixmap)
        self._pixmap_item.original_pixmap = pixmap
        self.scale_pixmap_if_needed()
        self.lay_out()

    def save_demotivator_to_file(self, filename):
        image = self.render_scene()
        image.save(filename, quality=self._model.quality)

    def render_scene(self):
        scene = self._scene
        rect = scene.sceneRect()
        width, height = rect.width(), rect.height()
        image = make_empty_image(width, height)
        self.render_to_image(scene, image)
        return image

    def render_to_image(self, view_or_scene, image):
        painter = QtGui.QPainter(image)
        painter.setRenderHints(QtGui.QPainter.Antialiasing |
                               QtGui.QPainter.TextAntialiasing)
        view_or_scene.render(painter)
        painter.end()

    def lay_out(self):
        rect = self.lay_out_pixmap()
        self.lay_out_frame(rect)
        rect = self.lay_out_background(rect)
        text_width, text_height = self.lay_out_text(rect)
        self.expand_background(text_width, text_height)
        self.update_scene_rect()

    def lay_out_pixmap(self):
        self.scale_pixmap_if_needed()
        return self._pixmap_item.boundingRect()

    def lay_out_text(self, background_rect):
        self.remove_all_text_items()

        start_y = background_rect.bottom()
        text_offset_y = text_width = 0

        text = self._model.text
        center_x = (background_rect.width() - (self._model.left_padding +
                                               self._model.right_padding)) / 2
        big_font, small_font = self._model.big_font, self._model.small_font
        text_interval = self._model.text_interval
        font_color = self._model.font_color

        for index, line in enumerate(text):
            width, height = self.make_and_align_text_item(
                line,
                font = small_font if index else big_font,
                color = font_color,
                center_x = center_x,
                y = start_y + text_offset_y
            )
            text_width = max(text_width, width)
            text_offset_y += height + text_interval
        return text_width, text_offset_y - text_interval

    def lay_out_background(self, image_rect):
        item = self._background_rect_item
        item.brush_color = self._model.background_color
        rect = expand_rect(image_rect, self._model.left_padding, self._model.top_padding,
                                       self._model.right_padding, self._model.bottom_padding)
        item.setRect(rect)
        return rect

    def lay_out_frame(self, image_rect):
        item = self._frame_rect_item
        item.pen_width = self._model.frame_width
        item.pen_color = self._model.frame_color
        item.setRect(expand_rect(image_rect, padding=self._model.frame_spacing))
        return image_rect

    def expand_background(self, text_width, text_height):
        item = self._background_rect_item
        rect = item.rect()
        rect.setHeight(rect.height() + text_height + self._model.bottom_text_padding)
        text_width_with_padding = (text_width + self._model.left_padding +
                                                self._model.right_padding)
        if text_width_with_padding > rect.width():
            padding = (text_width_with_padding - rect.width()) / 2.0
            rect = expand_rect(rect, left_right_padding=padding)
        item.setRect(rect)

    def update_scene_rect(self):
        scene = self._scene
        rect = scene.itemsBoundingRect()
        scene.setSceneRect(rect)

    def scale_pixmap_if_needed(self):
        item = self._pixmap_item
        pixmap = item.original_pixmap
        scale_to = self._model.scale_down
        if scale_to and (pixmap.width() > scale_to or
                         pixmap.height() > scale_to):
            pixmap = pixmap.scaled(scale_to, scale_to, QtCore.Qt.KeepAspectRatio,
                                                       QtCore.Qt.SmoothTransformation)
        item.setPixmap(pixmap)

    def remove_all_text_items(self):
        scene = self._scene
        for item in scene.items():
            if isinstance(item, QtGui.QGraphicsTextItem):
                scene.removeItem(item)

    def make_and_align_text_item(self, text, font, color, center_x, y):
        item = self.make_text_item(text, font=font, color=color)
        rect = item.boundingRect()
        width, height = rect.width(), rect.height()
        item.setPos(center_x - width / 2, y)
        return width, height

    def make_text_item(self, text, font, color):
        item = QtGui.QGraphicsTextItem(text, scene=self._scene)
        item.setFont(font)
        item.setDefaultTextColor(color)
        return item


class Controller(object):
    def __init__(self, model, view):
        self._model = model
        self._view = view

        self._timer = QtCore.QTimer()
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._view.lay_out)

        for widget in self._model.findChildren(QtGui.QWidget):
            if isinstance(widget, QtGui.QTextEdit) or isinstance(widget, QtGui.QLineEdit):
                signal = widget.textChanged
            elif isinstance(widget, QtGui.QSpinBox):
                signal = widget.valueChanged
            elif isinstance(widget, QtGui.QFontComboBox):
                signal = widget.currentFontChanged
            else:
                continue
            signal.connect(self.on_some_value_changed)

        self._model.actionOpen.triggered.connect(self.on_actionOpen_triggered)
        self._model.actionSaveAs.triggered.connect(self.on_actionSaveAs_triggered)
        self._model.bigFontSizeBox.valueChanged.connect(self.on_bigFontSizeBox_valueChanged)
        self._model.smallFontSizeBox.valueChanged.connect(self.on_smallFontSizeBox_valueChanged)

    def on_some_value_changed(self, *args):
        self.delayed_lay_out()

    def delayed_lay_out(self):
        self._timer.start(1000)

    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        filename = self._model.get_open_file_name()
        if filename:
            self._view.pixmap_from_file(filename)

    @QtCore.pyqtSlot()
    def on_actionSaveAs_triggered(self):
        filename = self._model.get_save_file_name()
        if filename:
            self._view.save_demotivator_to_file(filename)

    @QtCore.pyqtSlot(float)
    def on_bigFontSizeBox_valueChanged(self, size):
        self._model.big_font_size = size

    @QtCore.pyqtSlot(float)
    def on_smallFontSizeBox_valueChanged(self, size):
        self._model.small_font_size = size


app = QtGui.QApplication(sys.argv)
mainWindow = PyDemoWindow()
mainWindow.show()
sys.exit(app.exec_())

