import unittest
import pandas as pd

class TestDataToSqlite(unittest.TestCase):
    def test_import_pandas(self):
        import pandas
        self.assertIsNotNone(pandas)
        print("Pandas imported successfully")

    def test_read_csv(self):
        hospital = pd.read_csv(r"C:\Users\Abhishek Yadav\OneDrive - rgipt.ac.in\Desktop\DiseasePrediction\dataset\HospitalDetails.csv")
        self.assertIsNotNone(hospital)
        print("CSV file read successfully")

if __name__ == '__main__':
    unittest.main()