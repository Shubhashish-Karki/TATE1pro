# TATE: Transparent Attendance Tracking Engine

TATE is an attendance tracking system developed using Python and OpenCV. It leverages facial recognition technology to ensure accurate and transparent attendance records.

## Features

- **Facial Recognition**: Utilizes OpenCV's Haar Cascade classifiers to detect and recognize faces.
- **Attendance Logging**: Records attendance data in CSV files for easy tracking and management.
- **User-Friendly Interface**: Provides a simple interface for adding new students and capturing their images.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shubhashish-Karki/TATE1pro.git
   cd TATE1pro
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Haar Cascade Classifier**:
   The project uses OpenCV's pre-trained Haar Cascade classifier for face detection. Ensure `haarcascade_frontalface_default.xml` is present in the project directory. If not, download it from [OpenCV's GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Usage

1. **Add New Student**:
   - Run `studentdetails.py` to add a new student's information and capture their images.
   - Captured images are stored in the `images` directory.

2. **Train the Model**:
   - Execute `train.py` to train the facial recognition model using the stored images.
   - This generates the `classifier.xml` file, which is used for recognition.

3. **Start Attendance Tracking**:
   - Run `attendance.py` to start the attendance tracking system.
   - The system will detect faces and log attendance in `attendance1.csv` and `attendance2.csv`.

## Project Structure

```
TATE1pro/
├── icons/
├── images/
├── .gitignore
├── README.md
├── attendance.py
├── attendance1.csv
├── attendance2.csv
├── classifier.xml
├── face_recognition.py
├── haarcascade_frontalface_default.xml
├── main.py
├── sample.py
├── studentdetails.py
├── train.py
```

- `icons/`: Contains icon images used in the application.
- `images/`: Stores captured images of students.
- `attendance.py`: Script to run the attendance tracking system.
- `attendance1.csv` & `attendance2.csv`: Files where attendance records are stored.
- `classifier.xml`: Generated model for facial recognition.
- `face_recognition.py`: Module for handling face recognition tasks.
- `haarcascade_frontalface_default.xml`: Pre-trained Haar Cascade classifier for face detection.
- `main.py`: Main script to run the application.
- `sample.py`: Sample script (purpose to be detailed).
- `studentdetails.py`: Script to add new students and capture their images.
- `train.py`: Script to train the facial recognition model.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [OpenCV](https://opencv.org/) for providing the tools necessary for computer vision tasks.
- [Python](https://www.python.org/) for being the backbone of this project.
- [GitHub](https://github.com/) for hosting this repository.

---

*Note: Ensure all scripts are executed in the correct order for the system to function properly.*

