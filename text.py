from PyQt6.QtWidgets import (
    QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QColorDialog, QHBoxLayout
)
from PyQt6.QtGui import QTextCharFormat, QTextCursor, QColor, QFont, QPixmap
from PyQt6.QtCore import Qt
import sys

class PyQtEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Text Editor")
        self.resize(800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text = QTextEdit()
        self.layout.addWidget(self.text)

        # Buttons
        btn_layout = QHBoxLayout()
        self.layout.addLayout(btn_layout)

        bold_btn = QPushButton("Bold")
        bold_btn.clicked.connect(self.toggle_bold)
        btn_layout.addWidget(bold_btn)

        italic_btn = QPushButton("Italic")
        italic_btn.clicked.connect(self.toggle_italic)
        btn_layout.addWidget(italic_btn)

        color_btn = QPushButton("Text Color")
        color_btn.clicked.connect(self.change_color)
        btn_layout.addWidget(color_btn)

        highlight_btn = QPushButton("Highlight")
        highlight_btn.clicked.connect(self.highlight_text)
        btn_layout.addWidget(highlight_btn)

        bg_btn = QPushButton("Background Image")
        bg_btn.clicked.connect(self.set_background)
        btn_layout.addWidget(bg_btn)

        open_btn = QPushButton("Open")
        open_btn.clicked.connect(self.open_file)
        btn_layout.addWidget(open_btn)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_file)
        btn_layout.addWidget(save_btn)

        self.bg_label = None

    def toggle_bold(self):
        fmt = QTextCharFormat()
        cursor = self.text.textCursor()
        fmt.setFontWeight(QFont.Weight.Bold if cursor.charFormat().fontWeight() != QFont.Weight.Bold else QFont.Weight.Normal)
        cursor.mergeCharFormat(fmt)

    def toggle_italic(self):
        fmt = QTextCharFormat()
        cursor = self.text.textCursor()
        fmt.setFontItalic(not cursor.charFormat().fontItalic())
        cursor.mergeCharFormat(fmt)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            fmt = QTextCharFormat()
            fmt.setForeground(color)
            self.text.textCursor().mergeCharFormat(fmt)

    def highlight_text(self):
        color = QColorDialog.getColor()
        if color.isValid():
            fmt = QTextCharFormat()
            fmt.setBackground(color)
            self.text.textCursor().mergeCharFormat(fmt)

    def set_background(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Background Image", "", "Images (*.png *.jpg *.jpeg *.webp *.avif)")
        if path:
            pixmap = QPixmap(path).scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
            self.setStyleSheet(f"QTextEdit {{background-image: url({path}); background-repeat: no-repeat; background-position: center;}}")

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt *.md *.log)")
        if path:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                self.text.setPlainText(f.read())

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt *.md *.log)")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = PyQtEditor()
    editor.show()
    sys.exit(app.exec())
