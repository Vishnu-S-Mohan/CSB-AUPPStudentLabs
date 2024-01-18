from managementsystem import *

def main():
    Options = input("Enter Number: 1=URL / 2=Filename: ")

    if Options == "1":
        url = input("Enter the URL:")
        data = ManagementSystem.fetch_web_data(url=url)
    elif Options == "2":
        filename = input("Enter the filename: ")
        data = ManagementSystem.process_file(filename=filename)
        ManagementSystem.transfer_data(data, filename=filename)
        ManagementSystem.analyze_content(data=data,filename=filename)
        ManagementSystem.generate_summary(data=data, filename=filename)
    else:
        print("Invalid")

main()