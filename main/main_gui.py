import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
)
from PyQt5.QtCore import Qt


class DroneControlApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Drone Control Application")
        self.setGeometry(100, 100, 600, 400)

        # Main tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.tabs.addTab(self.create_configuration_tab(), "Configuration")
        self.tabs.addTab(self.create_manual_control_tab(), "Manual Control")
        self.tabs.addTab(self.create_mapping_mode_tab(), "Mapping Mode")

    def create_configuration_tab(self):
        """Creates the Configuration tab."""
        tab = QWidget()
        layout = QVBoxLayout()

        # Add form fields for configuration
        layout.addWidget(QLabel("Drone IP Address:"))
        self.ip_address_input = QLineEdit()
        layout.addWidget(self.ip_address_input)

        layout.addWidget(QLabel("Drone Port:"))
        self.port_input = QLineEdit()
        layout.addWidget(self.port_input)

        save_button = QPushButton("Save Configuration")
        save_button.clicked.connect(self.save_configuration)
        layout.addWidget(save_button)

        tab.setLayout(layout)
        return tab

    def create_manual_control_tab(self):
        """Creates the Manual Control tab."""
        tab = QWidget()
        layout = QVBoxLayout()

        # Add control buttons
        layout.addWidget(QLabel("Manual Drone Controls:"))
        button_layout = QHBoxLayout()

        takeoff_button = QPushButton("Takeoff")
        takeoff_button.clicked.connect(self.takeoff)
        button_layout.addWidget(takeoff_button)

        land_button = QPushButton("Land")
        land_button.clicked.connect(self.land)
        button_layout.addWidget(land_button)

        layout.addLayout(button_layout)

        move_layout = QHBoxLayout()
        move_forward_button = QPushButton("Move Forward")
        move_forward_button.clicked.connect(self.move_forward)
        move_layout.addWidget(move_forward_button)

        move_backward_button = QPushButton("Move Backward")
        move_backward_button.clicked.connect(self.move_backward)
        move_layout.addWidget(move_backward_button)

        layout.addLayout(move_layout)
        tab.setLayout(layout)
        return tab

    def create_mapping_mode_tab(self):
        """Creates the Mapping Mode tab."""
        tab = QWidget()
        layout = QVBoxLayout()

        # Add placeholder for mapping functionality
        layout.addWidget(QLabel("Mapping Mode Status:"))
        self.mapping_status_label = QLabel("Not started")
        self.mapping_status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mapping_status_label)

        start_mapping_button = QPushButton("Start Mapping")
        start_mapping_button.clicked.connect(self.start_mapping)
        layout.addWidget(start_mapping_button)

        stop_mapping_button = QPushButton("Stop Mapping")
        stop_mapping_button.clicked.connect(self.stop_mapping)
        layout.addWidget(stop_mapping_button)

        tab.setLayout(layout)
        return tab

    # Configuration tab actions
    def save_configuration(self):
        ip_address = self.ip_address_input.text()
        port = self.port_input.text()
        self.statusBar().showMessage(f"Configuration saved: IP={ip_address}, Port={port}")

    # Manual control tab actions
    def takeoff(self):
        self.statusBar().showMessage("Drone taking off...")

    def land(self):
        self.statusBar().showMessage("Drone landing...")

    def move_forward(self):
        self.statusBar().showMessage("Drone moving forward...")

    def move_backward(self):
        self.statusBar().showMessage("Drone moving backward...")

    # Mapping mode tab actions
    def start_mapping(self):
        self.mapping_status_label.setText("Mapping started")
        self.statusBar().showMessage("Mapping mode started...")

    def stop_mapping(self):
        self.mapping_status_label.setText("Mapping stopped")
        self.statusBar().showMessage("Mapping mode stopped...")

# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DroneControlApp()
    window.show()
    sys.exit(app.exec_())

