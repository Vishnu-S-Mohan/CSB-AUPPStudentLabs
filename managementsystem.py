import csv
import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

class ManagementSystem:
    def __init__(self):
        self.data = None

    def process_file(self, filename):
        try:
            if filename.endswith((".csv", ".xlsx")):
                self.data = pd.read_excel(filename) if filename.endswith(".xlsx") else list(csv.DictReader(open(filename)))
            elif filename.endswith(".txt"):
                self.data = open(filename, 'r').read()
            else:
                print("Error: Unsupported file format.")
                self.data = None
        except Exception as e:
            print(f"Error processing file: {e}")
            self.data = None

    def transfer_data(self, filename):
        try:
            if filename.endswith(".csv"):
                pd.DataFrame(self.data).to_csv("Copied_File.csv", index=False)
            elif filename.endswith(".txt"):
                with open("Copied_File.txt", "w") as txtfile:
                    txtfile.write(str(self.data))
            elif filename.endswith(".xlsx"):
                pd.DataFrame(self.data).to_excel("Copied_File.xlsx", index=False)
            else:
                print("Error: Unsupported file format.")
        except Exception as e:
            print(f"Error transferring data: {e}")

    def fetch_web_data(self, url):
        try:
            with urlopen(url) as response:
                self.data = response.read().decode('utf-8')
        except (HTTPError, URLError) as e:
            print(f"Error fetching web data: {e}")
            self.data = None

    def analyze_content(self, filename):
        try:
            if filename.endswith(".csv"):
                pass_count = sum(float(row["Overall"]) > 50 for row in self.data)
                fail_count = len(self.data) - pass_count
                print(f"{pass_count} students have Passed the Overall scores. {fail_count} students have Failed the Overall scores.")
            else:
                print("Error: Unsupported file format for analysis.")
        except Exception as e:
            print(f"Error analyzing content: {e}")

    def generate_summary(self, filename):
        try:
            if filename.endswith(".csv"):
                for row in self.data:
                    print(f"{row['Last Name']} {row['First Name']} With an ID of {row['ID']} has an Overall of {row['Overall']} and needs improvements on {row['Improvement']}.")
            else:
                print("Error: Unsupported file format for generating a summary.")
        except Exception as e:
            print(f"Error generating summary: {e}")

# Example Usage:
ms = ManagementSystem()

# Replace 'your_file_here' with the actual file path
file_data = ms.process_file('SampleData.csv')
ms.transfer_data(file_data, 'SampleData.csv')

web_data = ms.fetch_web_data('http://example.com')
print(web_data)

ms.analyze_content(file_data, 'SampleData.csv')
ms.generate_summary(file_data, 'SampleData.csv')
