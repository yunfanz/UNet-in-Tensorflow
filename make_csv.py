import numpy as np
import os, fnmatch, csv

def find_files(directory, pattern='*.npz', sortby='shuffle'):
    '''Recursively finds all files matching the pattern.'''
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            files.append(os.path.join(root, filename))

    if sortby == 'auto':
	files = np.sort(files)
    elif sortby == 'shuffle':
	np.random.shuffle(files)
    return files

def write_csv(fname, rows):
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['paths'])
        for row in rows:
            writer.writerow([row])

if __name__ == "__main__":
    FILES = find_files('/data1/FRB/C/train_256time_res8_allampwidth/signa/')
    train_files = FILES[:int(0.9*len(FILES))]
    test_files = FILES[int(0.9*len(FILES)):]
    write_csv('train.csv', train_files)
    write_csv('test.csv', test_files)
