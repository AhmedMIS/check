import csv


def main():
    '''This code is just an overview of combining required coulumn from same CSV file with using CSV
        library'''
    with open('name.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Opening the new file for the
        with open('new_names.csv', 'w') as new_file:
            fieldnames = ['first_name', 'last_name']
            # writing new file with dictionery
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

            csv_writer.writeheader()

            for line in csv_reader:
                # Deleting the non required column
                del line['email']
                csv_writer.writerow(line)


if __name__ == '__main__':
    main()
