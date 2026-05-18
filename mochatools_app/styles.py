# ── Stylesheet ───────────────────────────────────────────────────────────────
STYLESHEET = """
QMainWindow, QWidget#root {
    background-color: #111214;
}

QWidget {
    background-color: transparent;
    color: #e0e0e0;
    font-family: "Segoe UI", "SF Pro Display", "Helvetica Neue", sans-serif;
    font-size: 13px;
}

/* Section cards */
QFrame#card {
    background-color: #1a1c1f;
    border: 1px solid #2a2d32;
    border-left: 3px solid #c8975a;
    border-radius: 8px;
    padding: 4px;
}

/* Section header labels */
QLabel#section_header {
    color: #8a8f98;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 0px;
    background: transparent;
}

/* Regular labels */
QLabel#field_label {
    color: #9ca3af;
    font-size: 12px;
    min-width: 90px;
    background: transparent;
}

QLabel#status_label {
    color: #e0e0e0;
    font-size: 12px;
    background: transparent;
}

/* Text inputs */
QLineEdit {
    background-color: #0e1012;
    border: 1px solid #2a2d32;
    border-radius: 6px;
    padding: 7px 10px;
    color: #e0e0e0;
    font-size: 13px;
    selection-background-color: #c8975a;
}
QLineEdit:focus {
    border: 1px solid #c8975a;
    background-color: #111315;
}
QLineEdit::placeholder {
    color: #404449;
}

/* Spin box */
QSpinBox {
    background-color: #0e1012;
    border: 1px solid #2a2d32;
    border-radius: 6px;
    padding: 6px 8px;
    color: #e0e0e0;
    font-size: 13px;
}
QSpinBox:focus { border-color: #c8975a; }
QSpinBox::up-button, QSpinBox::down-button {
    background: #1e2024;
    border: none;
    width: 18px;
}
QSpinBox::up-arrow  { border: 4px solid transparent; border-bottom: 5px solid #8a8f98; width:0; height:0; }
QSpinBox::down-arrow{ border: 4px solid transparent; border-top:    5px solid #8a8f98; width:0; height:0; }

/* Combo box */
QComboBox {
    background-color: #0e1012;
    border: 1px solid #2a2d32;
    border-radius: 6px;
    padding: 6px 10px;
    color: #e0e0e0;
    font-size: 13px;
}
QComboBox:focus { border-color: #c8975a; }
QComboBox::drop-down { border: none; width: 24px; }
QComboBox::down-arrow { border: 4px solid transparent; border-top: 5px solid #8a8f98; width:0; height:0; }
QComboBox QAbstractItemView {
    background-color: #1a1c1f;
    border: 1px solid #2a2d32;
    selection-background-color: #c8975a33;
    selection-color: #e0e0e0;
    outline: none;
}

/* Primary upload button */
QPushButton#upload_btn {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #b8823e, stop:1 #c8975a);
    color: #111214;
    border: none;
    border-radius: 7px;
    padding: 10px 24px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.5px;
    min-height: 38px;
}
QPushButton#upload_btn:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #c8975a, stop:1 #d9a96c);
}
QPushButton#upload_btn:pressed { background: #a06e2e; }
QPushButton#upload_btn:disabled {
    background: #2a2d32;
    color: #505560;
}

/* Secondary/ghost buttons */
QPushButton#browse_btn {
    background-color: #1e2024;
    color: #c8975a;
    border: 1px solid #c8975a44;
    border-radius: 6px;
    padding: 6px 14px;
    font-size: 12px;
}
QPushButton#browse_btn:hover { background-color: #262930; border-color: #c8975a88; }

/* Checkboxes */
QCheckBox {
    color: #9ca3af;
    font-size: 12px;
    spacing: 6px;
    background: transparent;
}
QCheckBox::indicator {
    width: 15px;
    height: 15px;
    border: 1px solid #2a2d32;
    border-radius: 4px;
    background: #0e1012;
}
QCheckBox::indicator:checked {
    background: #c8975a;
    border-color: #c8975a;
    image: none;
}
QCheckBox::indicator:hover { border-color: #c8975a; }

/* Progress bar */
QProgressBar {
    background-color: #0e1012;
    border: 1px solid #2a2d32;
    border-radius: 4px;
    height: 6px;
    text-align: center;
    color: transparent;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #b8823e, stop:1 #c8975a);
    border-radius: 4px;
}

/* Log console */
QLabel#log_console {
    background-color: #0e1012;
    border: 1px solid #1e2125;
    border-radius: 6px;
    color: #c8975a;
    font-family: "Consolas", "Fira Code", "Courier New", monospace;
    font-size: 11px;
    padding: 8px 10px;
    min-height: 46px;
}

/* Status badge */
QLabel#status_badge {
    background-color: #1e2024;
    border: 1px solid #2a2d32;
    border-radius: 10px;
    color: #9ca3af;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 10px;
}

/* Drop zone */
QFrame#drop_zone {
    background-color: #0e1012;
    border: 2px dashed #2a2d32;
    border-radius: 10px;
    min-height: 110px;
}
QFrame#drop_zone[drag_active="true"] {
    border-color: #c8975a;
    background-color: #c8975a0d;
}

QLabel#drop_label {
    color: #505560;
    font-size: 13px;
    background: transparent;
}
QLabel#drop_label_bold {
    color: #c8975a;
    font-size: 13px;
    font-weight: 700;
    background: transparent;
}

/* Divider */
QFrame#divider {
    background-color: #2a2d32;
    max-height: 1px;
    border: none;
}

/* Scrollbar */
QScrollBar:vertical {
    background: transparent;
    width: 6px;
}
QScrollBar::handle:vertical {
    background: #2a2d32;
    border-radius: 3px;
    min-height: 20px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }

/* Tab widget */
QTabWidget::pane {
    border: none;
    background: transparent;
}
QTabBar::tab {
    background: #1a1c1f;
    color: #9ca3af;
    border: 1px solid #2a2d32;
    border-bottom: none;
    border-radius: 6px 6px 0 0;
    padding: 7px 20px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background: #111214;
    color: #c8975a;
    border-bottom: 2px solid #c8975a;
}
QTabBar::tab:hover:!selected { background: #22252a; color: #e0e0e0; }

/* File browser tree */
QTreeWidget {
    background: #0e1012;
    border: 1px solid #2a2d32;
    border-radius: 6px;
    color: #e0e0e0;
    font-size: 12px;
    outline: none;
    show-decoration-selected: 1;
}
QTreeWidget::item {
    padding: 5px 4px;
    border-bottom: 1px solid #1a1c1f;
}
QTreeWidget::item:selected {
    background: #c8975a22;
    color: #e0e0e0;
}
QTreeWidget::item:hover:!selected { background: #1a1c1f; }
QHeaderView::section {
    background: #1a1c1f;
    color: #8a8f98;
    border: none;
    border-right: 1px solid #2a2d32;
    border-bottom: 1px solid #2a2d32;
    padding: 5px 8px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* Toolbar */
QToolBar {
    background: transparent;
    border: none;
    spacing: 4px;
    padding: 0px;
}
QPushButton#tb_btn {
    background: #1e2024;
    color: #c8975a;
    border: 1px solid #2a2d32;
    border-radius: 5px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 600;
}
QPushButton#tb_btn:hover { background: #262930; border-color: #c8975a55; }
QPushButton#tb_btn:pressed { background: #111214; }
QPushButton#tb_btn:disabled { color: #404449; border-color: #1e2024; }

QPushButton#tb_btn_danger {
    background: #1e2024;
    color: #f87171;
    border: 1px solid #2a2d32;
    border-radius: 5px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 600;
}
QPushButton#tb_btn_danger:hover { background: #2a1a1a; border-color: #f8717155; }
QPushButton#tb_btn_danger:disabled { color: #404449; border-color: #1e2024; }
"""

for _old, _new in (
    ("#111214", "#050506"),
    ("#0e1012", "#08090b"),
    ("#111315", "#0b0b0d"),
    ("#1a1c1f", "#101114"),
    ("#1e2024", "#15161a"),
    ("#22252a", "#1a1014"),
    ("#262930", "#241017"),
    ("#2a2d32", "#35101a"),
    ("#c8975a", "#e11d48"),
    ("#b8823e", "#7f1022"),
    ("#d9a96c", "#ff335f"),
    ("#a06e2e", "#5f0714"),
):
    STYLESHEET = STYLESHEET.replace(_old, _new)

for _radius in ("10px", "8px", "7px", "6px", "5px", "4px", "3px"):
    STYLESHEET = STYLESHEET.replace(f"border-radius: {_radius}", "border-radius: 0px")
    STYLESHEET = STYLESHEET.replace(f"border-radius:{_radius}", "border-radius:0px")
STYLESHEET = STYLESHEET.replace("border-radius: 0px 6px 0 0", "border-radius: 0px")
