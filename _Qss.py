qss = '''

/* === Shared === */
QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, 
QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {
    background-color: #222222;
    color: #BBBBBB;
    font-family: "Segoe UI";
}
 
/* === QWidget === */
QWidget:window {
    background: #222222;
    color: #BBBBBB;
    font-family: "Segoe UI";
}
 
/* === QPushButton === */
QPushButton {
    border: 1px solid #333333;
    padding: 4px;
    min-width: 65px;
    min-height: 12px;
}
 
QPushButton:hover {
    background-color: #333333;
    border-color: #444444;
}
 
QPushButton:pressed {
    background-color: #111111;
    border-color: #333333;
    color: yellow;
}
 
QPushButton:disabled {
    color: #333333;
}
 
/* === Checkable items === */
QCheckBox::indicator, QRadioButton::indicator, QTreeView::indicator {
    width: 16px;
    height: 16px;
    background-color: #111111;
    border: 1px solid #333333;
}
 
/* === QComboBox === */
QComboBox {
    background-color: black;
    border: 1px solid #333333;
    color: white;
    padding:1px 2em 1px 3px;
}
 
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    border-left: 1px solid #333333;
}
 
QComboBox::down-arrow {
    border: 2px solid #333333;
    width: 6px;
    height: 6px;
    background: #5f5f5f;
}
 
/* =================== */
QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox {
    background-color: black;
    color: #BBBBBB;
    border: 1px solid #333333;
}
 
QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox {
    border-color: #333333;
    border: 1px solid #333333;
 
}
 
/* === QHeaderView === */
QHeaderView::section {
    background: #222222;
    border: 0;
    color: #BBBBBB;
    padding: 3px 0 3px 4px;
}
 


/* === QTreeView === */
QTreeView::item {
    background: black;
}
 
QTreeView::item:hover {
    background: #333333;
}
 
QTreeView::item:selected {
    background: #111111;
    color: yellow;
}
 
QTreeView::branch {
 
}
 
QTreeView::branch:has-siblings:adjoins-item {
 
}
 
QTreeView::branch:has-siblings:!adjoins-item {
 
}
 
QTreeView::branch:closed:has-children:has-siblings {
 
}
 
QTreeView::branch:has-children:!has-siblings:closed {
 
}
 
QTreeView::branch:!has-children:!has-siblings:adjoins-item {
 
}
 
QTreeView::branch:open:has-children:has-siblings {
 
}
 
QTreeView::branch:open:has-children:!has-siblings {
 
}
 
/* === Customizations === */
QFrame#infoLabel {
    border: 1px inset #333333;
}
2.
 
.QWidget {
   background-color: beige;
}
 
QToolBar {
    background-color: beige;
}
 
QDialog, QFileDialog {
    background-color: beige;
}
 
QTabWidget::pane { /* The tab widget frame */
    border-top: 2px solid #C2C7CB;
}
 
QTabWidget::tab-bar {
    left: 5px; /* move to the right by 5px */
}
 
QTabBar, QTabWidget {
    background-color: beige;
}
QTabBar::tab {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
     border: 1px solid darkkhaki;
     border-bottom-color: #C2C7CB; /* same as the pane color */
     border-top-left-radius: 4px;
     border-top-right-radius: 4px;
     min-width: 8ex;
     padding: 2px;
 }
QTabBar::tab:selected, QTabBar::tab:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
}
 
QTabBar::tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB; /* same as pane color */
}
 
QTabBar::tab:!selected {
    margin-top: 2px; /* make non-selected tabs look smaller */
}
 
/* Nice Windows-XP-style password character. */
QLineEdit[echoMode="2"] {
    lineedit-password-character: 9679;
}
 
QHeaderView::section {
     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                       stop:0 #616161, stop: 0.5 #505050,
                                       stop: 0.6 #434343, stop:1 #656565);
     color: white;
     padding-left: 4px;
     border: 1px solid #6c6c6c;
 }
 
 QHeaderView::section:checked
 {
     background-color: red;
 }
 
 
/* We provide a min-width and min-height for push buttons
   so that they look elegant regardless of the width of the text. */
QPushButton {
    background-color: palegoldenrod;
    border-width: 2px;
    border-color: darkkhaki;
    border-style: solid;
    border-radius: 5;
    padding: 3px;
    min-width: 9ex;
    min-height: 2.5ex;
}
 
QPushButton:hover {
   background-color: khaki;
}
 
/* Increase the padding, so the text is shifted when the button is
   pressed. */
QPushButton:pressed {
    padding-left: 5px;
    padding-top: 5px;
    background-color: #d0d67c;
}
 
QLabel, QAbstractButton {
    font: bold;
}
 

 
/* We reserve 1 pixel space in padding. When we get the focus,
   we kill the padding and enlarge the border. This makes the items
   glow. */
QLineEdit, QFrame {
    border-width: 1px;
    padding: 1px;
    border-style: solid;
    border-color: darkkhaki;
    border-radius: 5px;
}
 
/* As mentioned above, eliminate the padding and increase the border. */
QLineEdit:focus, QFrame:focus {
    border-width: 3px;
    padding: 0px;
}
 
/* A QLabel is a QFrame  */
QLabel {
    border: none;
    padding: 0;
    background: none;
}
 
/* A QToolTip is a QLabel  */
QToolTip {
    border: 2px solid darkkhaki;
    padding: 5px;
    border-radius: 3px;
    opacity: 200;
}
 
/* Nice to have the background color change when hovered. */
QRadioButton:hover, QCheckBox:hover {
    background-color: wheat;
}
 
/* Force the dialog's buttons to follow the Windows guidelines. */
QDialogButtonBox {
    button-layout: 0;
}
 
 
3.
/*
    Style by evilworks, 2012-2013. pollux@lavabit.com
    This file is Public Domain.
*/
 
/* === Shared === */
QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, 
QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog, QTabBar {
    font-family: "Segoe UI";
    background-color: #888;
    color: #000;
}
 
/* === QWidget === */
QWidget:window {
    font-family: 'Segoe UI';
    background-color: #888;
}
 
/* === QPushButton === */
QPushButton {
    border: 1px solid #555;
    padding: 4px;
    min-width: 65px;
    min-height: 12px;
}
 
QPushButton:hover {
    background-color: #999;
}
 
QPushButton:pressed {
    background-color: #333;
    border-color: #555;
    color: #AAA;
}
 
QPushButton:disabled {
    color: #333333;
}
 
/* === QComboBox === */
QComboBox {
    background-color: #AAA;
    border: 1px solid #555;
    color: black;
}
 
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    border-left: 1px solid #333333;
}
 

/* === QTreeView === */

QTreeView::branch:has:has-siblings::!adjoins-item {
    border-image: url(vline: url(vline.png) ) 0;
}}

QTreeView::branch:has:has-siblings:adjoins:adjoins-item {{
    border-image: url(branch: url(branch-more.png) ) 0;
}}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(branch-end.png) 0;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
        border-image: none;
        image: url(branch-closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
        border-image: none;
        image: url(branch-open.png);
}

'''
